"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '08948dd97b26da99feee7f36ad93d59f538cf08b8c7fd3b47b655e4785727a59'
__exp_qualname__ = 'sweetbean.stimulus.LikertSurvey'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_likert_survey'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the SweetBean pipeline — after SweetPea has produced a trial sequence and you need to collect structured Likert-scale ratings from participants. Pass the resulting handle to a SweetBean `Trial` or `Block` tool to embed the survey in the experiment timeline. Each call produces a single survey stimulus that renders as a jsPsych SurveyLikert page.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "questions": {\n      "default": [],\n      "description": "List of question objects, each with a \'prompt\' (string, the question text) and \'labels\' (array of strings or numbers representing the scale anchors, e.g. [\'Strongly Disagree\', ..., \'Strongly Agree\']). Defaults to [] if omitted.",\n      "items": {\n        "properties": {\n          "labels": {\n            "description": "Ordered scale labels for this question.",\n            "items": {\n              "type": "string"\n            },\n            "type": "array"\n          },\n          "prompt": {\n            "description": "The question text shown to the participant.",\n            "type": "string"\n          }\n        },\n        "required": [\n          "prompt",\n          "labels"\n        ],\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "side_effects": {\n      "additionalProperties": true,\n      "description": "Optional dictionary of side effects to execute when the stimulus is processed (e.g. updating data variables). Omit if not needed.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nIf `questions` is omitted or falsy the survey renders with no questions — always supply at least one entry. Each question carries its own independent `labels` list, so different questions on the same page can use different scales; if all questions share a scale, prefer the `LikertSurvey.from_scale` constructor (not exposed as a separate tool) to avoid repetition. Labels are displayed in the order provided; order determines numeric coding in the response data (Q0, Q1, … keys). The `side_effects` dict is passed through unchanged to the parent `_Survey` class and is only needed for advanced data-routing patterns.'
TOOL_PARAMETERS = { 'properties': { 'questions': { 'default': [],
                                 'description': 'List of question objects, each with a '
                                                "'prompt' (string, the question text) "
                                                "and 'labels' (array of strings or "
                                                'numbers representing the scale '
                                                "anchors, e.g. ['Strongly Disagree', "
                                                "..., 'Strongly Agree']). Defaults to "
                                                '[] if omitted.',
                                 'items': { 'properties': { 'labels': { 'description': 'Ordered '
                                                                                       'scale '
                                                                                       'labels '
                                                                                       'for '
                                                                                       'this '
                                                                                       'question.',
                                                                        'items': { 'type': 'string'},
                                                                        'type': 'array'},
                                                            'prompt': { 'description': 'The '
                                                                                       'question '
                                                                                       'text '
                                                                                       'shown '
                                                                                       'to '
                                                                                       'the '
                                                                                       'participant.',
                                                                        'type': 'string'}},
                                            'required': ['prompt', 'labels'],
                                            'type': 'object'},
                                 'type': 'array'},
                  'side_effects': { 'additionalProperties': True,
                                    'description': 'Optional dictionary of side '
                                                   'effects to execute when the '
                                                   'stimulus is processed (e.g. '
                                                   'updating data variables). Omit if '
                                                   'not needed.',
                                    'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'If `questions` is omitted or falsy the survey renders with no questions — always supply at least one entry. Each question carries its own independent `labels` list, so different questions on the same page can use different scales; if all questions share a scale, prefer the `LikertSurvey.from_scale` constructor (not exposed as a separate tool) to avoid repetition. Labels are displayed in the order provided; order determines numeric coding in the response data (Q0, Q1, … keys). The `side_effects` dict is passed through unchanged to the parent `_Survey` class and is only needed for advanced data-routing patterns.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.LikertSurvey
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
    def create_likert_survey(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the SweetBean pipeline — after SweetPea has produced a trial sequence and you need to collect structured Likert-scale ratings from participants.'
        return _impl(args or {})
