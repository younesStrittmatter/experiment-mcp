"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '83d0363dbac8f05c2c5c59d674f3596bb1205ab2e70916e6690629cb91036ca6'
__exp_qualname__ = 'sweetbean.check_java'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'check_java'
TOOL_DESCRIPTION = 'Call this tool before any pipeline step that requires Java (e.g., SweetPea\'s SAT-solver backend or SweetBean\'s headless compilation). It verifies that a Java runtime is present on the host and exits the process immediately if it is not. Returns nothing on success; raises a hard exit on failure.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis function calls sys.exit(1) — not a Python exception — if Java is missing, which will terminate the MCP server process rather than returning an error to the agent. Only call it when Java is genuinely required for the next step; do not call it as a general health check during ordinary SweetBean HTML generation, which does not need Java.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'This function calls sys.exit(1) — not a Python exception — if Java is missing, which will terminate the MCP server process rather than returning an error to the agent. Only call it when Java is genuinely required for the next step; do not call it as a general health check during ordinary SweetBean HTML generation, which does not need Java.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.check_java
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
    def check_java(args: dict[str, Any] | None = None) -> Any:
        "Call this tool before any pipeline step that requires Java (e.g., SweetPea's SAT-solver backend or SweetBean's headless compilation)."
        return _impl(args or {})
