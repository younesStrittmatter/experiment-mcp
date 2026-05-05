"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '691e68204003b8666baf126861df4f28efeeb03dac226bb17ef11a7c78bc729c'
__exp_qualname__ = 'sweetbean.stimulus.Stroop'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_stroop'
TOOL_DESCRIPTION = 'Call this tool to create a colored-text stimulus for a Stroop (or Stroop-like) trial — step 3 of the typical pipeline, after SweetPea has sampled a trial sequence and you have concrete `text` and `color` level values to wire in. The result is a SweetBean `Text` stimulus handle that can be passed to a `Trial` or `Block` tool to build a jsPsych experiment.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "choices": {\n      "description": "Keyboard keys that will be recorded if pressed (e.g. [\'f\', \'j\']). Defaults to an empty list (no keys recorded).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "color": {\n      "description": "CSS color for the text (e.g. \'red\', \'#0000FF\'). Defaults to \'white\'.",\n      "type": "string"\n    },\n    "correct_key": {\n      "description": "The key that counts as a correct response for accuracy scoring. Leave empty if accuracy is not needed.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "How long the stimulus is shown, in milliseconds. Omit (or pass null) for an indefinite display that waits for a key press.",\n      "type": "integer"\n    },\n    "side_effects": {\n      "description": "Optional list of SideEffect definitions (SweetBean SideEffect objects or their handle strings) for updating global runtime state such as score counters between trials.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "text": {\n      "description": "The word to display (e.g. \'RED\', \'BLUE\'). Defaults to an empty string, which renders a blank screen.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe `color` parameter accepts any CSS color value; it is injected directly into an inline `style` attribute — pass a valid CSS color string. If `text` is empty the LLM-readable template describes the screen as "a blank screen", which may affect language-model simulation logs. `choices` defaults to `[]` (no key capture); pass an explicit list whenever you need response data. Handle strings returned by SweetPea level-sampling tools can be passed as `text` and `color` values — the runtime resolves them to their string values before constructing the stimulus.'
TOOL_PARAMETERS = { 'properties': { 'choices': { 'description': 'Keyboard keys that will be recorded if '
                                              "pressed (e.g. ['f', 'j']). Defaults to "
                                              'an empty list (no keys recorded).',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'color': { 'description': "CSS color for the text (e.g. 'red', "
                                            "'#0000FF'). Defaults to 'white'.",
                             'type': 'string'},
                  'correct_key': { 'description': 'The key that counts as a correct '
                                                  'response for accuracy scoring. '
                                                  'Leave empty if accuracy is not '
                                                  'needed.',
                                   'type': 'string'},
                  'duration': { 'description': 'How long the stimulus is shown, in '
                                               'milliseconds. Omit (or pass null) for '
                                               'an indefinite display that waits for a '
                                               'key press.',
                                'type': 'integer'},
                  'side_effects': { 'description': 'Optional list of SideEffect '
                                                   'definitions (SweetBean SideEffect '
                                                   'objects or their handle strings) '
                                                   'for updating global runtime state '
                                                   'such as score counters between '
                                                   'trials.',
                                    'items': {'type': 'object'},
                                    'type': 'array'},
                  'text': { 'description': "The word to display (e.g. 'RED', 'BLUE'). "
                                           'Defaults to an empty string, which renders '
                                           'a blank screen.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The `color` parameter accepts any CSS color value; it is injected directly into an inline `style` attribute — pass a valid CSS color string. If `text` is empty the LLM-readable template describes the screen as "a blank screen", which may affect language-model simulation logs. `choices` defaults to `[]` (no key capture); pass an explicit list whenever you need response data. Handle strings returned by SweetPea level-sampling tools can be passed as `text` and `color` values — the runtime resolves them to their string values before constructing the stimulus.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Stroop
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
    def create_stroop(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a colored-text stimulus for a Stroop (or Stroop-like) trial — step 3 of the typical pipeline, after SweetPea has sampled a trial sequence and you have concrete `text` and `color` level values to wire in.'
        return _impl(args or {})
