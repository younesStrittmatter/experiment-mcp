"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '56cff9dcd6d365db215f86e249e5e84fd9557476d9192dc1f2e89245f4ac1457'
__exp_qualname__ = 'sweetbean.stimulus.Blank'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_blank'
TOOL_DESCRIPTION = 'Use this tool to create a blank-screen stimulus (inter-trial interval, fixation pause, or rest period) in a SweetBean trial sequence. Call it when you need a trial with no visible content — the result is a Blank stimulus object (handle string) that can be passed into a SweetBean Trial or Block alongside other stimuli. Fits between SweetPea sequence sampling and SweetBean Block assembly.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "choices": {\n      "description": "Keys that will be recorded if pressed during the blank interval (e.g. [\\"f\\", \\"j\\"]). Omit to accept no key input.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key considered correct for this trial. Defaults to empty string (no correct key). Used for accuracy scoring.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "How long the blank screen is shown, in milliseconds. If omitted, the trial waits indefinitely for a key press.",\n      "type": "integer"\n    },\n    "side_effects": {\n      "description": "List of SideEffect definitions that update global runtime data (e.g. score counter, trial counter) when this stimulus fires. See SweetBean SideEffect docs.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nAll parameters are optional; a bare `Blank()` call is valid and produces an indefinite blank screen. `duration` is in milliseconds — do not pass seconds. `correct_key` defaults to empty string, not null; scoring logic that checks for a non-empty correct key will treat the default as "no correct answer". `side_effects` expects SideEffect objects serialized as handle strings or plain dicts depending on runtime support — verify with SweetBean docs before use.'
TOOL_PARAMETERS = { 'properties': { 'choices': { 'description': 'Keys that will be recorded if pressed '
                                              'during the blank interval (e.g. ["f", '
                                              '"j"]). Omit to accept no key input.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'correct_key': { 'default': '',
                                   'description': 'The key considered correct for this '
                                                  'trial. Defaults to empty string (no '
                                                  'correct key). Used for accuracy '
                                                  'scoring.',
                                   'type': 'string'},
                  'duration': { 'description': 'How long the blank screen is shown, in '
                                               'milliseconds. If omitted, the trial '
                                               'waits indefinitely for a key press.',
                                'type': 'integer'},
                  'side_effects': { 'description': 'List of SideEffect definitions '
                                                   'that update global runtime data '
                                                   '(e.g. score counter, trial '
                                                   'counter) when this stimulus fires. '
                                                   'See SweetBean SideEffect docs.',
                                    'items': {'type': 'object'},
                                    'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'All parameters are optional; a bare `Blank()` call is valid and produces an indefinite blank screen. `duration` is in milliseconds — do not pass seconds. `correct_key` defaults to empty string, not null; scoring logic that checks for a non-empty correct key will treat the default as "no correct answer". `side_effects` expects SideEffect objects serialized as handle strings or plain dicts depending on runtime support — verify with SweetBean docs before use.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Blank
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
    def create_blank(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a blank-screen stimulus (inter-trial interval, fixation pause, or rest period) in a SweetBean trial sequence.'
        return _impl(args or {})
