"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '5b7925a18c15e1beac078fe0dd5fc05f6239684188474ff291c99fe6108e19e3'
__exp_qualname__ = 'sweetbean.stimulus.TextSurvey'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_text_survey'
TOOL_DESCRIPTION = 'Call this tool during SweetBean experiment construction (after SweetPea generates a trial sequence) when you need a stimulus that presents one or more free-text questions to participants and collects open-ended responses. Returns a TextSurvey handle that can be passed to a SweetBean Trial as a stimulus. Responses are stored as Q0, Q1, … keyed entries in the trial data.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "questions": {\n      "default": [],\n      "description": "List of question strings to present to the participant. Each string becomes a separate text-input prompt rendered by jsPsychSurveyText.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "side_effects": {\n      "description": "Optional list of SideEffect definition objects (see SweetBean docs) used to update global runtime state such as score or trial counter. Pass as handle strings if produced by another tool.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nIf `questions` is omitted or empty, the stimulus renders with no questions — participants see an empty survey. Responses are keyed Q0, Q1, … (zero-indexed) in the trial data dict, not by question text. When the experiment is run headlessly via `process_l` (language-model mode), questions are presented sequentially with `<<` as the response delimiter; the model\'s reply is extracted between `<<` markers. The underlying jsPsych plugin is `jsPsychSurveyText`; ensure that plugin is included in the jsPsych build if assembling HTML manually.'
TOOL_PARAMETERS = { 'properties': { 'questions': { 'default': [],
                                 'description': 'List of question strings to present '
                                                'to the participant. Each string '
                                                'becomes a separate text-input prompt '
                                                'rendered by jsPsychSurveyText.',
                                 'items': {'type': 'string'},
                                 'type': 'array'},
                  'side_effects': { 'description': 'Optional list of SideEffect '
                                                   'definition objects (see SweetBean '
                                                   'docs) used to update global '
                                                   'runtime state such as score or '
                                                   'trial counter. Pass as handle '
                                                   'strings if produced by another '
                                                   'tool.',
                                    'items': {'type': 'object'},
                                    'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "If `questions` is omitted or empty, the stimulus renders with no questions — participants see an empty survey. Responses are keyed Q0, Q1, … (zero-indexed) in the trial data dict, not by question text. When the experiment is run headlessly via `process_l` (language-model mode), questions are presented sequentially with `<<` as the response delimiter; the model's reply is extracted between `<<` markers. The underlying jsPsych plugin is `jsPsychSurveyText`; ensure that plugin is included in the jsPsych build if assembling HTML manually."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.TextSurvey
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
    def create_text_survey(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during SweetBean experiment construction (after SweetPea generates a trial sequence) when you need a stimulus that presents one or more free-text questions to participants and collects open-ended responses.'
        return _impl(args or {})
