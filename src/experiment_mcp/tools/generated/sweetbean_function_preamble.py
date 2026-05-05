"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '6cdd87f9f36f5caa8e6fcea538cbd0ecee31da38d6f36dd1a8787d0909a04f1b'
__exp_qualname__ = 'sweetbean.experiment.FUNCTION_PREAMBLE'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'function_preamble'
TOOL_DESCRIPTION = 'Call this tool when you need the raw JavaScript opening declaration string for a jsPsych `runExperiment()` function — either synchronous or async. It returns a partial JS snippet (the function header plus a black-background body init) that you can prepend to experiment logic when hand-assembling a JS payload. In normal usage this is called internally by the experiment-to-JS pipeline; invoke it directly only if you are constructing raw JS outside the standard `sweetbean_experiment_to_js` / `sweetbean_experiment_to_js_string` path.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "is_async": {\n      "description": "Whether to emit an async function declaration. Pass true when the experiment body contains await calls (e.g. async jsPsych plugins or fetch calls); false for a synchronous runExperiment().",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "is_async"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe returned string always includes `document.body.style.backgroundColor = \'black\';` as the first statement inside the function body — this is hardcoded and cannot be suppressed. The string ends with an open brace + two lines; you must append the function body and a closing `}` yourself. This is a low-level building block; prefer `sweetbean_experiment_to_js` or `sweetbean_experiment_to_js_string` for end-to-end JS generation.'
TOOL_PARAMETERS = { 'properties': { 'is_async': { 'description': 'Whether to emit an async function '
                                               'declaration. Pass true when the '
                                               'experiment body contains await calls '
                                               '(e.g. async jsPsych plugins or fetch '
                                               'calls); false for a synchronous '
                                               'runExperiment().',
                                'type': 'boolean'}},
  'required': ['is_async'],
  'type': 'object'}
TOOL_NOTES = "The returned string always includes `document.body.style.backgroundColor = 'black';` as the first statement inside the function body — this is hardcoded and cannot be suppressed. The string ends with an open brace + two lines; you must append the function body and a closing `}` yourself. This is a low-level building block; prefer `sweetbean_experiment_to_js` or `sweetbean_experiment_to_js_string` for end-to-end JS generation."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.FUNCTION_PREAMBLE
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
    def function_preamble(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need the raw JavaScript opening declaration string for a jsPsych `runExperiment()` function — either synchronous or async.'
        return _impl(args or {})
