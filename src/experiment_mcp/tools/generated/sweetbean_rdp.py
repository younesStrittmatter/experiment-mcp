"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '7d6f757685be13a1af76fcd619eff756133c3fb78a9b5102f6c3b41881205ca9'
__exp_qualname__ = 'sweetbean.stimulus.RDP'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_rdp'
TOOL_DESCRIPTION = 'Call this tool in the SweetBean stimulus-construction step (step 3 of the pipeline) when the experimental design requires a random-dot/object kinematogram that varies orientation coherence — for example, after SweetPea has generated trial sequences with `coherent_orientation` or `coherence_orientation` as factorial levels. Instantiates a `sweetbean.stimulus.RDP` (RandomDotPatterns) stimulus whose handle can be passed to a SweetBean `Trial`. Movement parameters are fixed to zero; use the parent `ROK` tool directly if you need motion coherence as well.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "aperture_position_left": {\n      "default": 50,\n      "description": "Horizontal midpoint of the aperture as a percentage of window width.",\n      "type": "number"\n    },\n    "aperture_position_top": {\n      "default": 50,\n      "description": "Vertical midpoint of the aperture as a percentage of window height.",\n      "type": "number"\n    },\n    "background_color": {\n      "default": "grey",\n      "description": "CSS color string for the aperture background.",\n      "type": "string"\n    },\n    "choices": {\n      "default": [],\n      "description": "List of valid keyboard keys the participant may press to respond. Empty list means all keys are accepted.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "coherence_orientation": {\n      "default": 0,\n      "description": "Percentage (0\\u2013100) of objects moving in the coherent orientation direction.",\n      "type": "number"\n    },\n    "coherent_orientation": {\n      "default": 0,\n      "description": "Orientation angle of the coherently-moving objects in degrees; 0 means pointing right.",\n      "type": "number"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key that constitutes a correct response. Leave as empty string if correctness is not tracked.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Time in milliseconds the stimulus is displayed. Pass null to display until a valid key is pressed.",\n      "type": "number"\n    },\n    "number_of_apertures": {\n      "default": 2,\n      "description": "Number of kinematogram apertures rendered on screen.",\n      "type": "integer"\n    },\n    "number_of_oobs": {\n      "default": 300,\n      "description": "Number of oriented objects per aperture set.",\n      "type": "integer"\n    },\n    "oob_color": {\n      "default": "white",\n      "description": "CSS color string for the oriented objects.",\n      "type": "string"\n    },\n    "side_effects": {\n      "description": "List of SideEffect handle strings (produced by SweetBean SideEffect tools) to attach to this stimulus for updating global data such as score or trial counter. Omit if no side effects are needed.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "stimulus_type": {\n      "default": 1,\n      "description": "Integer code selecting the shape of the oriented objects (jsPsych-ROK stimulus_type field).",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMovement is disabled: `coherent_movement_direction`, `coherence_movement`, and `movement_speed` are all hardcoded to 0 and cannot be set via this tool — this is the orientation-only RDP variant. If you need a kinematogram with motion coherence, use the `ROK` tool instead. `coherence_orientation` is a percentage (0–100), not a 0–1 fraction. `coherent_orientation` is in degrees with 0 meaning rightward. Both position parameters are percentages of the viewport dimensions, not pixel offsets. `side_effects` items should be handle strings returned by SideEffect constructor tools, not raw dicts.'
TOOL_PARAMETERS = { 'properties': { 'aperture_position_left': { 'default': 50,
                                              'description': 'Horizontal midpoint of '
                                                             'the aperture as a '
                                                             'percentage of window '
                                                             'width.',
                                              'type': 'number'},
                  'aperture_position_top': { 'default': 50,
                                             'description': 'Vertical midpoint of the '
                                                            'aperture as a percentage '
                                                            'of window height.',
                                             'type': 'number'},
                  'background_color': { 'default': 'grey',
                                        'description': 'CSS color string for the '
                                                       'aperture background.',
                                        'type': 'string'},
                  'choices': { 'default': [],
                               'description': 'List of valid keyboard keys the '
                                              'participant may press to respond. Empty '
                                              'list means all keys are accepted.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'coherence_orientation': { 'default': 0,
                                             'description': 'Percentage (0–100) of '
                                                            'objects moving in the '
                                                            'coherent orientation '
                                                            'direction.',
                                             'type': 'number'},
                  'coherent_orientation': { 'default': 0,
                                            'description': 'Orientation angle of the '
                                                           'coherently-moving objects '
                                                           'in degrees; 0 means '
                                                           'pointing right.',
                                            'type': 'number'},
                  'correct_key': { 'default': '',
                                   'description': 'The key that constitutes a correct '
                                                  'response. Leave as empty string if '
                                                  'correctness is not tracked.',
                                   'type': 'string'},
                  'duration': { 'description': 'Time in milliseconds the stimulus is '
                                               'displayed. Pass null to display until '
                                               'a valid key is pressed.',
                                'type': 'number'},
                  'number_of_apertures': { 'default': 2,
                                           'description': 'Number of kinematogram '
                                                          'apertures rendered on '
                                                          'screen.',
                                           'type': 'integer'},
                  'number_of_oobs': { 'default': 300,
                                      'description': 'Number of oriented objects per '
                                                     'aperture set.',
                                      'type': 'integer'},
                  'oob_color': { 'default': 'white',
                                 'description': 'CSS color string for the oriented '
                                                'objects.',
                                 'type': 'string'},
                  'side_effects': { 'description': 'List of SideEffect handle strings '
                                                   '(produced by SweetBean SideEffect '
                                                   'tools) to attach to this stimulus '
                                                   'for updating global data such as '
                                                   'score or trial counter. Omit if no '
                                                   'side effects are needed.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'stimulus_type': { 'default': 1,
                                     'description': 'Integer code selecting the shape '
                                                    'of the oriented objects '
                                                    '(jsPsych-ROK stimulus_type '
                                                    'field).',
                                     'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Movement is disabled: `coherent_movement_direction`, `coherence_movement`, and `movement_speed` are all hardcoded to 0 and cannot be set via this tool — this is the orientation-only RDP variant. If you need a kinematogram with motion coherence, use the `ROK` tool instead. `coherence_orientation` is a percentage (0–100), not a 0–1 fraction. `coherent_orientation` is in degrees with 0 meaning rightward. Both position parameters are percentages of the viewport dimensions, not pixel offsets. `side_effects` items should be handle strings returned by SideEffect constructor tools, not raw dicts.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.RDP
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
    def create_rdp(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in the SweetBean stimulus-construction step (step 3 of the pipeline) when the experimental design requires a random-dot/object kinematogram that varies orientation coherence — for example, after SweetPea has generated trial sequences with `coherent_orientation` or `coherence_orientation` as factorial levels.'
        return _impl(args or {})
