"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '492df2d2c8dbb561f6b8daf7633adfab7e1c893c9d65939f51ae6dfd461fc37f'
__exp_qualname__ = 'sweetpea.Constraint'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_constraint'
TOOL_DESCRIPTION = 'Do NOT call this tool directly. `sweetpea.Constraint` is an abstract base class defining the interface that all SweetPea constraint types implement; instantiating it raises `TypeError`. Use a concrete constraint subclass instead (e.g. `Exclude`, `Pin`, `MinimumTrials`, `AtMostKInARow`, `ExactlyKInARow`) to restrict or shape the trial sequences produced in step 1 of the SweetPea → SweetBean pipeline before calling a crossing or synthesis tool.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n`Constraint` is decorated with `@ABC` and all three of its key methods (`validate`, `apply`, `potential_sample_conforms`) are `@abstractmethod`. Calling `sweetpea.Constraint()` directly will raise `TypeError: Can\'t instantiate abstract class Constraint`. The tool is registered for completeness and introspection only — the agent should always route to a concrete constraint tool. If no concrete subclass tool matches your need, check the SweetPea docs for the right class name and use that tool instead.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = "`Constraint` is decorated with `@ABC` and all three of its key methods (`validate`, `apply`, `potential_sample_conforms`) are `@abstractmethod`. Calling `sweetpea.Constraint()` directly will raise `TypeError: Can't instantiate abstract class Constraint`. The tool is registered for completeness and introspection only — the agent should always route to a concrete constraint tool. If no concrete subclass tool matches your need, check the SweetPea docs for the right class name and use that tool instead."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Constraint
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
    def create_constraint(args: dict[str, Any] | None = None) -> Any:
        'Do NOT call this tool directly.'
        return _impl(args or {})
