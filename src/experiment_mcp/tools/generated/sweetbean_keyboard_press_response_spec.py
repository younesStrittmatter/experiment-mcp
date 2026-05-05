"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '447fde795098da828439f5e2277e169b945b6bf4409d479e86396152801b1907'
__exp_qualname__ = 'sweetbean.KeyboardPressResponseSpec'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_keyboard_press_response_spec'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the SweetBean pipeline, when defining how participants respond during a trial. Use it to create a keyboard-press response spec that you then pass to a SweetBean stimulus constructor (e.g. `sweetbean_text_stimulus` or similar). The result is a handle string pointing to a `KeyboardPressResponseSpec` object that encodes which keys are valid, which count as correct, and how many presses to capture before the trial ends.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "allowed_keys": {\n      "default": [],\n      "description": "Keys the participant may press (e.g. [\\"f\\", \\"j\\"]). Pass an empty list (the default) to accept any keypress, equivalent to jsPsych ALL_KEYS.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "correct_keys": {\n      "default": null,\n      "description": "Key(s) considered correct for feedback or scoring (e.g. [\\"f\\"]). Omit (null) if correctness is not evaluated for this response.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "max_responses": {\n      "default": 1,\n      "description": "Maximum keypresses to capture before the response phase closes. Default 1 captures a single response. Pass null to collect all responses that occur before the trial ends by other means.",\n      "oneOf": [\n        {\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "response_ends_trial": {\n      "default": true,\n      "description": "Whether a valid keypress immediately ends the trial. Defaults to true; set false when you want the trial to continue after a response (e.g. collect multiple presses or wait for a fixed duration).",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `allowed_keys` empty list == jsPsych ALL_KEYS (any key accepted); this is the default and is different from passing a non-empty list that happens to include every key.\n- `correct_keys` is for scoring/feedback only; it does not restrict which keys are accepted — use `allowed_keys` for that.\n- `max_responses` must be >= 1 or null; passing 0 raises a validation error.\n- `response_ends_trial` is marked `_PROMPT_SILENT` in the source, meaning SweetBean typically hides it from auto-generated prompts; it is still a valid, functional field.\n- `kind` is always `"keyboard_press"` and is set automatically — do not pass it.'
TOOL_PARAMETERS = { 'properties': { 'allowed_keys': { 'default': [],
                                    'description': 'Keys the participant may press '
                                                   '(e.g. ["f", "j"]). Pass an empty '
                                                   'list (the default) to accept any '
                                                   'keypress, equivalent to jsPsych '
                                                   'ALL_KEYS.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'correct_keys': { 'default': None,
                                    'description': 'Key(s) considered correct for '
                                                   'feedback or scoring (e.g. ["f"]). '
                                                   'Omit (null) if correctness is not '
                                                   'evaluated for this response.',
                                    'oneOf': [ { 'items': {'type': 'string'},
                                                 'type': 'array'},
                                               {'type': 'null'}]},
                  'max_responses': { 'default': 1,
                                     'description': 'Maximum keypresses to capture '
                                                    'before the response phase closes. '
                                                    'Default 1 captures a single '
                                                    'response. Pass null to collect '
                                                    'all responses that occur before '
                                                    'the trial ends by other means.',
                                     'oneOf': [ {'minimum': 1, 'type': 'integer'},
                                                {'type': 'null'}]},
                  'response_ends_trial': { 'default': True,
                                           'description': 'Whether a valid keypress '
                                                          'immediately ends the trial. '
                                                          'Defaults to true; set false '
                                                          'when you want the trial to '
                                                          'continue after a response '
                                                          '(e.g. collect multiple '
                                                          'presses or wait for a fixed '
                                                          'duration).',
                                           'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `allowed_keys` empty list == jsPsych ALL_KEYS (any key accepted); this is the default and is different from passing a non-empty list that happens to include every key.\n- `correct_keys` is for scoring/feedback only; it does not restrict which keys are accepted — use `allowed_keys` for that.\n- `max_responses` must be >= 1 or null; passing 0 raises a validation error.\n- `response_ends_trial` is marked `_PROMPT_SILENT` in the source, meaning SweetBean typically hides it from auto-generated prompts; it is still a valid, functional field.\n- `kind` is always `"keyboard_press"` and is set automatically — do not pass it.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.KeyboardPressResponseSpec
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
    def create_keyboard_press_response_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the SweetBean pipeline, when defining how participants respond during a trial.'
        return _impl(args or {})
