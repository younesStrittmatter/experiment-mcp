"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'c9d8ac273781cf622e5618b3413b5ea5f6f555ca8611c63ad228b639f469e4f5'
__exp_qualname__ = 'sweetbean.stimulus.ROK'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_rok'
TOOL_DESCRIPTION = 'Call this tool at SweetBean stimulus-definition time (step 3 of the pipeline) to create a Random Object Kinematogram (ROK) stimulus — a display of oriented objects where a controllable fraction move or are oriented coherently. Use it when your design (from SweetPea) includes factors for motion coherence, direction, or orientation and you need a jsPsych ROK trial. Returns a SweetBean stimulus handle that can be composed into a Trial and then a Block.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "aperture_position_left": {\n      "default": 50,\n      "description": "Horizontal midpoint of the aperture as a percentage of window width. Default 50 (centered).",\n      "type": "number"\n    },\n    "aperture_position_top": {\n      "default": 50,\n      "description": "Vertical midpoint of the aperture as a percentage of window height. Default 50 (centered).",\n      "type": "number"\n    },\n    "background_color": {\n      "default": "black",\n      "description": "CSS color string for the background. Default \'black\'.",\n      "type": "string"\n    },\n    "choices": {\n      "default": [],\n      "description": "List of valid key names the participant may press to respond (e.g. [\'ArrowLeft\', \'ArrowRight\']). Default [] (no keys accepted).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "coherence_movement": {\n      "default": 100,\n      "description": "Percentage of objects moving in the coherent direction (0\\u2013100). Default 100.",\n      "type": "number"\n    },\n    "coherence_orientation": {\n      "default": 100,\n      "description": "Percentage of objects oriented coherently (0\\u2013100). Default 100.",\n      "type": "number"\n    },\n    "coherent_movement_direction": {\n      "default": 180,\n      "description": "Direction of coherent motion in degrees; 0 = rightward. Default 180 (leftward).",\n      "type": "number"\n    },\n    "coherent_orientation": {\n      "default": 180,\n      "description": "Orientation of objects in degrees; 0 = rightward. Default 180.",\n      "type": "number"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key name that counts as a correct response; used to set bean_correct in trial data. Default \'\' (no correct key defined).",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Stimulus presentation time in milliseconds (trial_duration). Omit for indefinite display until a key is pressed.",\n      "type": "integer"\n    },\n    "movement_speed": {\n      "default": 10,\n      "description": "Speed of objects as a percentage of aperture width per second. Default 10.",\n      "type": "number"\n    },\n    "number_of_apertures": {\n      "default": 1,\n      "description": "Number of independent kinematogram apertures shown simultaneously. Default 1.",\n      "type": "integer"\n    },\n    "number_of_oobs": {\n      "default": 300,\n      "description": "Number of oriented objects (oobs) per aperture set. Default 300.",\n      "type": "integer"\n    },\n    "oob_color": {\n      "default": "white",\n      "description": "CSS color string for the oriented objects. Default \'white\'.",\n      "type": "string"\n    },\n    "side_effects": {\n      "additionalProperties": true,\n      "description": "Optional dictionary of side effects that update trial-level data variables after the stimulus.",\n      "type": "object"\n    },\n    "stimulus_type": {\n      "default": 0,\n      "description": "Integer code selecting the object shape/type rendered by jsPsychRok. Default 0.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\ncoherent_movement_direction and coherent_orientation are independent axes: you can set objects to all face right (coherent_orientation=0) while moving left (coherent_movement_direction=180). Both default to 180, so the default ROK is fully left-moving and left-oriented. movement_speed is in units of (aperture_width %)/second, not pixels/second — values above ~30 look unrealistically fast. The jsPsych plugin name is \'jsPsychRok\'; make sure the jsPsych build includes that plugin when exporting to HTML. process_l (language-model mode) raises NotImplementedError, so this stimulus cannot be used in headless LLM simulation runs.'
TOOL_PARAMETERS = { 'properties': { 'aperture_position_left': { 'default': 50,
                                              'description': 'Horizontal midpoint of '
                                                             'the aperture as a '
                                                             'percentage of window '
                                                             'width. Default 50 '
                                                             '(centered).',
                                              'type': 'number'},
                  'aperture_position_top': { 'default': 50,
                                             'description': 'Vertical midpoint of the '
                                                            'aperture as a percentage '
                                                            'of window height. Default '
                                                            '50 (centered).',
                                             'type': 'number'},
                  'background_color': { 'default': 'black',
                                        'description': 'CSS color string for the '
                                                       "background. Default 'black'.",
                                        'type': 'string'},
                  'choices': { 'default': [],
                               'description': 'List of valid key names the participant '
                                              'may press to respond (e.g. '
                                              "['ArrowLeft', 'ArrowRight']). Default "
                                              '[] (no keys accepted).',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'coherence_movement': { 'default': 100,
                                          'description': 'Percentage of objects moving '
                                                         'in the coherent direction '
                                                         '(0–100). Default 100.',
                                          'type': 'number'},
                  'coherence_orientation': { 'default': 100,
                                             'description': 'Percentage of objects '
                                                            'oriented coherently '
                                                            '(0–100). Default 100.',
                                             'type': 'number'},
                  'coherent_movement_direction': { 'default': 180,
                                                   'description': 'Direction of '
                                                                  'coherent motion in '
                                                                  'degrees; 0 = '
                                                                  'rightward. Default '
                                                                  '180 (leftward).',
                                                   'type': 'number'},
                  'coherent_orientation': { 'default': 180,
                                            'description': 'Orientation of objects in '
                                                           'degrees; 0 = rightward. '
                                                           'Default 180.',
                                            'type': 'number'},
                  'correct_key': { 'default': '',
                                   'description': 'The key name that counts as a '
                                                  'correct response; used to set '
                                                  'bean_correct in trial data. Default '
                                                  "'' (no correct key defined).",
                                   'type': 'string'},
                  'duration': { 'description': 'Stimulus presentation time in '
                                               'milliseconds (trial_duration). Omit '
                                               'for indefinite display until a key is '
                                               'pressed.',
                                'type': 'integer'},
                  'movement_speed': { 'default': 10,
                                      'description': 'Speed of objects as a percentage '
                                                     'of aperture width per second. '
                                                     'Default 10.',
                                      'type': 'number'},
                  'number_of_apertures': { 'default': 1,
                                           'description': 'Number of independent '
                                                          'kinematogram apertures '
                                                          'shown simultaneously. '
                                                          'Default 1.',
                                           'type': 'integer'},
                  'number_of_oobs': { 'default': 300,
                                      'description': 'Number of oriented objects '
                                                     '(oobs) per aperture set. Default '
                                                     '300.',
                                      'type': 'integer'},
                  'oob_color': { 'default': 'white',
                                 'description': 'CSS color string for the oriented '
                                                "objects. Default 'white'.",
                                 'type': 'string'},
                  'side_effects': { 'additionalProperties': True,
                                    'description': 'Optional dictionary of side '
                                                   'effects that update trial-level '
                                                   'data variables after the stimulus.',
                                    'type': 'object'},
                  'stimulus_type': { 'default': 0,
                                     'description': 'Integer code selecting the object '
                                                    'shape/type rendered by '
                                                    'jsPsychRok. Default 0.',
                                     'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "coherent_movement_direction and coherent_orientation are independent axes: you can set objects to all face right (coherent_orientation=0) while moving left (coherent_movement_direction=180). Both default to 180, so the default ROK is fully left-moving and left-oriented. movement_speed is in units of (aperture_width %)/second, not pixels/second — values above ~30 look unrealistically fast. The jsPsych plugin name is 'jsPsychRok'; make sure the jsPsych build includes that plugin when exporting to HTML. process_l (language-model mode) raises NotImplementedError, so this stimulus cannot be used in headless LLM simulation runs."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.ROK
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
    def create_rok(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at SweetBean stimulus-definition time (step 3 of the pipeline) to create a Random Object Kinematogram (ROK) stimulus — a display of oriented objects where a controllable fraction move or are oriented coherently.'
        return _impl(args or {})
