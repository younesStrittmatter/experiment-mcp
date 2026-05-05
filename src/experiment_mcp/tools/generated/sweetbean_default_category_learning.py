"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '29fd063e32ee17b19d5c58b51bd8377bce7515a81499caa3936c65b93be4da5c'
__exp_qualname__ = 'sweetbean.stimulus.DefaultCategoryLearning'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_default_category_learning'
TOOL_DESCRIPTION = 'Call this tool in Step 3 of the SweetPea→SweetBean pipeline, after you have a SweetPea trial sequence whose trials include a binary feature vector (6-element list of 0/1 values). It creates a jsPsych HtmlKeyboardResponse stimulus that renders a geometric shape (circle/triangle, colored, sized, bordered, patterned, with optional inner mark) from that vector. The returned handle can be passed directly to a SweetBean Trial or Block constructor.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "choices": {\n      "description": "Keyboard keys the participant may press, e.g. [\\"f\\", \\"j\\"]. If omitted, any key is accepted.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key considered correct for accuracy scoring. Defaults to empty string (no correct-key tracking).",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Display duration in milliseconds. If omitted, the trial waits for a keypress response.",\n      "type": "number"\n    },\n    "feature_vector": {\n      "description": "Exactly 6 binary (0 or 1) integers encoding [shape, color, size, border, pattern, inner_mark] OR a handle string to a SweetBean TimelineVariable/Variable that resolves to such a list at runtime. Pass a handle when the vector varies per trial (typical SweetPea pipeline).",\n      "oneOf": [\n        {\n          "items": {\n            "enum": [\n              0,\n              1\n            ],\n            "type": "integer"\n          },\n          "maxItems": 6,\n          "minItems": 6,\n          "type": "array"\n        },\n        {\n          "description": "Handle string for a SweetBean Variable (e.g. TimelineVariable) produced by another tool.",\n          "type": "string"\n        }\n      ]\n    },\n    "prompt_template": {\n      "description": "Jinja2 template for the language-model prompt shown alongside the stimulus. May reference {{ feature_description }}. Defaults to \'You see a {{ feature_description }}.\'",\n      "type": "string"\n    },\n    "response_template": {\n      "description": "Jinja2 template for formatting the participant/LLM response. Optional; leave unset to use the class default.",\n      "type": "string"\n    },\n    "side_effects": {\n      "description": "Handle string to a list of SweetBean SideEffect objects to execute on each trial (e.g. feedback, data logging).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "feature_vector"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `feature_vector` is the only required argument; passing a 6-element list with any value outside {0, 1} raises ValueError at instantiation time. When the vector is a TimelineVariable (handle string), validation is deferred to runtime.\n- Feature index semantics: 0=shape (0 circle/1 triangle), 1=color (0 orange #E69F00/1 blue #0072B2), 2=size (0 small/1 large), 3=border (0 none/1 pink #CC79A7), 4=pattern (0 filled/1 striped), 5=inner_mark (0 none/1 star).\n- `correct_key` defaults to `""` (empty string), not `None`; leave it unset if you are not tracking accuracy.\n- The class internally generates two derived Variables (`default_category_learning_stimulus` and `default_category_learning_description`) — do not pass those names as kwargs, they will be overwritten.\n- When running headless / LLM simulation, `prompt_template` and `response_template` control what the language model sees; they have no effect in a standard browser jsPsych run.'
TOOL_PARAMETERS = { 'properties': { 'choices': { 'description': 'Keyboard keys the participant may '
                                              'press, e.g. ["f", "j"]. If omitted, any '
                                              'key is accepted.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'correct_key': { 'default': '',
                                   'description': 'The key considered correct for '
                                                  'accuracy scoring. Defaults to empty '
                                                  'string (no correct-key tracking).',
                                   'type': 'string'},
                  'duration': { 'description': 'Display duration in milliseconds. If '
                                               'omitted, the trial waits for a '
                                               'keypress response.',
                                'type': 'number'},
                  'feature_vector': { 'description': 'Exactly 6 binary (0 or 1) '
                                                     'integers encoding [shape, color, '
                                                     'size, border, pattern, '
                                                     'inner_mark] OR a handle string '
                                                     'to a SweetBean '
                                                     'TimelineVariable/Variable that '
                                                     'resolves to such a list at '
                                                     'runtime. Pass a handle when the '
                                                     'vector varies per trial (typical '
                                                     'SweetPea pipeline).',
                                      'oneOf': [ { 'items': { 'enum': [0, 1],
                                                              'type': 'integer'},
                                                   'maxItems': 6,
                                                   'minItems': 6,
                                                   'type': 'array'},
                                                 { 'description': 'Handle string for a '
                                                                  'SweetBean Variable '
                                                                  '(e.g. '
                                                                  'TimelineVariable) '
                                                                  'produced by another '
                                                                  'tool.',
                                                   'type': 'string'}]},
                  'prompt_template': { 'description': 'Jinja2 template for the '
                                                      'language-model prompt shown '
                                                      'alongside the stimulus. May '
                                                      'reference {{ '
                                                      'feature_description }}. '
                                                      "Defaults to 'You see a {{ "
                                                      "feature_description }}.'",
                                       'type': 'string'},
                  'response_template': { 'description': 'Jinja2 template for '
                                                        'formatting the '
                                                        'participant/LLM response. '
                                                        'Optional; leave unset to use '
                                                        'the class default.',
                                         'type': 'string'},
                  'side_effects': { 'description': 'Handle string to a list of '
                                                   'SweetBean SideEffect objects to '
                                                   'execute on each trial (e.g. '
                                                   'feedback, data logging).',
                                    'type': 'string'}},
  'required': ['feature_vector'],
  'type': 'object'}
TOOL_NOTES = '- `feature_vector` is the only required argument; passing a 6-element list with any value outside {0, 1} raises ValueError at instantiation time. When the vector is a TimelineVariable (handle string), validation is deferred to runtime.\n- Feature index semantics: 0=shape (0 circle/1 triangle), 1=color (0 orange #E69F00/1 blue #0072B2), 2=size (0 small/1 large), 3=border (0 none/1 pink #CC79A7), 4=pattern (0 filled/1 striped), 5=inner_mark (0 none/1 star).\n- `correct_key` defaults to `""` (empty string), not `None`; leave it unset if you are not tracking accuracy.\n- The class internally generates two derived Variables (`default_category_learning_stimulus` and `default_category_learning_description`) — do not pass those names as kwargs, they will be overwritten.\n- When running headless / LLM simulation, `prompt_template` and `response_template` control what the language model sees; they have no effect in a standard browser jsPsych run.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.DefaultCategoryLearning
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
    def create_default_category_learning(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in Step 3 of the SweetPea→SweetBean pipeline, after you have a SweetPea trial sequence whose trials include a binary feature vector (6-element list of 0/1 values).'
        return _impl(args or {})
