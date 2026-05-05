"""In-process registry of live experiment-construction objects.

The eventual MCP tools in this repo will return things that are *not*
JSON-serialisable — a SweetPea ``Block``, a SweetBean ``Trial``, a
list of ``Stimulus`` objects, a generated jsPsych payload, a pandas
DataFrame produced by a sim run, etc. Each such object is stashed
here under a stable string handle and the agent only ever sees the
handle plus light metadata. Subsequent tool calls that need the live
object pass the handle string back; the impl walks its kwargs and
rehydrates each handle into the live object before calling into the
domain library.

Polymorphism note: unlike the sibling ``psyneulink_mcp.handles`` —
which has a baked-in resolver for PNL function-class-name strings
(``{"function": "Linear"}`` → ``pnl.Linear``) — this registry stays
**deliberately polymorphic**. SweetPea ``Block`` / ``Factor``,
SweetBean ``Trial`` / ``Stimulus`` / ``Block``, raw dicts from
jsPsych, pandas frames from runs, and PSYCHE ``Dataset`` instances
should all coexist behind the same handle protocol. We do *not*
import ``sweetpea`` / ``sweetbean`` here — that would defeat the
"server boots without the experiments extra" rule. Class-name
auto-resolution can be added later if a concrete pain point emerges.

The registry is **process-scoped**: a fresh MCP subprocess starts
with an empty dict, and entries live until the process dies. Each
``experiment-agent`` chat session spawns its own MCP, which matches
the natural "experiment-design session" lifecycle. We deliberately
do not persist handles or share them across sessions — the moment
we'd need that, the right move is real serialisation (SweetBean
already round-trips through JSON), not a pickle of opaque strings.
"""

from __future__ import annotations

import copy
import re
import uuid
import warnings
from dataclasses import dataclass, field
from typing import Any, Literal

HANDLE_PREFIX = "h_"
HANDLE_PATTERN = re.compile(r"^h_[0-9a-f]{12}$")

_HANDLES: dict[str, Any] = {}

# ---- Object revision counter --------------------------------------------- #
#
# Mirrors `psyneulink_mcp.handles._COMPOSITION_REVISION`: the (eventual) UI
# wants a cheap "did this experiment-design change?" check before re-rendering
# a block diagram or recompiling a SweetBean program. Tools that mutate the
# underlying object in place (e.g. a future ``add_factor`` curated tool)
# should call ``bump_revision(handle)`` after the mutation succeeds. Pure
# read-only tools (``compile_task``, ``inspect_block``) must not bump.
#
# Process-scoped, like ``_HANDLES`` and the journal.

_OBJECT_REVISION: dict[str, int] = {}


def get_revision(handle: str) -> int:
    """Current revision of a handle (0 if never bumped)."""
    return _OBJECT_REVISION.get(handle, 0)


def bump_revision(handle: str) -> int:
    """Increment the revision counter for ``handle`` and return the new value.

    No-op (returns 0) if the handle isn't currently registered — prevents
    stray bumps from leaking into the dict.
    """
    if handle not in _HANDLES:
        return 0
    _OBJECT_REVISION[handle] = _OBJECT_REVISION.get(handle, 0) + 1
    return _OBJECT_REVISION[handle]


# ---- Session journal ----------------------------------------------------- #
#
# Every tool's ``_impl`` (curated or generated) appends a ``JournalEntry``
# here. A future ``persistence.export_python_script`` (mirroring the
# sibling) will walk the journal to emit a runnable ``.py`` script that
# reproduces the experiment-design built in this session.
#
# The journal is process-scoped, just like ``_HANDLES``.

ToolLayer = Literal["generated", "curated"]


@dataclass
class JournalEntry:
    """One recorded tool call.

    ``args`` preserves handle strings verbatim (i.e. it is the PRE-resolved
    kwargs dict the tool was called with). ``result_handle`` is the handle
    string the tool returned, or ``None`` for tools that don't produce one
    (``compile_task`` returning a JSON-serialisable jsPsych program,
    ``run_task`` returning a Dataset, etc.). ``tool_layer`` distinguishes
    generated wrappers from curated tools.
    """

    tool_name: str
    args: dict[str, Any]
    result_handle: str | None = None
    tool_layer: ToolLayer = "generated"
    extras: dict[str, Any] = field(default_factory=dict)


_JOURNAL: list[JournalEntry] = []
_JOURNAL_CAP = 5000
_JOURNAL_CAP_WARNED = False


def is_handle_string(value: Any) -> bool:
    """True iff *value* looks like a registered handle ID."""
    return isinstance(value, str) and HANDLE_PATTERN.match(value) is not None


