"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '7d6f757685be13a1af76fcd619eff756133c3fb78a9b5102f6c3b41881205ca9'
__exp_qualname__ = 'sweetbean.stimulus.RandomDotPatterns'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_random_dot_patterns'
TOOL_DESCRIPTION = 'Call this tool at SweetBean stimulus-definition time (step 3 of the pipeline) to create a Random Dot Patterns (orientation-only kinematogram) stimulus. Use it when your experimental design requires participants to judge the coherent orientation of oriented objects — not motion direction. Returns a SweetBean `RandomDotPatterns` stimulus object (handle string) that can be passed into a `Trial` or `Block` tool.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "aperture_position_left": {\n      "default": 50,\n      "description": "Horizontal position of the aperture midpoint as a percentage of window width (0\\u2013100).",\n      "type": "number"\n    },\n    "aperture_position_top": {\n      "default": 50,\n      "description": "Vertical position of the aperture midpoint as a percentage of window height (0\\u2013100).",\n      "type": "number"\n    },\n    "background_color": {\n      "default": "grey",\n      "description": "CSS color string for the aperture background.",\n      "type": "string"\n    },\n    "choices": {\n      "default": [],\n      "description": "Valid keyboard keys the participant may press to indicate a response (e.g. [\\"ArrowLeft\\", \\"ArrowRight\\"]).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "coherence_orientation": {\n      "default": 0,\n      "description": "Percentage (0\\u2013100) of objects that are oriented in the coherent direction. The remainder are randomly oriented.",\n      "type": "number"\n    },\n    "coherent_orientation": {\n      "default": 0,\n      "description": "Orientation angle of the coherently oriented objects in degrees. 0 = pointing right, increases counter-clockwise.",\n      "type": "number"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key that constitutes a correct response. Used for accuracy feedback and scoring.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Presentation time in milliseconds. If omitted, the trial waits for a key response.",\n      "type": "integer"\n    },\n    "number_of_apertures": {\n      "default": 2,\n      "description": "Number of independent kinematogram apertures shown simultaneously.",\n      "type": "integer"\n    },\n    "number_of_oobs": {\n      "default": 300,\n      "description": "Number of oriented objects (oobs) rendered per aperture set.",\n      "type": "integer"\n    },\n    "oob_color": {\n      "default": "white",\n      "description": "CSS color string for the oriented objects.",\n      "type": "string"\n    },\n    "side_effects": {\n      "description": "List of SideEffect handle strings (produced by SideEffect tools) to attach to this stimulus. Used to update global state such as score or trial counter on response.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "stimulus_type": {\n      "default": 1,\n      "description": "Integer code selecting the shape/type of the oriented objects (see SweetBean ROK docs).",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis stimulus is orientation-only: all motion parameters (`coherent_movement_direction`, `coherence_movement`, `movement_speed`) are hardcoded to 0 and cannot be overridden — use the parent `ROK` tool if you need motion coherence. `coherence_orientation` is a percentage (0–100), not a 0–1 fraction; passing 0.5 will give near-zero coherence, not 50%. `coherent_orientation` of 0 means objects point right; angles increase counter-clockwise. When `duration` is `None` and `choices` is empty, the trial advances immediately with no response window — always set at least one of these for response-collection paradigms.'
TOOL_PARAMETERS = { 'properties': { 'aperture_position_left': { 'default': 50,
                                              'description': 'Horizontal position of '
                                                             'the aperture midpoint as '
                                                             'a percentage of window '
                                                             'width (0–100).',
                                              'type': 'number'},
                  'aperture_position_top': { 'default': 50,
                                             'description': 'Vertical position of the '
                                                            'aperture midpoint as a '
                                                            'percentage of window '
                                                            'height (0–100).',
                                             'type': 'number'},
                  'background_color': { 'default': 'grey',
                                        'description': 'CSS color string for the '
                                                       'aperture background.',
                                        'type': 'string'},
                  'choices': { 'default': [],
                               'description': 'Valid keyboard keys the participant may '
                                              'press to indicate a response (e.g. '
                                              '["ArrowLeft", "ArrowRight"]).',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'coherence_orientation': { 'default': 0,
                                             'description': 'Percentage (0–100) of '
                                                            'objects that are oriented '
                                                            'in the coherent '
                                                            'direction. The remainder '
                                                            'are randomly oriented.',
                                             'type': 'number'},
                  'coherent_orientation': { 'default': 0,
                                            'description': 'Orientation angle of the '
                                                           'coherently oriented '
                                                           'objects in degrees. 0 = '
                                                           'pointing right, increases '
                                                           'counter-clockwise.',
                                            'type': 'number'},
                  'correct_key': { 'default': '',
                                   'description': 'The key that constitutes a correct '
                                                  'response. Used for accuracy '
                                                  'feedback and scoring.',
                                   'type': 'string'},
                  'duration': { 'description': 'Presentation time in milliseconds. If '
                                               'omitted, the trial waits for a key '
                                               'response.',
                                'type': 'integer'},
                  'number_of_apertures': { 'default': 2,
                                           'description': 'Number of independent '
                                                          'kinematogram apertures '
                                                          'shown simultaneously.',
                                           'type': 'integer'},
                  'number_of_oobs': { 'default': 300,
                                      'description': 'Number of oriented objects '
                                                     '(oobs) rendered per aperture '
                                                     'set.',
                                      'type': 'integer'},
                  'oob_color': { 'default': 'white',
                                 'description': 'CSS color string for the oriented '
                                                'objects.',
                                 'type': 'string'},
                  'side_effects': { 'description': 'List of SideEffect handle strings '
                                                   '(produced by SideEffect tools) to '
                                                   'attach to this stimulus. Used to '
                                                   'update global state such as score '
                                                   'or trial counter on response.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'stimulus_type': { 'default': 1,
                                     'description': 'Integer code selecting the '
                                                    'shape/type of the oriented '
                                                    'objects (see SweetBean ROK docs).',
                                     'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'This stimulus is orientation-only: all motion parameters (`coherent_movement_direction`, `coherence_movement`, `movement_speed`) are hardcoded to 0 and cannot be overridden — use the parent `ROK` tool if you need motion coherence. `coherence_orientation` is a percentage (0–100), not a 0–1 fraction; passing 0.5 will give near-zero coherence, not 50%. `coherent_orientation` of 0 means objects point right; angles increase counter-clockwise. When `duration` is `None` and `choices` is empty, the trial advances immediately with no response window — always set at least one of these for response-collection paradigms.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.RandomDotPatterns
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
    def create_random_dot_patterns(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at SweetBean stimulus-definition time (step 3 of the pipeline) to create a Random Dot Patterns (orientation-only kinematogram) stimulus.'
        return _impl(args or {})
