"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '1de0985135b1c387b0ec30c1d7fdf11faf355565cf5abd194f9ccd2888a755f5'
__exp_qualname__ = 'sweetbean.BotDetection'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_bot_detection'
TOOL_DESCRIPTION = 'Call this tool when building a SweetBean experiment that will be served to human participants and you want to flag or deter automated/bot responses. Use it at experiment-assembly time — after constructing stimuli and blocks but before compiling to HTML — by passing the returned handle as a protection layer to the Experiment. The tool returns a handle to a BotDetection object that injects passive interaction logging (RT distribution, slider moves, trial-level interaction stats) and, when countermeasures are enabled, active traps (honeypot DOM, clipboard/devtools blocking) into the jsPsych runtime.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "enable_countermeasures": {\n      "default": true,\n      "description": "When true (default), active countermeasures are enabled: honeypot DOM elements, clipboard blocking, devtools traps. Set to false for pilot runs or debugging to get passive logging only without interference with normal browser behaviour.",\n      "type": "boolean"\n    },\n    "track_sliders": {\n      "default": true,\n      "description": "When true (default), installs a document-level input listener that records every range-slider move via BotDetection.recordSliderMove(), capturing per-trial slider interaction stats without modifying any stimulus class.",\n      "type": "boolean"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nBoth parameters default to true so calling with no arguments gives full protection. Set enable_countermeasures=false during piloting — active countermeasures can interfere with debugging tools and produce confusing behaviour for the experimenter. Per-trial interaction data (RT, slider stats) is merged into jsPsych trial data automatically at on_finish; no extra data-collection code is needed. The protection only takes effect after the experiment is compiled to HTML; this tool alone does not modify any existing stimulus or block handle.'
TOOL_PARAMETERS = { 'properties': { 'enable_countermeasures': { 'default': True,
                                              'description': 'When true (default), '
                                                             'active countermeasures '
                                                             'are enabled: honeypot '
                                                             'DOM elements, clipboard '
                                                             'blocking, devtools '
                                                             'traps. Set to false for '
                                                             'pilot runs or debugging '
                                                             'to get passive logging '
                                                             'only without '
                                                             'interference with normal '
                                                             'browser behaviour.',
                                              'type': 'boolean'},
                  'track_sliders': { 'default': True,
                                     'description': 'When true (default), installs a '
                                                    'document-level input listener '
                                                    'that records every range-slider '
                                                    'move via '
                                                    'BotDetection.recordSliderMove(), '
                                                    'capturing per-trial slider '
                                                    'interaction stats without '
                                                    'modifying any stimulus class.',
                                     'type': 'boolean'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'Both parameters default to true so calling with no arguments gives full protection. Set enable_countermeasures=false during piloting — active countermeasures can interfere with debugging tools and produce confusing behaviour for the experimenter. Per-trial interaction data (RT, slider stats) is merged into jsPsych trial data automatically at on_finish; no extra data-collection code is needed. The protection only takes effect after the experiment is compiled to HTML; this tool alone does not modify any existing stimulus or block handle.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.BotDetection
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
    def create_bot_detection(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when building a SweetBean experiment that will be served to human participants and you want to flag or deter automated/bot responses.'
        return _impl(args or {})
