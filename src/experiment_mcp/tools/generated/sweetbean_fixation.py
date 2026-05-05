"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'a9d3c9f1cddd210e00ebd9bbe20540d42c9bec226d269817e52d7d55d66dac23'
__exp_qualname__ = 'sweetbean.stimulus.Fixation'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_fixation'
TOOL_DESCRIPTION = 'Use this tool to create a fixation-cross stimulus for inter-trial intervals or baseline periods in a jsPsych experiment. Call it in step 3 of the SweetPea→SweetBean pipeline, after sampling a trial sequence, whenever a trial needs a centered white "+" before or between other stimuli. Returns a Fixation handle that can be passed to a SweetBean Trial or Block tool.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "duration": {\n      "description": "How long the fixation cross is displayed, in milliseconds. If omitted, the stimulus waits indefinitely for a keypress (no timeout).",\n      "type": "integer"\n    },\n    "side_effects": {\n      "description": "Optional list of SideEffect handle strings (produced by SweetBean SideEffect tools) that update global runtime data such as score or trial counter while this stimulus is shown.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe cross text ("+"), color ("white"), and allowed keys ([]) are hardcoded — do not attempt to override them. If duration is omitted the stimulus renders with no time limit, which is rarely what you want for a fixation; always supply duration for timed paradigms. side_effects items must be handle strings returned by SideEffect constructor tools, not raw dicts.'
TOOL_PARAMETERS = { 'properties': { 'duration': { 'description': 'How long the fixation cross is '
                                               'displayed, in milliseconds. If '
                                               'omitted, the stimulus waits '
                                               'indefinitely for a keypress (no '
                                               'timeout).',
                                'type': 'integer'},
                  'side_effects': { 'description': 'Optional list of SideEffect handle '
                                                   'strings (produced by SweetBean '
                                                   'SideEffect tools) that update '
                                                   'global runtime data such as score '
                                                   'or trial counter while this '
                                                   'stimulus is shown.',
                                    'items': {'type': 'string'},
                                    'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The cross text ("+"), color ("white"), and allowed keys ([]) are hardcoded — do not attempt to override them. If duration is omitted the stimulus renders with no time limit, which is rarely what you want for a fixation; always supply duration for timed paradigms. side_effects items must be handle strings returned by SideEffect constructor tools, not raw dicts.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Fixation
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
    def create_fixation(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create a fixation-cross stimulus for inter-trial intervals or baseline periods in a jsPsych experiment.'
        return _impl(args or {})
