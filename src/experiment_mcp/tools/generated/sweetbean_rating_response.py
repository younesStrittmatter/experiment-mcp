"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'ef66b2ceb86e5601730202aafd74d3673e63a5d4a09d6e51093dc1b602d96018'
__exp_qualname__ = 'sweetbean.stimulus.RatingResponse'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_rating_response'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the pipeline — after SweetPea has sampled a trial sequence — to add a discrete N-point rating widget or a static filled-pip display to a SweetBean trial. Pass `value=null` (default) for response mode, where the participant presses digit keys and `bean_response` is written to jsPsych data; pass an integer or a sweetbean Variable handle for display mode, which renders a pre-filled scale and auto-advances. Returns a handle string referencing the constructed `RatingResponse` object for use in a SweetBean `Trial`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "duration": {\n      "description": "Trial duration in milliseconds. In display mode, omitting this defaults to 1500 ms (auto-advance). In response mode, omitting this means no timeout \\u2014 the trial waits for a keypress.",\n      "minimum": 0,\n      "type": "integer"\n    },\n    "label": {\n      "description": "Optional text caption rendered above the pip row.",\n      "type": "string"\n    },\n    "n_points": {\n      "default": 5,\n      "description": "Number of discrete rating points on the scale. Must be 2\\u201310 inclusive.",\n      "maximum": 10,\n      "minimum": 2,\n      "type": "integer"\n    },\n    "side_effects": {\n      "additionalProperties": true,\n      "description": "Standard sweetbean side-effects dict applied after the trial completes.",\n      "type": "object"\n    },\n    "value": {\n      "default": null,\n      "description": "Controls the display/response mode split. Omit or pass null for response mode (participant presses a key, result stored in bean_response). Pass an integer to show that many filled pips and auto-advance. Pass a handle string referencing a sweetbean Variable (e.g. a TimelineVariable) to defer per-trial resolution \\u2014 the runtime resolves the handle before dispatch.",\n      "oneOf": [\n        {\n          "description": "Static filled-pip count; switches to display mode.",\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "description": "Handle string for a sweetbean Variable; resolved per trial.",\n          "type": "string"\n        },\n        {\n          "description": "Response mode \\u2014 waits for participant keypress.",\n          "type": "null"\n        }\n      ]\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nMode is determined entirely by `value`: null → response mode; integer or Variable handle → display mode. Passing a Python list to `value` raises ValueError — use a Variable handle string instead. In response mode, `bean_response` in jsPsych data holds the pressed digit string (\'1\'..\'n_points\'); it is absent or null in display mode. Display mode silently defaults to 1500 ms auto-advance when `duration` is omitted — pass an explicit `duration` to override. `n_points` outside 2–10 raises ValueError at construction time.'
TOOL_PARAMETERS = { 'properties': { 'duration': { 'description': 'Trial duration in milliseconds. In '
                                               'display mode, omitting this defaults '
                                               'to 1500 ms (auto-advance). In response '
                                               'mode, omitting this means no timeout — '
                                               'the trial waits for a keypress.',
                                'minimum': 0,
                                'type': 'integer'},
                  'label': { 'description': 'Optional text caption rendered above the '
                                            'pip row.',
                             'type': 'string'},
                  'n_points': { 'default': 5,
                                'description': 'Number of discrete rating points on '
                                               'the scale. Must be 2–10 inclusive.',
                                'maximum': 10,
                                'minimum': 2,
                                'type': 'integer'},
                  'side_effects': { 'additionalProperties': True,
                                    'description': 'Standard sweetbean side-effects '
                                                   'dict applied after the trial '
                                                   'completes.',
                                    'type': 'object'},
                  'value': { 'default': None,
                             'description': 'Controls the display/response mode split. '
                                            'Omit or pass null for response mode '
                                            '(participant presses a key, result stored '
                                            'in bean_response). Pass an integer to '
                                            'show that many filled pips and '
                                            'auto-advance. Pass a handle string '
                                            'referencing a sweetbean Variable (e.g. a '
                                            'TimelineVariable) to defer per-trial '
                                            'resolution — the runtime resolves the '
                                            'handle before dispatch.',
                             'oneOf': [ { 'description': 'Static filled-pip count; '
                                                         'switches to display mode.',
                                          'minimum': 1,
                                          'type': 'integer'},
                                        { 'description': 'Handle string for a '
                                                         'sweetbean Variable; resolved '
                                                         'per trial.',
                                          'type': 'string'},
                                        { 'description': 'Response mode — waits for '
                                                         'participant keypress.',
                                          'type': 'null'}]}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "Mode is determined entirely by `value`: null → response mode; integer or Variable handle → display mode. Passing a Python list to `value` raises ValueError — use a Variable handle string instead. In response mode, `bean_response` in jsPsych data holds the pressed digit string ('1'..'n_points'); it is absent or null in display mode. Display mode silently defaults to 1500 ms auto-advance when `duration` is omitted — pass an explicit `duration` to override. `n_points` outside 2–10 raises ValueError at construction time."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.RatingResponse
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
    def create_rating_response(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the pipeline — after SweetPea has sampled a trial sequence — to add a discrete N-point rating widget or a static filled-pip display to a SweetBean trial.'
        return _impl(args or {})
