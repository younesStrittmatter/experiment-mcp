"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'fa7db812ea0641ea710146ffcccaa9d1a5bff58ec8dfcd0d5dafecf2906ee60d'
__exp_qualname__ = 'sweetbean.stimulus.MultiChoiceSurvey'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_multi_choice_survey'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the pipeline — after sampling a SweetPea trial sequence — to create a multiple-choice survey stimulus that presents one or more questions each with a fixed set of answer options. Returns a handle to a `MultiChoiceSurvey` stimulus that can be embedded in a SweetBean `Trial` or `Block`, and later compiled to HTML or run headless via `Experiment`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "questions": {\n      "default": [],\n      "description": "List of question objects. Each object must have a \'prompt\' key (string) and an \'options\' key (array of strings or numbers representing the selectable choices).",\n      "items": {\n        "properties": {\n          "options": {\n            "description": "The selectable answer choices for this question.",\n            "items": {\n              "type": "string"\n            },\n            "type": "array"\n          },\n          "prompt": {\n            "description": "The question text shown to the participant.",\n            "type": "string"\n          }\n        },\n        "required": [\n          "prompt",\n          "options"\n        ],\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "side_effects": {\n      "additionalProperties": true,\n      "description": "Optional dictionary of side effects that are triggered based on participant responses. Omit if no conditional side effects are needed.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nIf `questions` is omitted or an empty list, the survey renders with no questions — always provide at least one entry. Each question\'s `options` values are cast to strings via `str()` before display, so numeric options are safe. In headless / language-model mode (`process_l`), option values are presented as a comma-separated list appended to the prompt; responses are keyed `Q0`, `Q1`, … in the returned data dict. `side_effects` is passed through to the parent `_Survey` class and may be `null`/omitted when not needed.'
TOOL_PARAMETERS = { 'properties': { 'questions': { 'default': [],
                                 'description': 'List of question objects. Each object '
                                                "must have a 'prompt' key (string) and "
                                                "an 'options' key (array of strings or "
                                                'numbers representing the selectable '
                                                'choices).',
                                 'items': { 'properties': { 'options': { 'description': 'The '
                                                                                        'selectable '
                                                                                        'answer '
                                                                                        'choices '
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
                                            'required': ['prompt', 'options'],
                                            'type': 'object'},
                                 'type': 'array'},
                  'side_effects': { 'additionalProperties': True,
                                    'description': 'Optional dictionary of side '
                                                   'effects that are triggered based '
                                                   'on participant responses. Omit if '
                                                   'no conditional side effects are '
                                                   'needed.',
                                    'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = "If `questions` is omitted or an empty list, the survey renders with no questions — always provide at least one entry. Each question's `options` values are cast to strings via `str()` before display, so numeric options are safe. In headless / language-model mode (`process_l`), option values are presented as a comma-separated list appended to the prompt; responses are keyed `Q0`, `Q1`, … in the returned data dict. `side_effects` is passed through to the parent `_Survey` class and may be `null`/omitted when not needed."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.MultiChoiceSurvey
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
    def create_multi_choice_survey(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the pipeline — after sampling a SweetPea trial sequence — to create a multiple-choice survey stimulus that presents one or more questions each with a fixed set of answer options.'
        return _impl(args or {})
