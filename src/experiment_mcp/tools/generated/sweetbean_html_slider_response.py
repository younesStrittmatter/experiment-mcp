"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '60c968d3fa2762cfefff512d331997942b4736b12f0c34435a272fdc044edcbd'
__exp_qualname__ = 'sweetbean.stimulus.HtmlSliderResponse'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_html_slider_response'
TOOL_DESCRIPTION = 'Call this tool in the SweetBean stimulus-building step (after SweetPea has generated a trial sequence) to create a trial that presents HTML content and collects a continuous slider response via the jsPsych html-slider-response plugin. Use it whenever the experimental design requires a rating, estimation, or confidence judgment on a numeric scale. The tool returns a SweetBean stimulus handle that can be passed to a Block or Trial constructor.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "button_label": {\n      "default": "Continue",\n      "description": "Text shown on the submit button. Defaults to \'Continue\'.",\n      "type": "string"\n    },\n    "correct_max": {\n      "description": "Upper bound (inclusive) of correct response range. Must be paired with correct_min. Mutually exclusive with correct_values.",\n      "type": "number"\n    },\n    "correct_min": {\n      "description": "Lower bound (inclusive) of correct response range. Must be paired with correct_max. Mutually exclusive with correct_values.",\n      "type": "number"\n    },\n    "correct_values": {\n      "default": [],\n      "description": "Exact numeric values considered correct. Sets bean_correct in trial data. Mutually exclusive with correct_min/correct_max.",\n      "items": {\n        "type": "number"\n      },\n      "type": "array"\n    },\n    "duration": {\n      "description": "Maximum trial duration in milliseconds. Trial ends automatically when elapsed. Omit for no time limit.",\n      "type": "number"\n    },\n    "labels": {\n      "default": [],\n      "description": "Anchor labels distributed evenly along the slider (e.g. [\\"Not at all\\", \\"Extremely\\"]). Defaults to no labels.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "max": {\n      "default": 100,\n      "description": "Maximum value of the slider scale. Defaults to 100.0.",\n      "type": "number"\n    },\n    "min": {\n      "default": 0,\n      "description": "Minimum value of the slider scale. Defaults to 0.0.",\n      "type": "number"\n    },\n    "require_movement": {\n      "default": false,\n      "description": "If true, the participant must move the slider before the submit button becomes active. Useful to prevent defaulting to the start position. Defaults to false.",\n      "type": "boolean"\n    },\n    "response_ends_trial": {\n      "default": true,\n      "description": "If true, clicking the submit button ends the trial. Defaults to true.",\n      "type": "boolean"\n    },\n    "side_effects": {\n      "description": "List of handle strings referencing SweetBean CodeVariable or side-effect objects to execute alongside this stimulus.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "slider_start": {\n      "default": 50,\n      "description": "Initial position of the slider thumb when the trial begins. Defaults to 50.0.",\n      "type": "number"\n    },\n    "step": {\n      "description": "Granularity of slider movement. Null means the browser default (continuous). Provide an integer to discretize (e.g. 1 for whole-number steps).",\n      "type": "number"\n    },\n    "stimulus": {\n      "default": "",\n      "description": "HTML string displayed above the slider (e.g. a question, image tag, or formatted prompt). Defaults to empty string.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `bean_correct` in the recorded trial data is null when neither `correct_values` nor the `correct_min`/`correct_max` pair is supplied; if both are supplied, `correct_values` takes precedence (only one branch runs).\n- `slider_start` does NOT automatically center between `min` and `max` — it is always 50.0 regardless of scale. Pass an explicit value when using a non-0–100 range (e.g. slider_start=0 for a -50–50 scale).\n- The slider response is stored as a float in `bean_response`; `correct_values` comparison uses float equality, so avoid floating-point-imprecise targets.\n- `step` defaults to null (browser-continuous), not 1; passing step=1 makes the slider discrete.\n- `side_effects` items must be handle strings returned by prior CodeVariable or equivalent tool calls, not raw JavaScript strings.'
TOOL_PARAMETERS = { 'properties': { 'button_label': { 'default': 'Continue',
                                    'description': 'Text shown on the submit button. '
                                                   "Defaults to 'Continue'.",
                                    'type': 'string'},
                  'correct_max': { 'description': 'Upper bound (inclusive) of correct '
                                                  'response range. Must be paired with '
                                                  'correct_min. Mutually exclusive '
                                                  'with correct_values.',
                                   'type': 'number'},
                  'correct_min': { 'description': 'Lower bound (inclusive) of correct '
                                                  'response range. Must be paired with '
                                                  'correct_max. Mutually exclusive '
                                                  'with correct_values.',
                                   'type': 'number'},
                  'correct_values': { 'default': [],
                                      'description': 'Exact numeric values considered '
                                                     'correct. Sets bean_correct in '
                                                     'trial data. Mutually exclusive '
                                                     'with correct_min/correct_max.',
                                      'items': {'type': 'number'},
                                      'type': 'array'},
                  'duration': { 'description': 'Maximum trial duration in '
                                               'milliseconds. Trial ends automatically '
                                               'when elapsed. Omit for no time limit.',
                                'type': 'number'},
                  'labels': { 'default': [],
                              'description': 'Anchor labels distributed evenly along '
                                             'the slider (e.g. ["Not at all", '
                                             '"Extremely"]). Defaults to no labels.',
                              'items': {'type': 'string'},
                              'type': 'array'},
                  'max': { 'default': 100,
                           'description': 'Maximum value of the slider scale. Defaults '
                                          'to 100.0.',
                           'type': 'number'},
                  'min': { 'default': 0,
                           'description': 'Minimum value of the slider scale. Defaults '
                                          'to 0.0.',
                           'type': 'number'},
                  'require_movement': { 'default': False,
                                        'description': 'If true, the participant must '
                                                       'move the slider before the '
                                                       'submit button becomes active. '
                                                       'Useful to prevent defaulting '
                                                       'to the start position. '
                                                       'Defaults to false.',
                                        'type': 'boolean'},
                  'response_ends_trial': { 'default': True,
                                           'description': 'If true, clicking the '
                                                          'submit button ends the '
                                                          'trial. Defaults to true.',
                                           'type': 'boolean'},
                  'side_effects': { 'description': 'List of handle strings referencing '
                                                   'SweetBean CodeVariable or '
                                                   'side-effect objects to execute '
                                                   'alongside this stimulus.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'slider_start': { 'default': 50,
                                    'description': 'Initial position of the slider '
                                                   'thumb when the trial begins. '
                                                   'Defaults to 50.0.',
                                    'type': 'number'},
                  'step': { 'description': 'Granularity of slider movement. Null means '
                                           'the browser default (continuous). Provide '
                                           'an integer to discretize (e.g. 1 for '
                                           'whole-number steps).',
                            'type': 'number'},
                  'stimulus': { 'default': '',
                                'description': 'HTML string displayed above the slider '
                                               '(e.g. a question, image tag, or '
                                               'formatted prompt). Defaults to empty '
                                               'string.',
                                'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `bean_correct` in the recorded trial data is null when neither `correct_values` nor the `correct_min`/`correct_max` pair is supplied; if both are supplied, `correct_values` takes precedence (only one branch runs).\n- `slider_start` does NOT automatically center between `min` and `max` — it is always 50.0 regardless of scale. Pass an explicit value when using a non-0–100 range (e.g. slider_start=0 for a -50–50 scale).\n- The slider response is stored as a float in `bean_response`; `correct_values` comparison uses float equality, so avoid floating-point-imprecise targets.\n- `step` defaults to null (browser-continuous), not 1; passing step=1 makes the slider discrete.\n- `side_effects` items must be handle strings returned by prior CodeVariable or equivalent tool calls, not raw JavaScript strings.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.HtmlSliderResponse
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
    def create_html_slider_response(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in the SweetBean stimulus-building step (after SweetPea has generated a trial sequence) to create a trial that presents HTML content and collects a continuous slider response via the jsPsych html-slider-response plugin.'
        return _impl(args or {})
