"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '314c01d078623afb29015a93852fd9da5020a4529c4f6478b3247d8d39234d13'
__exp_qualname__ = 'sweetbean.experiment.run_stimuli'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'run_stimuli'
TOOL_DESCRIPTION = 'Call this tool only when building a custom language-model simulation loop that needs fine-grained, per-stimulus control over a SweetBean block. In a normal workflow, prefer `sweetbean_experiment_run_on_language`, which orchestrates the full pipeline automatically. Use `run_stimuli` directly when you need to process a specific slice of stimuli (e.g. a single block at a time), carry accumulated state across calls, or inject a custom input handler. Returns a tuple of (out_data, prompts, shared_variables, datum_index) representing the updated simulation state after processing all stimuli in the list.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "data": {\n      "description": "Optional list of pre-recorded trial data rows to replay instead of calling get_input. Pass [] if running a fresh simulation.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "datum_index": {\n      "default": 0,\n      "description": "Index into `data` for the first stimulus in this pass. Pass 0 to start from the beginning; pass the returned datum_index to continue where a prior call left off.",\n      "type": "integer"\n    },\n    "get_input": {\n      "description": "Handle string for a registered callable that accepts a single prompt string and returns the LLM response string. Must be registered in the handle registry before this call.",\n      "type": "string"\n    },\n    "multi_turn": {\n      "description": "Whether to carry conversation history across stimuli in a single multi-turn context.",\n      "type": "boolean"\n    },\n    "out_data": {\n      "description": "Accumulated output data records from prior stimuli; pass [] when starting a fresh run.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "preamble": {\n      "description": "Optional text prepended to every prompt before invoking get_input. Pass an empty string to omit.",\n      "type": "string"\n    },\n    "prompts": {\n      "description": "Accumulated prompt history from prior turns. Pass [] to start fresh; pass the returned value to continue a multi-turn conversation.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "response_close_token": {\n      "description": "Token that marks the end of the expected response region in the LLM output.",\n      "type": "string"\n    },\n    "response_open_token": {\n      "description": "Token that marks the start of the expected response region in the LLM output (e.g. a delimiter or XML-like tag).",\n      "type": "string"\n    },\n    "shared_variables": {\n      "additionalProperties": true,\n      "description": "Mutable dict of shared variables carried across stimuli. Pass {} to start fresh; pass the returned value from a previous call to chain runs.",\n      "type": "object"\n    },\n    "stimuli": {\n      "description": "Ordered list of handle strings for SweetBean stimulus objects to process in this pass.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "timeline_element": {\n      "description": "Handle string for the current jsPsych timeline element that provides the trial context.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "stimuli",\n    "timeline_element",\n    "out_data",\n    "shared_variables",\n    "prompts",\n    "get_input",\n    "multi_turn",\n    "datum_index",\n    "data",\n    "preamble",\n    "response_open_token",\n    "response_close_token"\n  ],\n  "type": "object"\n}\n\nNotes:\n`get_input` cannot be an inline function — it must be a handle string pointing to a callable already registered in the handle registry (e.g. from a prior tool call that returned a callable handle). The function mutates `out_data` and `shared_variables` in place AND returns them; always use the returned values for subsequent calls rather than the inputs you passed in. `datum_index` is not reset automatically between calls; to chain multiple `run_stimuli` calls over a single `data` list, pass the returned `datum_index` as the `datum_index` argument of the next call. Side-effect resolution (shared variable propagation and `bean_*`-prefixed data extraction) happens inside this call — do not attempt to replay side effects manually after the fact.'
TOOL_PARAMETERS = { 'properties': { 'data': { 'description': 'Optional list of pre-recorded trial data '
                                           'rows to replay instead of calling '
                                           'get_input. Pass [] if running a fresh '
                                           'simulation.',
                            'items': {'type': 'object'},
                            'type': 'array'},
                  'datum_index': { 'default': 0,
                                   'description': 'Index into `data` for the first '
                                                  'stimulus in this pass. Pass 0 to '
                                                  'start from the beginning; pass the '
                                                  'returned datum_index to continue '
                                                  'where a prior call left off.',
                                   'type': 'integer'},
                  'get_input': { 'description': 'Handle string for a registered '
                                                'callable that accepts a single prompt '
                                                'string and returns the LLM response '
                                                'string. Must be registered in the '
                                                'handle registry before this call.',
                                 'type': 'string'},
                  'multi_turn': { 'description': 'Whether to carry conversation '
                                                 'history across stimuli in a single '
                                                 'multi-turn context.',
                                  'type': 'boolean'},
                  'out_data': { 'description': 'Accumulated output data records from '
                                               'prior stimuli; pass [] when starting a '
                                               'fresh run.',
                                'items': {'type': 'object'},
                                'type': 'array'},
                  'preamble': { 'description': 'Optional text prepended to every '
                                               'prompt before invoking get_input. Pass '
                                               'an empty string to omit.',
                                'type': 'string'},
                  'prompts': { 'description': 'Accumulated prompt history from prior '
                                              'turns. Pass [] to start fresh; pass the '
                                              'returned value to continue a multi-turn '
                                              'conversation.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'response_close_token': { 'description': 'Token that marks the end '
                                                           'of the expected response '
                                                           'region in the LLM output.',
                                            'type': 'string'},
                  'response_open_token': { 'description': 'Token that marks the start '
                                                          'of the expected response '
                                                          'region in the LLM output '
                                                          '(e.g. a delimiter or '
                                                          'XML-like tag).',
                                           'type': 'string'},
                  'shared_variables': { 'additionalProperties': True,
                                        'description': 'Mutable dict of shared '
                                                       'variables carried across '
                                                       'stimuli. Pass {} to start '
                                                       'fresh; pass the returned value '
                                                       'from a previous call to chain '
                                                       'runs.',
                                        'type': 'object'},
                  'stimuli': { 'description': 'Ordered list of handle strings for '
                                              'SweetBean stimulus objects to process '
                                              'in this pass.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'timeline_element': { 'description': 'Handle string for the current '
                                                       'jsPsych timeline element that '
                                                       'provides the trial context.',
                                        'type': 'string'}},
  'required': [ 'stimuli',
                'timeline_element',
                'out_data',
                'shared_variables',
                'prompts',
                'get_input',
                'multi_turn',
                'datum_index',
                'data',
                'preamble',
                'response_open_token',
                'response_close_token'],
  'type': 'object'}
TOOL_NOTES = '`get_input` cannot be an inline function — it must be a handle string pointing to a callable already registered in the handle registry (e.g. from a prior tool call that returned a callable handle). The function mutates `out_data` and `shared_variables` in place AND returns them; always use the returned values for subsequent calls rather than the inputs you passed in. `datum_index` is not reset automatically between calls; to chain multiple `run_stimuli` calls over a single `data` list, pass the returned `datum_index` as the `datum_index` argument of the next call. Side-effect resolution (shared variable propagation and `bean_*`-prefixed data extraction) happens inside this call — do not attempt to replay side effects manually after the fact.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.run_stimuli
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
    def run_stimuli(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when building a custom language-model simulation loop that needs fine-grained, per-stimulus control over a SweetBean block.'
        return _impl(args or {})
