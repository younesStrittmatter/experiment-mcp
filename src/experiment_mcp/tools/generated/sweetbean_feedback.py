"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'fa3efdab26489509c5eaa80cf1c83a3cfdb6a911e0dd9a5ea2b2af6c55f1ea4b'
__exp_qualname__ = 'sweetbean.stimulus.Feedback'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_feedback'
TOOL_DESCRIPTION = 'Call this tool after constructing a response stimulus (e.g., HtmlKeyboardResponse with `choices` and `correct_key`) to append a Feedback stimulus that automatically displays a correct/incorrect message based on the participant\'s response. The result is a Feedback stimulus handle to be passed into a Trial or Block alongside the preceding stimulus.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "correct_color": {\n      "default": "green",\n      "description": "CSS color of the correct message text.",\n      "type": "string"\n    },\n    "correct_message": {\n      "default": "Correct!",\n      "description": "Text displayed when the participant\'s response was correct.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Time in milliseconds the feedback message is displayed. Omit for indefinite display.",\n      "type": "integer"\n    },\n    "false_color": {\n      "default": "red",\n      "description": "CSS color of the incorrect message text.",\n      "type": "string"\n    },\n    "false_message": {\n      "default": "False!",\n      "description": "Text displayed when the participant\'s response was incorrect.",\n      "type": "string"\n    },\n    "side_effects": {\n      "description": "Optional list of SideEffect handle strings (produced by SideEffect tools) to update global runtime state such as cumulative score or trial counter.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "window": {\n      "default": 1,\n      "description": "How many stimuli back to look for the response to evaluate. The target stimulus at that offset must have both `choices` and `correct_key` set. Default 1 means the immediately preceding stimulus.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe stimulus `window` positions back in the same trial must have both `choices` and `correct_key` parameters — if it does not, the correctness check will silently fail or error at runtime. All constructor arguments have defaults, so the tool can be called with no arguments for a minimal feedback stimulus. `side_effects` items are handle strings, not inline definitions.'
TOOL_PARAMETERS = { 'properties': { 'correct_color': { 'default': 'green',
                                     'description': 'CSS color of the correct message '
                                                    'text.',
                                     'type': 'string'},
                  'correct_message': { 'default': 'Correct!',
                                       'description': 'Text displayed when the '
                                                      "participant's response was "
                                                      'correct.',
                                       'type': 'string'},
                  'duration': { 'description': 'Time in milliseconds the feedback '
                                               'message is displayed. Omit for '
                                               'indefinite display.',
                                'type': 'integer'},
                  'false_color': { 'default': 'red',
                                   'description': 'CSS color of the incorrect message '
                                                  'text.',
                                   'type': 'string'},
                  'false_message': { 'default': 'False!',
                                     'description': 'Text displayed when the '
                                                    "participant's response was "
                                                    'incorrect.',
                                     'type': 'string'},
                  'side_effects': { 'description': 'Optional list of SideEffect handle '
                                                   'strings (produced by SideEffect '
                                                   'tools) to update global runtime '
                                                   'state such as cumulative score or '
                                                   'trial counter.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'window': { 'default': 1,
                              'description': 'How many stimuli back to look for the '
                                             'response to evaluate. The target '
                                             'stimulus at that offset must have both '
                                             '`choices` and `correct_key` set. Default '
                                             '1 means the immediately preceding '
                                             'stimulus.',
                              'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The stimulus `window` positions back in the same trial must have both `choices` and `correct_key` parameters — if it does not, the correctness check will silently fail or error at runtime. All constructor arguments have defaults, so the tool can be called with no arguments for a minimal feedback stimulus. `side_effects` items are handle strings, not inline definitions.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Feedback
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
    def create_feedback(args: dict[str, Any] | None = None) -> Any:
        "Call this tool after constructing a response stimulus (e.g., HtmlKeyboardResponse with `choices` and `correct_key`) to append a Feedback stimulus that automatically displays a correct/incorrect message based on the participant's response."
        return _impl(args or {})
