"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'ef7b9212732a627682ba478979e38ce2c4f245b211cb2204b808cfdcd515751e'
__exp_qualname__ = 'sweetbean.stimulus.HtmlChoice'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_html_choice'
TOOL_DESCRIPTION = 'Call this tool at SweetBean trial-construction time (step 3 of the pipeline) when a trial requires a participant to click one option from a set of rendered HTML items. It produces a SweetBean `HtmlChoice` stimulus object (returned as a handle string) that can be passed to a `Trial` or `Block` tool. The recorded data includes `choice` (0-based index), `value`, `bean_response`, and `bean_value`; optionally `bean_correct` if `correct_values` is provided.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "correct_values": {\n      "default": [],\n      "description": "Optional subset of `values` considered correct. When non-empty the trial data includes `bean_correct` (boolean). Pass an empty array to omit correctness tracking.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "duration": {\n      "description": "Maximum display time in milliseconds. Omit (or pass null) to keep the screen up until the participant clicks.",\n      "type": "integer"\n    },\n    "html_array": {\n      "default": [],\n      "description": "Ordered list of HTML strings rendered as clickable options. Must be the same length as `values`.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "side_effects": {\n      "default": [],\n      "description": "Handle strings for SideEffect objects (produced by SweetBean side-effect tools) that should fire when this stimulus records a response. Omit or pass an empty array if no side effects are needed.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "time_after_response": {\n      "default": 3000,\n      "description": "Extra delay in milliseconds after a click before the trial ends. Useful for visual confirmation animations. Default is 3000 ms.",\n      "type": "integer"\n    },\n    "values": {\n      "default": [],\n      "description": "Opaque labels/values (strings) aligned 1-to-1 with `html_array`. The entry at the clicked index is emitted as `value` and `bean_value`. Use strings; numeric values should be stringified.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `html_array` and `values` must be the same length; mismatched lengths silently yield broken trials (no runtime error).\n- `time_after_response` defaults to **3000 ms** — participants will see a 3-second pause after clicking even if no animation is needed. Pass `0` to eliminate the delay.\n- `duration` is the *maximum* display time; a click always ends the trial first (then `time_after_response` fires). If both `duration` and a click occur, the click wins.\n- `correct_values` entries are compared as strings; pass all numeric values as strings (e.g. `["1", "2"]`) to avoid silent mismatches.\n- `bean_correct` is `null` in the jsPsych data when `correct_values` is empty or omitted — downstream analysis code should guard against null before boolean-testing this field.\n- `side_effects` expects handle strings, not inline objects; produce SideEffect handles with the appropriate SweetBean side-effect tool first.'
TOOL_PARAMETERS = { 'properties': { 'correct_values': { 'default': [],
                                      'description': 'Optional subset of `values` '
                                                     'considered correct. When '
                                                     'non-empty the trial data '
                                                     'includes `bean_correct` '
                                                     '(boolean). Pass an empty array '
                                                     'to omit correctness tracking.',
                                      'items': {'type': 'string'},
                                      'type': 'array'},
                  'duration': { 'description': 'Maximum display time in milliseconds. '
                                               'Omit (or pass null) to keep the screen '
                                               'up until the participant clicks.',
                                'type': 'integer'},
                  'html_array': { 'default': [],
                                  'description': 'Ordered list of HTML strings '
                                                 'rendered as clickable options. Must '
                                                 'be the same length as `values`.',
                                  'items': {'type': 'string'},
                                  'type': 'array'},
                  'side_effects': { 'default': [],
                                    'description': 'Handle strings for SideEffect '
                                                   'objects (produced by SweetBean '
                                                   'side-effect tools) that should '
                                                   'fire when this stimulus records a '
                                                   'response. Omit or pass an empty '
                                                   'array if no side effects are '
                                                   'needed.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'time_after_response': { 'default': 3000,
                                           'description': 'Extra delay in milliseconds '
                                                          'after a click before the '
                                                          'trial ends. Useful for '
                                                          'visual confirmation '
                                                          'animations. Default is 3000 '
                                                          'ms.',
                                           'type': 'integer'},
                  'values': { 'default': [],
                              'description': 'Opaque labels/values (strings) aligned '
                                             '1-to-1 with `html_array`. The entry at '
                                             'the clicked index is emitted as `value` '
                                             'and `bean_value`. Use strings; numeric '
                                             'values should be stringified.',
                              'items': {'type': 'string'},
                              'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `html_array` and `values` must be the same length; mismatched lengths silently yield broken trials (no runtime error).\n- `time_after_response` defaults to **3000 ms** — participants will see a 3-second pause after clicking even if no animation is needed. Pass `0` to eliminate the delay.\n- `duration` is the *maximum* display time; a click always ends the trial first (then `time_after_response` fires). If both `duration` and a click occur, the click wins.\n- `correct_values` entries are compared as strings; pass all numeric values as strings (e.g. `["1", "2"]`) to avoid silent mismatches.\n- `bean_correct` is `null` in the jsPsych data when `correct_values` is empty or omitted — downstream analysis code should guard against null before boolean-testing this field.\n- `side_effects` expects handle strings, not inline objects; produce SideEffect handles with the appropriate SweetBean side-effect tool first.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.HtmlChoice
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
    def create_html_choice(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at SweetBean trial-construction time (step 3 of the pipeline) when a trial requires a participant to click one option from a set of rendered HTML items.'
        return _impl(args or {})
