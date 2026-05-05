"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '6a2a99d679fd5f27982fdc60d0412d5d0869042df94d0a81e0efeacaed5ee7b4'
__exp_qualname__ = 'sweetbean.response_spec.SliderResponseSpec'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_slider_response_spec'
TOOL_DESCRIPTION = 'Call this tool in SweetBean pipeline step 3 — after SweetPea has produced a trial sequence — when you need a continuous or discrete slider rating as the participant response for a trial. Pass the returned spec object (as a handle string) to a SweetBean stimulus or trial constructor\'s `response` argument. The result is a `SliderResponseSpec` handle representing an HTML slider widget with configurable range, step, anchors, and optional correctness scoring.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "button_label": {\n      "default": "Continue",\n      "description": "Label on the submit button shown below the slider.",\n      "type": "string"\n    },\n    "correct_max_value": {\n      "description": "Inclusive upper bound of a correct range. Must be paired with correct_min_value, and >= correct_min_value.",\n      "nullable": true,\n      "type": "number"\n    },\n    "correct_min_value": {\n      "description": "Inclusive lower bound of a correct range. Must be paired with correct_max_value.",\n      "nullable": true,\n      "type": "number"\n    },\n    "correct_values": {\n      "description": "Exact slider values considered correct for feedback or scoring. Mutually exclusive with correct_min_value / correct_max_value.",\n      "items": {\n        "type": "number"\n      },\n      "nullable": true,\n      "type": "array"\n    },\n    "max_responses": {\n      "default": 1,\n      "description": "Maximum number of slider submissions to record. Pass null for unlimited (capture all submissions until the trial ends by other means). Must be >= 1 if an integer.",\n      "nullable": true,\n      "type": "integer"\n    },\n    "max_value": {\n      "default": 100,\n      "description": "Maximum (right-end) value of the slider. Must be strictly greater than min_value.",\n      "type": "number"\n    },\n    "min_value": {\n      "default": 0,\n      "description": "Minimum (left-end) value of the slider.",\n      "type": "number"\n    },\n    "require_movement": {\n      "default": false,\n      "description": "When true, the participant must drag the slider at least once before the submit button becomes active.",\n      "type": "boolean"\n    },\n    "response_ends_trial": {\n      "default": true,\n      "description": "Whether clicking the submit button ends the trial immediately.",\n      "type": "boolean"\n    },\n    "start_value": {\n      "description": "Initial thumb position. Must be within [min_value, max_value]. Omit to use the midpoint automatically.",\n      "nullable": true,\n      "type": "number"\n    },\n    "step": {\n      "description": "Snap-to step size. Null produces a fully continuous slider; a positive number adds discrete ticks at that interval.",\n      "nullable": true,\n      "type": "number"\n    },\n    "tick_labels": {\n      "default": [],\n      "description": "Optional text labels rendered along the slider track (e.g. [\'Not at all\', \'Extremely\'] for endpoint anchors).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `correct_min_value` and `correct_max_value` are all-or-nothing: provide both or neither; a mismatch raises a validation error at construction time.\n- `start_value` defaults to the midpoint of [min_value, max_value] when omitted — this can bias ratings in Likert-style designs; set it explicitly if that matters.\n- `tick_labels` are cosmetic only and do not constrain slider values; the number of labels need not match the number of steps.\n- `button_label`, `require_movement`, and `response_ends_trial` are marked silent in the SweetBean prompt schema — they are valid and honoured at runtime but are not surfaced in the jsPsych prompt description; change them only when the default behaviour is wrong for your design.\n- `max_responses` null (unlimited) is only meaningful when `response_ends_trial` is false; combining null with the default true is effectively the same as 1.'
TOOL_PARAMETERS = { 'properties': { 'button_label': { 'default': 'Continue',
                                    'description': 'Label on the submit button shown '
                                                   'below the slider.',
                                    'type': 'string'},
                  'correct_max_value': { 'description': 'Inclusive upper bound of a '
                                                        'correct range. Must be paired '
                                                        'with correct_min_value, and '
                                                        '>= correct_min_value.',
                                         'nullable': True,
                                         'type': 'number'},
                  'correct_min_value': { 'description': 'Inclusive lower bound of a '
                                                        'correct range. Must be paired '
                                                        'with correct_max_value.',
                                         'nullable': True,
                                         'type': 'number'},
                  'correct_values': { 'description': 'Exact slider values considered '
                                                     'correct for feedback or scoring. '
                                                     'Mutually exclusive with '
                                                     'correct_min_value / '
                                                     'correct_max_value.',
                                      'items': {'type': 'number'},
                                      'nullable': True,
                                      'type': 'array'},
                  'max_responses': { 'default': 1,
                                     'description': 'Maximum number of slider '
                                                    'submissions to record. Pass null '
                                                    'for unlimited (capture all '
                                                    'submissions until the trial ends '
                                                    'by other means). Must be >= 1 if '
                                                    'an integer.',
                                     'nullable': True,
                                     'type': 'integer'},
                  'max_value': { 'default': 100,
                                 'description': 'Maximum (right-end) value of the '
                                                'slider. Must be strictly greater than '
                                                'min_value.',
                                 'type': 'number'},
                  'min_value': { 'default': 0,
                                 'description': 'Minimum (left-end) value of the '
                                                'slider.',
                                 'type': 'number'},
                  'require_movement': { 'default': False,
                                        'description': 'When true, the participant '
                                                       'must drag the slider at least '
                                                       'once before the submit button '
                                                       'becomes active.',
                                        'type': 'boolean'},
                  'response_ends_trial': { 'default': True,
                                           'description': 'Whether clicking the submit '
                                                          'button ends the trial '
                                                          'immediately.',
                                           'type': 'boolean'},
                  'start_value': { 'description': 'Initial thumb position. Must be '
                                                  'within [min_value, max_value]. Omit '
                                                  'to use the midpoint automatically.',
                                   'nullable': True,
                                   'type': 'number'},
                  'step': { 'description': 'Snap-to step size. Null produces a fully '
                                           'continuous slider; a positive number adds '
                                           'discrete ticks at that interval.',
                            'nullable': True,
                            'type': 'number'},
                  'tick_labels': { 'default': [],
                                   'description': 'Optional text labels rendered along '
                                                  "the slider track (e.g. ['Not at "
                                                  "all', 'Extremely'] for endpoint "
                                                  'anchors).',
                                   'items': {'type': 'string'},
                                   'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `correct_min_value` and `correct_max_value` are all-or-nothing: provide both or neither; a mismatch raises a validation error at construction time.\n- `start_value` defaults to the midpoint of [min_value, max_value] when omitted — this can bias ratings in Likert-style designs; set it explicitly if that matters.\n- `tick_labels` are cosmetic only and do not constrain slider values; the number of labels need not match the number of steps.\n- `button_label`, `require_movement`, and `response_ends_trial` are marked silent in the SweetBean prompt schema — they are valid and honoured at runtime but are not surfaced in the jsPsych prompt description; change them only when the default behaviour is wrong for your design.\n- `max_responses` null (unlimited) is only meaningful when `response_ends_trial` is false; combining null with the default true is effectively the same as 1.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.SliderResponseSpec
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
    def create_slider_response_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in SweetBean pipeline step 3 — after SweetPea has produced a trial sequence — when you need a continuous or discrete slider rating as the participant response for a trial.'
        return _impl(args or {})
