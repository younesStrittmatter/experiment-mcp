"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '440824d762956c9c38e9615c6aa359aa8d5e4ae4b4d4ebc7a507028507f5895c'
__exp_qualname__ = 'sweetbean.stimulus.HtmlKeyboardResponse'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_html_keyboard_response'
TOOL_DESCRIPTION = 'Call this tool at stimulus-definition time — after SweetPea has sampled a trial sequence but before assembling a SweetBean Block — to create an HTML-rendered, keyboard-response stimulus that jsPsych will display to participants and collect key-press data from. Returns a stimulus handle to pass into Trial or Block tool calls.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "choices": {\n      "default": [],\n      "description": "Keys that will be recorded if pressed (e.g. [\\"f\\", \\"j\\"]). Empty list means no keys are recorded.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key considered correct for this trial. Used for accuracy scoring; does not restrict which keys are recorded.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Time in milliseconds the stimulus is shown before advancing automatically. Omit to wait indefinitely for a key press.",\n      "type": "integer"\n    },\n    "fit_to_viewport": {\n      "description": "If true, CSS-zooms rendered content to fill the viewport without overflow. If false, uses natural layout with scrolling. Omit to use the class default (true for most stimuli).",\n      "type": "boolean"\n    },\n    "min_rt": {\n      "description": "Minimum response time in milliseconds. Key presses are swallowed for this duration, preventing single-key spamming. Omit to use the class default (normally 0).",\n      "type": "integer"\n    },\n    "side_effects": {\n      "description": "List of SideEffect definition handles (produced by SweetBean SideEffect tools) for updating global runtime state such as score or trial counter.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "stimulus": {\n      "default": "",\n      "description": "Raw HTML string rendered as the trial content. May reference SweetPea-sampled level values interpolated before dispatch.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `choices` defaults to `[]` — participants can view the stimulus but no key is recorded unless you pass an explicit list.\n- `correct_key` is metadata only; it does not filter or restrict `choices`.\n- `side_effects` items should be handle strings returned by SweetBean SideEffect constructor tools, not raw dicts.\n- `fit_to_viewport` and `min_rt` fall back to class-level defaults when omitted; for `HtmlKeyboardResponse` the class default for `fit_to_viewport` is `True` and for `min_rt` is `0`.\n- `duration` and `min_rt` are both in milliseconds; passing `min_rt` >= `duration` means the trial will time out before any key can register.'
TOOL_PARAMETERS = { 'properties': { 'choices': { 'default': [],
                               'description': 'Keys that will be recorded if pressed '
                                              '(e.g. ["f", "j"]). Empty list means no '
                                              'keys are recorded.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'correct_key': { 'default': '',
                                   'description': 'The key considered correct for this '
                                                  'trial. Used for accuracy scoring; '
                                                  'does not restrict which keys are '
                                                  'recorded.',
                                   'type': 'string'},
                  'duration': { 'description': 'Time in milliseconds the stimulus is '
                                               'shown before advancing automatically. '
                                               'Omit to wait indefinitely for a key '
                                               'press.',
                                'type': 'integer'},
                  'fit_to_viewport': { 'description': 'If true, CSS-zooms rendered '
                                                      'content to fill the viewport '
                                                      'without overflow. If false, '
                                                      'uses natural layout with '
                                                      'scrolling. Omit to use the '
                                                      'class default (true for most '
                                                      'stimuli).',
                                       'type': 'boolean'},
                  'min_rt': { 'description': 'Minimum response time in milliseconds. '
                                             'Key presses are swallowed for this '
                                             'duration, preventing single-key '
                                             'spamming. Omit to use the class default '
                                             '(normally 0).',
                              'type': 'integer'},
                  'side_effects': { 'description': 'List of SideEffect definition '
                                                   'handles (produced by SweetBean '
                                                   'SideEffect tools) for updating '
                                                   'global runtime state such as score '
                                                   'or trial counter.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'stimulus': { 'default': '',
                                'description': 'Raw HTML string rendered as the trial '
                                               'content. May reference '
                                               'SweetPea-sampled level values '
                                               'interpolated before dispatch.',
                                'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `choices` defaults to `[]` — participants can view the stimulus but no key is recorded unless you pass an explicit list.\n- `correct_key` is metadata only; it does not filter or restrict `choices`.\n- `side_effects` items should be handle strings returned by SweetBean SideEffect constructor tools, not raw dicts.\n- `fit_to_viewport` and `min_rt` fall back to class-level defaults when omitted; for `HtmlKeyboardResponse` the class default for `fit_to_viewport` is `True` and for `min_rt` is `0`.\n- `duration` and `min_rt` are both in milliseconds; passing `min_rt` >= `duration` means the trial will time out before any key can register.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.HtmlKeyboardResponse
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
    def create_html_keyboard_response(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at stimulus-definition time — after SweetPea has sampled a trial sequence but before assembling a SweetBean Block — to create an HTML-rendered, keyboard-response stimulus that jsPsych will display to participants and collect key-press data from.'
        return _impl(args or {})
