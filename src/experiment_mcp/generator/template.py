"""Render a generated tool module from a :class:`SymbolMeta` + :class:`ToolSpec`.

Symmetric with ``psyneulink_mcp.generator.template`` apart from one
key difference: the template is **multi-root**. SweetPea and SweetBean
are independent top-level packages, so the generated module imports
the symbol from whichever one ``symbol.root_module`` says it came from
(``import sweetpea as sp`` for sweetpea-rooted symbols, ``import
sweetbean as sb`` for sweetbean-rooted ones). The first regen wires
every generated tool to ``args: dict[str, Any]`` for the same FastMCP
schema-derivation reason as the sibling.
"""

from __future__ import annotations

import json
import keyword
import pprint
import re
from typing import Any

from .adapters.base import ToolSpec
from .introspection import SymbolMeta

_SNAKE1 = re.compile(r"(.)([A-Z][a-z]+)")
_SNAKE2 = re.compile(r"([a-z0-9])([A-Z])")

# Short import aliases per top-level package — purely cosmetic in the
# generated module body, but consistent across the repo so reviewers
# eyeballing diffs across tools see the same names everywhere.
_ROOT_ALIAS: dict[str, str] = {
    "sweetpea": "sp",
    "sweetbean": "sb",
}


def snake_case(name: str) -> str:
    """``CrossBlock`` -> ``cross_block``;
    ``HTMLStimulus`` -> ``html_stimulus`` (treats all-caps runs as one word).
    """
    s = _SNAKE1.sub(r"\1_\2", name)
    s = _SNAKE2.sub(r"\1_\2", s).lower()
    s = re.sub(r"[^0-9a-z_]+", "_", s).strip("_")
    return s or "tool"


def tool_name_for(symbol: SymbolMeta) -> str:
    """Tool name an MCP client sees.

    Classes get a ``create_`` prefix because the underlying call is
    ``cls(**kwargs)`` — naming it ``create_cross_block`` reads better
    to an LLM consumer than just ``cross_block``. Functions and methods
    keep their snake-cased name.
    """
    base = snake_case(symbol.short_name)
    if keyword.iskeyword(base):
        base = f"{base}_"
    if symbol.kind == "class":
        return f"create_{base}"
    return base


def module_filename_for(symbol: SymbolMeta) -> str:
    """Filename inside ``tools/generated/`` for this symbol.

    Methods are namespaced by their owning class so two same-named
    methods on different classes don't collide on the filesystem.
    Classes/functions are namespaced by the root package so a future
    name collision between sweetpea and sweetbean (e.g. they both
    expose a ``Block`` class) lands in two distinct files.
    """
    return f"{module_stem_for(symbol)}.py"


def module_stem_for(symbol: SymbolMeta) -> str:
    """Importable stem of the generated module (filename without ``.py``).

    For classes / functions we prefix the snake-cased name with the
    root package (``sweetpea_block``, ``sweetbean_block``) since both
    SweetPea and SweetBean expose a top-level ``Block`` and the
    generated layer must not collide. For methods we additionally
    include the owning class to disambiguate same-named methods on
    different classes.
    """
    if symbol.kind == "method" and symbol.class_short_name:
        return (
            f"{snake_case(symbol.root_module)}_"
            f"{snake_case(symbol.class_short_name)}_"
            f"{snake_case(symbol.short_name)}"
        )
    return f"{snake_case(symbol.root_module)}_{snake_case(symbol.short_name)}"


def render_module(
    symbol: SymbolMeta,
    spec: ToolSpec,
    *,
    generated_by: str,
) -> str:
    """Return the full Python source for the generated tool module."""
    tool_name = tool_name_for(symbol)
    description_raw = (spec.get("description") or "").strip()
    parameters = spec.get("parameters") or {}
    notes = (spec.get("notes") or "").strip()

    description_with_schema = _description_with_schema(
        description_raw, parameters, notes
    )

    parameters_literal = pprint.pformat(parameters, sort_dicts=True, width=88, indent=2)

    docstring_first_line = _first_sentence(description_raw) or tool_name

    root = symbol.root_module
    alias = _ROOT_ALIAS.get(root, root)

    if symbol.kind == "method":
        impl_lines = _render_method_impl(symbol, alias=alias)
    else:
        impl_lines = _render_constructor_impl(symbol, alias=alias)

    lines = [
        '"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""',
        "",
        "from __future__ import annotations",
        "",
        "import json",
        "from typing import Any",
        "",
        f"import {root} as {alias}",
        "",
        "from experiment_mcp import handles",
        "from experiment_mcp.feedback import captured_tool",
        "",
        f"__source_sha256__ = {symbol.source_sha256!r}",
        f"__exp_qualname__ = {symbol.qualname!r}",
        f"__exp_kind__ = {symbol.kind!r}",
        f"__exp_root__ = {root!r}",
        f"__generated_by__ = {generated_by!r}",
        "",
        f"TOOL_NAME = {tool_name!r}",
        f"TOOL_DESCRIPTION = {description_with_schema!r}",
        f"TOOL_PARAMETERS = {parameters_literal}",
        f"TOOL_NOTES = {notes!r}",
        "",
        "",
        *impl_lines,
        "",
        "",
        "def register(mcp: Any) -> None:",
        '    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)',
        # FastMCP derives an MCP `inputSchema` from the function signature.
        # `**kwargs` would surface as a single required `kwargs` arg
        # rather than passing through the LLM's chosen parameters, so
        # we declare an explicit `args: dict` parameter that the impl
        # then unpacks. The real per-symbol schema lives in
        # TOOL_PARAMETERS / TOOL_DESCRIPTION for the LLM consumer.
        f"    def {tool_name}(args: dict[str, Any] | None = None) -> Any:",
        f"        {docstring_first_line!r}",
        "        return _impl(args or {})",
        "",
    ]
    return "\n".join(lines)


