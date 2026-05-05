"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '8dba3336011ea479e0102b0070f697326470c104c6ed8a7c37b5ea1387f60148'
__exp_qualname__ = 'sweetbean.block.CodeVariable'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_code_variable'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the pipeline when a SweetBean stimulus or trial parameter needs a value derived from raw JavaScript code rather than a static Python value — for example, reading from `jsPsych.data`, computing elapsed time, or accessing browser state. Pass the returned handle wherever a SweetBean variable is accepted (e.g., as a stimulus property or trial argument). The result is a handle to a `CodeVariable` instance that emits `let {name}={value};` when the trial initialises.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "A valid JavaScript identifier. This becomes the variable name in the emitted `let` declaration and is used to reference the value elsewhere in the trial\'s JS context.",\n      "type": "string"\n    },\n    "value": {\n      "description": "A JavaScript expression assigned to the variable verbatim (e.g., `jsPsych.data.get().last(1).values()[0].rt`). Must be syntactically valid JS; no escaping or quoting is applied.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "name",\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\n`value` is injected into the JS output without any sanitization — the generated code is `let {name}={value};`, so invalid JS will silently produce a broken experiment. The name must be a valid JS identifier (no spaces, no reserved words). This variable is initialised once at trial start; it does not reactively update. If you only need a static Python-side value, prefer `DataVariable` or `FunctionVariable` instead.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'A valid JavaScript identifier. This '
                                           'becomes the variable name in the emitted '
                                           '`let` declaration and is used to reference '
                                           "the value elsewhere in the trial's JS "
                                           'context.',
                            'type': 'string'},
                  'value': { 'description': 'A JavaScript expression assigned to the '
                                            'variable verbatim (e.g., '
                                            '`jsPsych.data.get().last(1).values()[0].rt`). '
                                            'Must be syntactically valid JS; no '
                                            'escaping or quoting is applied.',
                             'type': 'string'}},
  'required': ['name', 'value'],
  'type': 'object'}
TOOL_NOTES = '`value` is injected into the JS output without any sanitization — the generated code is `let {name}={value};`, so invalid JS will silently produce a broken experiment. The name must be a valid JS identifier (no spaces, no reserved words). This variable is initialised once at trial start; it does not reactively update. If you only need a static Python-side value, prefer `DataVariable` or `FunctionVariable` instead.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.CodeVariable
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
    def create_code_variable(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the pipeline when a SweetBean stimulus or trial parameter needs a value derived from raw JavaScript code rather than a static Python value — for example, reading from `jsPsych.data`, computing elapsed time, or accessing browser state.'
        return _impl(args or {})