def _handle_payload(handle: str, obj: Any) -> dict[str, Any]:
    return {
        "handle": handle,
        "type": type(obj).__name__,
        "name": getattr(obj, "name", None) or "",
        "repr": repr(obj),
    }


def register_handle(obj: Any) -> dict[str, Any]:
    """Stash *obj* and return its handle payload.

    ``None`` is returned as-is; the agent should never see a handle for
    something it could just read directly. Primitives that round-trip
    through JSON are caller's responsibility — the eventual tool wrappers
    decide whether to register or return inline (see the sibling's
    ``method_helpers._wrap_result`` for the canonical pattern).
    """
    if obj is None:
        return None  # type: ignore[return-value]
    handle = HANDLE_PREFIX + uuid.uuid4().hex[:12]
    _HANDLES[handle] = obj
    return _handle_payload(handle, obj)


def resolve_handle(handle: str) -> Any:
    """Return the live object for *handle*, raising on miss."""
    try:
        return _HANDLES[handle]
    except KeyError as exc:
        raise KeyError(
            f"unknown handle: {handle!r}. "
            "Either it was never created in this session or the MCP "
            "subprocess restarted and lost in-memory state."
        ) from exc


def resolve_in(value: Any) -> Any:
    """Walk *value* recursively, swapping handle strings for live objects.

    Used by every tool's ``_impl`` so an agent can pass a previously-returned
    handle anywhere a SweetPea / SweetBean constructor expects an object:
    ``compile_task(args={"block": "h_abc..."})`` just works.

    Polymorphic by design (see module docstring): no class-name
    auto-resolution and no domain-library imports happen here.
    """
    if is_handle_string(value):
        return resolve_handle(value)
    if isinstance(value, list):
        return [resolve_in(item) for item in value]
    if isinstance(value, tuple):
        return tuple(resolve_in(item) for item in value)
    if isinstance(value, dict):
        return {key: resolve_in(item) for key, item in value.items()}
    return value


def list_handles() -> list[dict[str, Any]]:
    """Snapshot of every handle currently alive in this MCP process."""
    return [_handle_payload(handle, obj) for handle, obj in _HANDLES.items()]


def describe_handle(handle: str) -> dict[str, Any]:
    """Single-handle view (errors if unknown)."""
    return _handle_payload(handle, resolve_handle(handle))


def record_call(
    tool_name: str,
    args: dict[str, Any],
    result_handle: str | None = None,
    tool_layer: ToolLayer = "generated",
) -> None:
    """Append one ``JournalEntry`` to the per-process session journal.

    ``args`` is **deep-copied** so that any subsequent in-place mutation by
    the caller (e.g. ``handles.resolve_in`` swapping handle strings for live
    objects on the same dict) cannot corrupt the journal. The dict that
    lands in the journal therefore preserves handle strings as the agent
    originally passed them — exactly what a future ``export_python_script``
    will need.

    When the journal exceeds ``_JOURNAL_CAP``, a one-shot ``UserWarning``
    fires (subsequent overflows stay silent) so a runaway session is
    visible but doesn't drown the operator in noise.
    """
    global _JOURNAL_CAP_WARNED
    try:
        snapshot_args = copy.deepcopy(args) if args else {}
    except Exception:
        snapshot_args = dict(args) if args else {}
    _JOURNAL.append(
        JournalEntry(
            tool_name=tool_name,
            args=snapshot_args,
            result_handle=result_handle,
            tool_layer=tool_layer,
        )
    )
    if len(_JOURNAL) > _JOURNAL_CAP and not _JOURNAL_CAP_WARNED:
        _JOURNAL_CAP_WARNED = True
        warnings.warn(
            f"experiment-mcp session journal exceeded {_JOURNAL_CAP} entries; "
            "exported scripts may grow large. Consider clearing handles "
            "between experiment-design sessions.",
            stacklevel=2,
        )


def journal_snapshot() -> list[JournalEntry]:
    """Return a list copy of the current journal (mutating it is safe)."""
    return list(_JOURNAL)


def clear_journal() -> int:
    """Drop the session journal; returns count cleared."""
    global _JOURNAL_CAP_WARNED
    n = len(_JOURNAL)
    _JOURNAL.clear()
    _JOURNAL_CAP_WARNED = False
    return n


def clear_handles() -> int:
    """Drop everything; primarily for tests. Returns count of handles cleared.

    Also clears the session journal and the revision counter as side-effects
    — callers that need to distinguish the counts can call
    :func:`clear_journal` first, or inspect ``len(journal_snapshot())``
    before calling.
    """
    n = len(_HANDLES)
    _HANDLES.clear()
    _OBJECT_REVISION.clear()
    clear_journal()
    return n