def _render_constructor_impl(symbol: SymbolMeta, *, alias: str) -> list[str]:
    """``_impl`` body for class / function symbols.

    Single shape for both classes and module-level callables: build the
    result, then either return it as-is (JSON-friendly) or stash it in
    the handles registry and return a handle payload. Pre-resolution
    ``kwargs`` is what ``handles.record_call`` wants — the resolver
    mutates a copy.
    """
    return [
        "def _impl(kwargs: dict[str, Any]) -> Any:",
        f"    target = {alias}.{symbol.short_name}",
        "    resolved = handles.resolve_in(kwargs)",
        "    result = target(**resolved)",
        "    try:",
        "        json.dumps(result)",
        "    except (TypeError, ValueError):",
        "        payload = handles.register_handle(result)",
        "        handles.record_call(",
        "            TOOL_NAME,",
        "            kwargs,",
        "            result_handle=payload.get('handle') if isinstance(payload, dict) else None,",
        '            tool_layer="generated",',
        "        )",
        "        return payload",
        '    handles.record_call(TOOL_NAME, kwargs, result_handle=None, tool_layer="generated")',
        "    return result",
    ]


def _render_method_impl(symbol: SymbolMeta, *, alias: str) -> list[str]:
    """``_impl`` body for method symbols.

    Generic dispatcher with no per-method special cases (yet). The
    agent is expected to pass the bound instance as a handle under a
    kwarg whose natural name is the lowercased class name. The runtime
    resolver in ``handles.resolve_in`` rehydrates the handle, which is
    then popped here before dispatch. Once the feedback loop surfaces
    a per-method gotcha, hand-tune it in a sibling-style helper rather
    than baking it into this template.
    """
    cls_name = symbol.class_short_name or ""
    method_name = symbol.short_name
    instance_kwarg = snake_case(cls_name) or "instance"
    return [
        "def _impl(kwargs: dict[str, Any]) -> Any:",
        f"    cls = {alias}.{cls_name}",
        "    resolved = handles.resolve_in(kwargs)",
        f"    instance = resolved.pop({instance_kwarg!r}, None)",
        "    if instance is None:",
        "        raise TypeError(",
        f"            f\"{{TOOL_NAME}} requires kwarg {instance_kwarg!r} \"",
        f"            f\"(handle returned by create_{snake_case(cls_name)}).\"",
        "        )",
        "    if not isinstance(instance, cls):",
        "        raise TypeError(",
        f"            f\"{{TOOL_NAME}} got {instance_kwarg!r}={{type(instance).__name__}}, \"",
        f"            f\"expected {cls_name}.\"",
        "        )",
        f"    result = instance.{method_name}(**resolved)",
        "    try:",
        "        json.dumps(result)",
        "    except (TypeError, ValueError):",
        "        payload = handles.register_handle(result)",
        "        handles.record_call(",
        "            TOOL_NAME,",
        "            kwargs,",
        "            result_handle=payload.get('handle') if isinstance(payload, dict) else None,",
        '            tool_layer="generated",',
        "        )",
        "        return payload",
        '    handles.record_call(TOOL_NAME, kwargs, result_handle=None, tool_layer="generated")',
        "    return result",
    ]


def render_init(stems: list[str]) -> str:
    """Render the ``tools/generated/__init__.py`` index module."""
    sorted_stems = sorted(set(stems))
    lines = [
        '"""Auto-generated index. Do not edit by hand.',
        "",
        "Rewritten by scripts/generate_tools.py on every successful run.",
        "On a fresh clone (no regen yet) the modules tuple is empty and",
        "register_all is a safe no-op.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
    ]
    if sorted_stems:
        lines.append(f"from . import {', '.join(sorted_stems)}")
        lines.append("")
        lines.append(f"ALL = ({', '.join(sorted_stems)},)")
    else:
        lines.append("ALL: tuple[Any, ...] = ()")
    lines += [
        "",
        "",
        "def register_all(mcp: Any) -> None:",
        '    """Register every generated tool module with ``mcp``."""',
        "    for module in ALL:",
        "        module.register(mcp)",
        "",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# helpers                                                                     #
# --------------------------------------------------------------------------- #


def _description_with_schema(
    description: str, parameters: dict[str, Any], notes: str
) -> str:
    """Compose the user-visible description used for MCP registration.

    Includes the JSON Schema and notes inline so an LLM agent sees them
    in the tool listing even though FastMCP can't validate against them
    yet (see module docstring).
    """
    parts: list[str] = []
    if description:
        parts.append(description.strip())
    if parameters:
        parts.append("")
        parts.append("Parameters (JSON Schema):")
        parts.append(json.dumps(parameters, indent=2, sort_keys=True))
    if notes:
        parts.append("")
        parts.append("Notes:")
        parts.append(notes.strip())
    return "\n".join(parts)


_SENTENCE_END = re.compile(r"[.!?](?:\s|$)")


def _first_sentence(text: str) -> str:
    """First sentence of a description, for use as the function docstring."""
    if not text:
        return ""
    match = _SENTENCE_END.search(text)
    if match is None:
        return text.strip().splitlines()[0]
    return text[: match.end()].strip()
