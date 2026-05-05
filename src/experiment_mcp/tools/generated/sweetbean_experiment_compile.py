"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '5875019218bf73c4e20eb1e410dec937fbc388c7aa6ff7060e09903c32b06bcb'
__exp_qualname__ = 'sweetbean.Experiment.compile'
__exp_kind__ = 'method'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'compile'
TOOL_DESCRIPTION = 'Call this tool after constructing a SweetBean `Experiment` (step 4 of the SweetPea→SweetBean pipeline) when you need a reusable JavaScript template: it renders stimulus graphs and jsPsych setup once, leaving each block\'s `timeline_variables` as a placeholder string. Pass the resulting JS template to `sweetbean_experiment_to_js_string_from_template` to inject per-condition trial data without re-running Transcrypt — ideal for multi-condition deployments (e.g. Firebase). Returns the compiled JavaScript as a plain string.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "as_function": {\n      "default": true,\n      "description": "When true (default), wraps the emitted JavaScript in a function declaration. Set to false to emit a flat script suitable for direct <script> injection.",\n      "type": "boolean"\n    },\n    "experiment": {\n      "description": "Handle string returned by the sweetbean_experiment constructor tool, identifying the live Experiment instance whose blocks and stimuli will be compiled.",\n      "type": "string"\n    },\n    "is_async": {\n      "default": true,\n      "description": "When true (default), the emitted JS function is declared async. Only meaningful when as_function is also true.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "experiment"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis method produces a TEMPLATE, not a finished experiment: each block\'s timeline_variables is replaced with a placeholder token. You MUST call sweetbean_experiment_to_js_string_from_template afterward to inject the actual per-condition trial sequences before the JS is runnable. Blocks whose timeline is a CodeVariable are rendered inline (no placeholder). The is_async flag has no effect when as_function=false. Protections registered on the Experiment are active during compilation and reset to [] in a finally block — do not rely on protection state being preserved after this call.'
TOOL_PARAMETERS = { 'properties': { 'as_function': { 'default': True,
                                   'description': 'When true (default), wraps the '
                                                  'emitted JavaScript in a function '
                                                  'declaration. Set to false to emit a '
                                                  'flat script suitable for direct '
                                                  '<script> injection.',
                                   'type': 'boolean'},
                  'experiment': { 'description': 'Handle string returned by the '
                                                 'sweetbean_experiment constructor '
                                                 'tool, identifying the live '
                                                 'Experiment instance whose blocks and '
                                                 'stimuli will be compiled.',
                                  'type': 'string'},
                  'is_async': { 'default': True,
                                'description': 'When true (default), the emitted JS '
                                               'function is declared async. Only '
                                               'meaningful when as_function is also '
                                               'true.',
                                'type': 'boolean'}},
  'required': ['experiment'],
  'type': 'object'}
TOOL_NOTES = "This method produces a TEMPLATE, not a finished experiment: each block's timeline_variables is replaced with a placeholder token. You MUST call sweetbean_experiment_to_js_string_from_template afterward to inject the actual per-condition trial sequences before the JS is runnable. Blocks whose timeline is a CodeVariable are rendered inline (no placeholder). The is_async flag has no effect when as_function=false. Protections registered on the Experiment are active during compilation and reset to [] in a finally block — do not rely on protection state being preserved after this call."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = sb.Experiment
    resolved = handles.resolve_in(kwargs)
    instance = resolved.pop('experiment', None)
    if instance is None:
        raise TypeError(
            f"{TOOL_NAME} requires kwarg 'experiment' "
            f"(handle returned by create_experiment)."
        )
    if not isinstance(instance, cls):
        raise TypeError(
            f"{TOOL_NAME} got 'experiment'={type(instance).__name__}, "
            f"expected Experiment."
        )
    result = instance.compile(**resolved)
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
    def compile(args: dict[str, Any] | None = None) -> Any:
        "Call this tool after constructing a SweetBean `Experiment` (step 4 of the SweetPea→SweetBean pipeline) when you need a reusable JavaScript template: it renders stimulus graphs and jsPsych setup once, leaving each block's `timeline_variables` as a placeholder string."
        return _impl(args or {})
