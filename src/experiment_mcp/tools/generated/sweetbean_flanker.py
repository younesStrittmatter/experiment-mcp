"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '061457990cd7def439357ee4664689159edfe3fd9b688d22fe94439f66d14b74'
__exp_qualname__ = 'sweetbean.stimulus.Flanker'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_flanker'
TOOL_DESCRIPTION = 'Call this tool to create a Flanker stimulus for a flanker attention/conflict task, after SweetPea has sampled a trial sequence with `direction` and `distractor` factors. The result is a Flanker stimulus handle that encodes a central target arrow flanked by distractor arrows (e.g. `<< < <<`, `>> > >>`), ready to be passed into a SweetBean Trial.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "choices": {\n      "description": "Keys that will be recorded if pressed during stimulus display (e.g. [\\"ArrowLeft\\", \\"ArrowRight\\"]). Omit to record no keys.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "color": {\n      "default": "white",\n      "description": "CSS color of the arrow text (e.g. \'white\', \'#ff0000\').",\n      "type": "string"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The key the participant must press to be scored correct. Used for accuracy feedback and scoring.",\n      "type": "string"\n    },\n    "direction": {\n      "default": "left",\n      "description": "Direction of the central target arrow. Accepts \'left\', \'right\', \'l\', \'r\', \'L\', or \'R\'. When wiring SweetPea-sampled levels, pass a DataVariable or CodeVariable handle string instead of a literal.",\n      "type": "string"\n    },\n    "distractor": {\n      "default": "left",\n      "description": "Direction of the flanking distractor arrows. Same accepted values as `direction`. Pass a handle string when driven by a SweetPea factor.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Time in milliseconds the stimulus is displayed. Omit for indefinite display until a key is pressed.",\n      "type": "integer"\n    },\n    "n_flankers": {\n      "default": 2,\n      "description": "Number of distractor arrows on EACH side of the target. Default 2 produces `<< < <<` (2 left + target + 2 right).",\n      "type": "integer"\n    },\n    "side_effects": {\n      "description": "List of SideEffect handle strings (produced by SweetBean SideEffect tools) for updating global state such as running score or trial counter.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `direction` and `distractor` accept both full words and single letters (case-insensitive). Any unrecognised value silently produces an empty string for that arrow — no error is raised, which can result in a malformed stimulus.\n- `n_flankers` is the count per side, not total: `n_flankers=2` renders 5 symbols total (2 distractors + 1 target + 2 distractors).\n- When the trial sequence comes from SweetPea, `direction` and `distractor` should be SweetBean `DataVariable` or `CodeVariable` handle strings that resolve to the sampled level at runtime, not plain string literals.\n- `side_effects` items must be handle strings returned by SweetBean SideEffect constructor tools, not raw dicts.'
TOOL_PARAMETERS = { 'properties': { 'choices': { 'description': 'Keys that will be recorded if pressed '
                                              'during stimulus display (e.g. '
                                              '["ArrowLeft", "ArrowRight"]). Omit to '
                                              'record no keys.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'color': { 'default': 'white',
                             'description': 'CSS color of the arrow text (e.g. '
                                            "'white', '#ff0000').",
                             'type': 'string'},
                  'correct_key': { 'default': '',
                                   'description': 'The key the participant must press '
                                                  'to be scored correct. Used for '
                                                  'accuracy feedback and scoring.',
                                   'type': 'string'},
                  'direction': { 'default': 'left',
                                 'description': 'Direction of the central target '
                                                "arrow. Accepts 'left', 'right', 'l', "
                                                "'r', 'L', or 'R'. When wiring "
                                                'SweetPea-sampled levels, pass a '
                                                'DataVariable or CodeVariable handle '
                                                'string instead of a literal.',
                                 'type': 'string'},
                  'distractor': { 'default': 'left',
                                  'description': 'Direction of the flanking distractor '
                                                 'arrows. Same accepted values as '
                                                 '`direction`. Pass a handle string '
                                                 'when driven by a SweetPea factor.',
                                  'type': 'string'},
                  'duration': { 'description': 'Time in milliseconds the stimulus is '
                                               'displayed. Omit for indefinite display '
                                               'until a key is pressed.',
                                'type': 'integer'},
                  'n_flankers': { 'default': 2,
                                  'description': 'Number of distractor arrows on EACH '
                                                 'side of the target. Default 2 '
                                                 'produces `<< < <<` (2 left + target '
                                                 '+ 2 right).',
                                  'type': 'integer'},
                  'side_effects': { 'description': 'List of SideEffect handle strings '
                                                   '(produced by SweetBean SideEffect '
                                                   'tools) for updating global state '
                                                   'such as running score or trial '
                                                   'counter.',
                                    'items': {'type': 'string'},
                                    'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `direction` and `distractor` accept both full words and single letters (case-insensitive). Any unrecognised value silently produces an empty string for that arrow — no error is raised, which can result in a malformed stimulus.\n- `n_flankers` is the count per side, not total: `n_flankers=2` renders 5 symbols total (2 distractors + 1 target + 2 distractors).\n- When the trial sequence comes from SweetPea, `direction` and `distractor` should be SweetBean `DataVariable` or `CodeVariable` handle strings that resolve to the sampled level at runtime, not plain string literals.\n- `side_effects` items must be handle strings returned by SweetBean SideEffect constructor tools, not raw dicts.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Flanker
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
    def create_flanker(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a Flanker stimulus for a flanker attention/conflict task, after SweetPea has sampled a trial sequence with `direction` and `distractor` factors.'
        return _impl(args or {})
