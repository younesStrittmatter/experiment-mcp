"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '1e9c131679149c8c909c9ec31fbb8e216cfe24f689dde43cc47da1fd1a553632'
__exp_qualname__ = 'sweetpea.CrossBlock'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_cross_block'
TOOL_DESCRIPTION = 'Call this tool after creating Factors (and optionally Constraints) to declare the full factorial design of an experiment — this is step 1 of the SweetPea pipeline. It returns a CrossBlock handle that you pass to a synthesis tool (e.g. `sweetpea_synthesize_trials`) to sample a balanced, randomized trial sequence; that sequence is then wired into SweetBean stimuli and blocks.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "constraints": {\n      "description": "Handle strings for Constraint objects (e.g. Exclude, Forbid) that restrict the generated trials. Pass an empty array if there are no constraints.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "crossing": {\n      "description": "Handle strings for the subset of Factors to fully cross. The number of trials per block equals the product of the level counts of these factors. Must be a subset of design.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "design": {\n      "description": "Handle strings for every Factor in the experiment. Each trial in the generated sequence will have one level drawn from each factor listed here.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "require_complete_crossing": {\n      "default": true,\n      "description": "When true (default), every combination of levels in the crossing must appear exactly once per block. Set to false only when Exclude constraints intentionally omit some combinations.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "design",\n    "crossing",\n    "constraints"\n  ],\n  "type": "object"\n}\n\nNotes:\n`constraints` has no default in the constructor — agents must always supply it; pass `[]` when there are none. Trial count per block is determined solely by `crossing`, not by the full `design` list. `require_complete_crossing=false` is only meaningful when paired with `Exclude` constraints; using it without them produces under-constrained blocks. All Factor handles in `crossing` must also appear in `design`, or synthesis will raise a validation error.'
TOOL_PARAMETERS = { 'properties': { 'constraints': { 'description': 'Handle strings for Constraint '
                                                  'objects (e.g. Exclude, Forbid) that '
                                                  'restrict the generated trials. Pass '
                                                  'an empty array if there are no '
                                                  'constraints.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'crossing': { 'description': 'Handle strings for the subset of '
                                               'Factors to fully cross. The number of '
                                               'trials per block equals the product of '
                                               'the level counts of these factors. '
                                               'Must be a subset of design.',
                                'items': {'type': 'string'},
                                'type': 'array'},
                  'design': { 'description': 'Handle strings for every Factor in the '
                                             'experiment. Each trial in the generated '
                                             'sequence will have one level drawn from '
                                             'each factor listed here.',
                              'items': {'type': 'string'},
                              'type': 'array'},
                  'require_complete_crossing': { 'default': True,
                                                 'description': 'When true (default), '
                                                                'every combination of '
                                                                'levels in the '
                                                                'crossing must appear '
                                                                'exactly once per '
                                                                'block. Set to false '
                                                                'only when Exclude '
                                                                'constraints '
                                                                'intentionally omit '
                                                                'some combinations.',
                                                 'type': 'boolean'}},
  'required': ['design', 'crossing', 'constraints'],
  'type': 'object'}
TOOL_NOTES = '`constraints` has no default in the constructor — agents must always supply it; pass `[]` when there are none. Trial count per block is determined solely by `crossing`, not by the full `design` list. `require_complete_crossing=false` is only meaningful when paired with `Exclude` constraints; using it without them produces under-constrained blocks. All Factor handles in `crossing` must also appear in `design`, or synthesis will raise a validation error.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.CrossBlock
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
    def create_cross_block(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after creating Factors (and optionally Constraints) to declare the full factorial design of an experiment — this is step 1 of the SweetPea pipeline.'
        return _impl(args or {})
