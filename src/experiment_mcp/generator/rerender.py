"""Re-template every already-generated tool module without calling the LLM.

Symmetric with ``psyneulink_mcp.generator.rerender`` apart from the
metadata constant names (``__exp_qualname__`` / ``__exp_kind__`` /
``__exp_root__``). Used when only ``template.render_module`` has changed
(impl shape, import list, registration boilerplate) and the LLM-produced
metadata (``TOOL_DESCRIPTION``, ``TOOL_PARAMETERS``, ``TOOL_NOTES``) on
disk is still correct. Avoids the cost and nondeterminism of a full regen.

Strategy: read each module on disk, AST-extract the metadata constants
literally, reconstruct a stub :class:`SymbolMeta` plus the original
:class:`ToolSpec`, then call :func:`render_module`.
"""

from __future__ import annotations

import ast
from pathlib import Path
from typing import Any

from .adapters.base import ToolSpec
from .introspection import SymbolMeta
from .template import render_module

_REQUIRED_CONSTANTS = (
    "__source_sha256__",
    "__exp_qualname__",
    "__exp_kind__",
    "__exp_root__",
    "__generated_by__",
    "TOOL_NAME",
    "TOOL_DESCRIPTION",
    "TOOL_PARAMETERS",
    "TOOL_NOTES",
)


class RerenderError(RuntimeError):
    """Raised when a module on disk doesn't have the expected metadata."""


def _extract_constants(source: str, path: Path) -> dict[str, Any]:
    tree = ast.parse(source, filename=str(path))
    out: dict[str, Any] = {}
    wanted = set(_REQUIRED_CONSTANTS)
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        if target.id not in wanted:
            continue
        try:
            out[target.id] = ast.literal_eval(node.value)
        except ValueError as exc:
            raise RerenderError(
                f"{path}: could not literal-eval constant {target.id}: {exc}"
            ) from exc
    missing = sorted(set(_REQUIRED_CONSTANTS) - out.keys())
    if missing:
        raise RerenderError(
            f"{path}: missing required constants: {missing}"
        )
    return out


def _strip_schema_augmentation(description_with_schema: str) -> str:
    """Recover the raw description string from the augmented one.

    ``template._description_with_schema`` joins the raw description with
    the JSON Schema and notes via two markers. Splitting on the first
    one we encounter recovers the original.
    """
    text = description_with_schema
    for marker in ("\n\nParameters (JSON Schema):", "\n\nNotes:"):
        if marker in text:
            text = text.split(marker, 1)[0]
            break
    return text.strip()


def rerender_path(path: Path) -> Path:
    """Rewrite *path* using the current template; return the same path."""
    source = path.read_text(encoding="utf-8")
    constants = _extract_constants(source, path)

    qualname: str = constants["__exp_qualname__"]
    kind: str = constants["__exp_kind__"]
    root: str = constants["__exp_root__"]

    if kind not in {"class", "function", "method"}:
        raise RerenderError(
            f"{path}: unknown __exp_kind__ {kind!r}; expected class|function|method"
        )

    # Reconstruct a minimal SymbolMeta. Source / docstring / module
    # are not consulted by render_module — only qualname, kind,
    # source_sha256, and (transitively via root_module) the qualname's
    # first segment matter. We synthesise a module stub that points at
    # the package root, which is enough for the template.
    symbol = SymbolMeta(
        qualname=qualname,
        kind=kind,  # type: ignore[arg-type]
        source="",
        docstring=None,
        module=root,
        source_sha256=constants["__source_sha256__"],
    )

    parameters: dict[str, Any] = constants["TOOL_PARAMETERS"] or {}
    notes: str = constants["TOOL_NOTES"] or ""
    description_raw = _strip_schema_augmentation(constants["TOOL_DESCRIPTION"])

    spec: ToolSpec = {
        "description": description_raw,
        "parameters": parameters,
        "notes": notes,
    }

    rendered = render_module(
        symbol, spec, generated_by=constants["__generated_by__"]
    )
    text = rendered if rendered.endswith("\n") else rendered + "\n"
    path.write_text(text, encoding="utf-8")
    return path


def rerender_directory(generated_dir: Path) -> tuple[list[Path], list[tuple[Path, str]]]:
    """Rewrite every ``*.py`` in *generated_dir* (excluding ``__init__.py``).

    Returns ``(written, failures)`` where ``failures`` is a list of
    ``(path, error_message)`` pairs.
    """
    written: list[Path] = []
    failures: list[tuple[Path, str]] = []
    if not generated_dir.is_dir():
        return written, failures
    for path in sorted(generated_dir.iterdir()):
        if path.suffix != ".py" or path.name.startswith("__"):
            continue
        try:
            rerender_path(path)
        except (RerenderError, OSError, ValueError) as exc:
            failures.append((path, str(exc)))
            continue
        written.append(path)
    return written, failures


__all__ = ["rerender_path", "rerender_directory", "RerenderError"]
