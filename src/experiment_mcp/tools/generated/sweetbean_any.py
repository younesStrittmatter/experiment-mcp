"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'b597e7d4bf519e68346ced3cb1944f5c12dc0cb00c2a573489088a05dba4a131'
__exp_qualname__ = 'sweetbean.block.Any'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_any'
TOOL_DESCRIPTION = 'Do not call this tool. `sweetbean.block.Any` is a re-export of Python\'s `typing.Any` — a static type annotation sentinel, not a constructable SweetBean object. Attempting to instantiate it raises `TypeError` at runtime. No agent workflow step maps to this symbol; use the concrete SweetBean tools (`sweetbean_block`, `sweetbean_trial_spec`, etc.) to build experiment pipelines.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis symbol is `typing.Any` re-exported from `sweetbean.block`. Its `__new__` unconditionally raises `TypeError: Any cannot be instantiated` when called directly. The generator picked it up as a class in the module namespace, but it is purely a type-checking construct with no runtime use. Any invocation of this tool will fail.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'This symbol is `typing.Any` re-exported from `sweetbean.block`. Its `__new__` unconditionally raises `TypeError: Any cannot be instantiated` when called directly. The generator picked it up as a class in the module namespace, but it is purely a type-checking construct with no runtime use. Any invocation of this tool will fail.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Any
    resolved = handles.resolve_in(kwargs)
    result = target(**resolved)
    try:
        json.dumps(result)
    except (TypeError, ValueError):
        payload = handles.register_handle(result)
        handles.record_call(
            TOOL_NAME,
            kwargs,
            result_handle=payload.get('handle') if isinstance(payload, dict) else None,
            tool_layer="generated",
        )
        return payload
    handles.record_call(TOOL_NAME, kwargs, result_handle=None, tool_layer="generated")
    return result


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_any(args: dict[str, Any] | None = None) -> Any:
        'Do not call this tool.'
        return _impl(args or {})
