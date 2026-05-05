"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'c9d8ac273781cf622e5618b3413b5ea5f6f555ca8611c63ad228b639f469e4f5'
__exp_qualname__ = 'sweetbean.stimulus.RandomObjectKinematogram'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_random_object_kinematogram'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the pipeline to define a Random Object Kinematogram (ROK) stimulus — a display of moving oriented objects used to measure perception of coherent motion direction or orientation. Pass the result (a handle string) into a SweetBean Trial or Block to build the experiment. Parameters like `coherent_movement_direction` and `coherence_movement` are the primary manipulation levers; bind them to SweetPea TimelineVariable handle strings when the values must vary trial-by-trial.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "aperture_position_left": {\n      "default": 50,\n      "description": "Horizontal midpoint of the aperture as a percentage of window width (0\\u2013100).",\n      "type": "number"\n    },\n    "aperture_position_top": {\n      "default": 50,\n      "description": "Vertical midpoint of the aperture as a percentage of window height (0\\u2013100).",\n      "type": "number"\n    },\n    "background_color": {\n      "default": "black",\n      "description": "CSS color string for the aperture background.",\n      "type": "string"\n    },\n    "choices": {\n      "default": [],\n      "description": "List of valid keyboard keys the participant may press to respond. Empty list means any key is accepted.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "coherence_movement": {\n      "default": 100,\n      "description": "Percentage (0\\u2013100) of objects moving in the coherent direction.",\n      "type": "number"\n    },\n    "coherence_orientation": {\n      "default": 100,\n      "description": "Percentage (0\\u2013100) of objects oriented in the coherent direction.",\n      "type": "number"\n    },\n    "coherent_movement_direction": {\n      "default": 180,\n      "description": "Direction of coherent motion in degrees; 0 = rightward, 180 = leftward. Can be a TimelineVariable handle string for trial-by-trial variation.",\n      "type": "number"\n    },\n    "coherent_orientation": {\n      "default": 180,\n      "description": "Orientation of the oriented objects in degrees; 0 = rightward. Can be a TimelineVariable handle string.",\n      "type": "number"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key that counts as a correct response; used to populate bean_correct in trial data.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Presentation duration in milliseconds (trial_duration). Omit for an indefinite display until a key is pressed.",\n      "type": "integer"\n    },\n    "movement_speed": {\n      "default": 10,\n      "description": "Speed of oob movement expressed as percentage of aperture width per second.",\n      "type": "number"\n    },\n    "number_of_apertures": {\n      "default": 1,\n      "description": "Number of kinematogram apertures to render simultaneously.",\n      "type": "integer"\n    },\n    "number_of_oobs": {\n      "default": 300,\n      "description": "Number of oriented objects (oobs) rendered per stimulus frame.",\n      "type": "integer"\n    },\n    "oob_color": {\n      "default": "white",\n      "description": "CSS color string for the oriented objects.",\n      "type": "string"\n    },\n    "side_effects": {\n      "additionalProperties": true,\n      "description": "Dictionary of side effects to apply after the stimulus; keys are variable names, values are expressions. Omit if no side effects are needed.",\n      "type": "object"\n    },\n    "stimulus_type": {\n      "default": 0,\n      "description": "Integer code selecting the shape of the oriented objects (e.g., 0 = lines). Consult jsPsychRok docs for valid codes.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- All angle parameters (`coherent_movement_direction`, `coherent_orientation`) use degrees where 0 = rightward; the defaults of 180 produce leftward motion/orientation.\n- `coherence_movement` and `coherence_orientation` are both percentages (0–100), not fractions; passing 1 instead of 100 means 1%, not 100%.\n- `movement_speed` is percentage-of-aperture-width per second, not pixels — perceived speed depends on aperture size.\n- `choices=None` in the Python constructor is converted to `[]` internally; pass an explicit list or omit the field.\n- `correct_key` is wrapped in a list internally (`correct_choice = [correct_key]`); pass the bare key string, not a list.\n- Trial data gets a `bean_correct` field mirroring jsPsych\'s `correct` field — use this rather than `correct` when reading results.\n- `process_l` (language model simulation) raises `NotImplementedError` — this stimulus cannot be used in headless LLM simulation mode.\n- Parameters that should vary by trial (e.g., `coherent_movement_direction`, `coherence_movement`) should be passed as SweetPea TimelineVariable handle strings, not hard-coded values.'
TOOL_PARAMETERS = { 'properties': { 'aperture_position_left': { 'default': 50,
                                              'description': 'Horizontal midpoint of '
                                                             'the aperture as a '
                                                             'percentage of window '
                                                             'width (0–100).',
                                              'type': 'number'},
                  'aperture_position_top': { 'default': 50,
                                             'description': 'Vertical midpoint of the '
                                                            'aperture as a percentage '
                                                            'of window height (0–100).',
                                             'type': 'number'},
                  'background_color': { 'default': 'black',
                                        'description': 'CSS color string for the '
                                                       'aperture background.',
                                        'type': 'string'},
                  'choices': { 'default': [],
                               'description': 'List of valid keyboard keys the '
                                              'participant may press to respond. Empty '
                                              'list means any key is accepted.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'coherence_movement': { 'default': 100,
                                          'description': 'Percentage (0–100) of '
                                                         'objects moving in the '
                                                         'coherent direction.',
                                          'type': 'number'},
                  'coherence_orientation': { 'default': 100,
                                             'description': 'Percentage (0–100) of '
                                                            'objects oriented in the '
                                                            'coherent direction.',
                                             'type': 'number'},
                  'coherent_movement_direction': { 'default': 180,
                                                   'description': 'Direction of '
                                                                  'coherent motion in '
                                                                  'degrees; 0 = '
                                                                  'rightward, 180 = '
                                                                  'leftward. Can be a '
                                                                  'TimelineVariable '
                                                                  'handle string for '
                                                                  'trial-by-trial '
                                                                  'variation.',
                                                   'type': 'number'},
                  'coherent_orientation': { 'default': 180,
                                            'description': 'Orientation of the '
                                                           'oriented objects in '
                                                           'degrees; 0 = rightward. '
                                                           'Can be a TimelineVariable '
                                                           'handle string.',
                                            'type': 'number'},
                  'correct_key': { 'default': '',
                                   'description': 'The key that counts as a correct '
                                                  'response; used to populate '
                                                  'bean_correct in trial data.',
                                   'type': 'string'},
                  'duration': { 'description': 'Presentation duration in milliseconds '
                                               '(trial_duration). Omit for an '
                                               'indefinite display until a key is '
                                               'pressed.',
                                'type': 'integer'},
                  'movement_speed': { 'default': 10,
                                      'description': 'Speed of oob movement expressed '
                                                     'as percentage of aperture width '
                                                     'per second.',
                                      'type': 'number'},
                  'number_of_apertures': { 'default': 1,
                                           'description': 'Number of kinematogram '
                                                          'apertures to render '
                                                          'simultaneously.',
                                           'type': 'integer'},
                  'number_of_oobs': { 'default': 300,
                                      'description': 'Number of oriented objects '
                                                     '(oobs) rendered per stimulus '
                                                     'frame.',
                                      'type': 'integer'},
                  'oob_color': { 'default': 'white',
                                 'description': 'CSS color string for the oriented '
                                                'objects.',
                                 'type': 'string'},
                  'side_effects': { 'additionalProperties': True,
                                    'description': 'Dictionary of side effects to '
                                                   'apply after the stimulus; keys are '
                                                   'variable names, values are '
                                                   'expressions. Omit if no side '
                                                   'effects are needed.',
                                    'type': 'object'},
                  'stimulus_type': { 'default': 0,
                                     'description': 'Integer code selecting the shape '
                                                    'of the oriented objects (e.g., 0 '
                                                    '= lines). Consult jsPsychRok docs '
                                                    'for valid codes.',
                                     'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "- All angle parameters (`coherent_movement_direction`, `coherent_orientation`) use degrees where 0 = rightward; the defaults of 180 produce leftward motion/orientation.\n- `coherence_movement` and `coherence_orientation` are both percentages (0–100), not fractions; passing 1 instead of 100 means 1%, not 100%.\n- `movement_speed` is percentage-of-aperture-width per second, not pixels — perceived speed depends on aperture size.\n- `choices=None` in the Python constructor is converted to `[]` internally; pass an explicit list or omit the field.\n- `correct_key` is wrapped in a list internally (`correct_choice = [correct_key]`); pass the bare key string, not a list.\n- Trial data gets a `bean_correct` field mirroring jsPsych's `correct` field — use this rather than `correct` when reading results.\n- `process_l` (language model simulation) raises `NotImplementedError` — this stimulus cannot be used in headless LLM simulation mode.\n- Parameters that should vary by trial (e.g., `coherent_movement_direction`, `coherence_movement`) should be passed as SweetPea TimelineVariable handle strings, not hard-coded values."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.RandomObjectKinematogram
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
    def create_random_object_kinematogram(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the pipeline to define a Random Object Kinematogram (ROK) stimulus — a display of moving oriented objects used to measure perception of coherent motion direction or orientation.'
        return _impl(args or {})
