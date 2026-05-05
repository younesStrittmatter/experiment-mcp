"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '691e68204003b8666baf126861df4f28efeeb03dac226bb17ef11a7c78bc729c'
__exp_qualname__ = 'sweetbean.stimulus.Text'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_text'
TOOL_DESCRIPTION = 'Call this tool at the SweetBean stimulus-building stage (step 3 of the pipeline) to create a colored-text display that can be used inside a SweetBean Trial or Block. Pass SweetPea-sampled factor levels (e.g., word string and ink color) as `text` and `color` to wire the factorial design into the jsPsych trial. Returns a `Text` stimulus handle to pass to trial-construction tools.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "choices": {\n      "default": [],\n      "description": "Keys the participant can press (e.g. [\'f\', \'j\']). An empty array means any key is accepted but nothing is recorded.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "color": {\n      "default": "white",\n      "description": "CSS color value for the displayed text (e.g. \'red\', \'#ff0000\'). Defaults to \'white\'.",\n      "type": "string"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key considered correct for this trial (used for accuracy scoring). Leave empty if accuracy is not tracked.",\n      "type": "string"\n    },\n    "duration": {\n      "default": null,\n      "description": "How long the stimulus is shown, in milliseconds. Omit or pass null for an indefinite display (waits for a keypress).",\n      "type": "integer"\n    },\n    "side_effects": {\n      "default": null,\n      "description": "Optional list of SideEffect handle strings returned by side-effect construction tools. Used to update global state such as running score or trial counter.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "text": {\n      "default": "",\n      "description": "The string to display on screen. Typically a SweetPea factor level (e.g. a word or symbol).",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nAll parameters are optional; omitting `text` renders a blank screen (the l_template says "you see a blank screen"). `duration` is in milliseconds — do not pass seconds. `color` accepts any valid CSS color string; the default \'white\' may be invisible on a white background, so always set it explicitly when the background matters. `choices` silently defaults to an empty list inside the constructor if not provided — pass an explicit list whenever you want keypress recording. `side_effects` items should be handle strings from SideEffect-producing tools, not raw SideEffect objects.'
TOOL_PARAMETERS = { 'properties': { 'choices': { 'default': [],
                               'description': 'Keys the participant can press (e.g. '
                                              "['f', 'j']). An empty array means any "
                                              'key is accepted but nothing is '
                                              'recorded.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'color': { 'default': 'white',
                             'description': 'CSS color value for the displayed text '
                                            "(e.g. 'red', '#ff0000'). Defaults to "
                                            "'white'.",
                             'type': 'string'},
                  'correct_key': { 'default': '',
                                   'description': 'The key considered correct for this '
                                                  'trial (used for accuracy scoring). '
                                                  'Leave empty if accuracy is not '
                                                  'tracked.',
                                   'type': 'string'},
                  'duration': { 'default': None,
                                'description': 'How long the stimulus is shown, in '
                                               'milliseconds. Omit or pass null for an '
                                               'indefinite display (waits for a '
                                               'keypress).',
                                'type': 'integer'},
                  'side_effects': { 'default': None,
                                    'description': 'Optional list of SideEffect handle '
                                                   'strings returned by side-effect '
                                                   'construction tools. Used to update '
                                                   'global state such as running score '
                                                   'or trial counter.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'text': { 'default': '',
                            'description': 'The string to display on screen. Typically '
                                           'a SweetPea factor level (e.g. a word or '
                                           'symbol).',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'All parameters are optional; omitting `text` renders a blank screen (the l_template says "you see a blank screen"). `duration` is in milliseconds — do not pass seconds. `color` accepts any valid CSS color string; the default \'white\' may be invisible on a white background, so always set it explicitly when the background matters. `choices` silently defaults to an empty list inside the constructor if not provided — pass an explicit list whenever you want keypress recording. `side_effects` items should be handle strings from SideEffect-producing tools, not raw SideEffect objects.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Text
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
    def create_text(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at the SweetBean stimulus-building stage (step 3 of the pipeline) to create a colored-text display that can be used inside a SweetBean Trial or Block.'
        return _impl(args or {})
