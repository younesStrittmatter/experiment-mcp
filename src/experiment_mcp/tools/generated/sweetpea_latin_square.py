"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '20ebab5de4f05a343ed6d185f0cf0e0fe7d0ceb2381ab8b9315ef43356f1bfe3'
__exp_qualname__ = 'sweetpea.LatinSquare'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_latin_square'
TOOL_DESCRIPTION = 'Call this tool before constructing a NestedBlock when you need Latin Square counterbalancing — i.e., when each participant should see only one diagonal slice of the outer factor grid rather than all combinations. Pass the returned handle to NestedBlock\'s `constraints` argument; then pass a `participants` list to `synthesize_trials` so it builds one reduced NestedBlock per participant instead of solving the full outer grid. The result is a handle to a LatinSquare constraint object.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "num_diagonals": {\n      "description": "Number of diagonals (unique participant assignments). Defaults to the maximum level count across all outer_factors. Increase this to accommodate more participants than the default diagonal count.",\n      "type": "integer"\n    },\n    "outer_factors": {\n      "description": "Handle strings for the Factor objects that form the outer grid of the NestedBlock. Each string must be a handle returned by a prior Factor-creation tool call.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "require_balanced_grid": {\n      "default": true,\n      "description": "When true (default), prints a WARNING to stdout if outer factors have different numbers of levels (rectangular grid). Set to false to suppress these warnings when an unbalanced grid is intentional.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "outer_factors"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `num_diagonals` defaults to `max(len(f.levels) for f in outer_factors)`, so the default participant capacity equals the largest factor\'s level count — explicitly set it if you need more participants.\n- Participant IDs passed to `synthesize_trials` wrap cyclically via `participant % num_participants`, so IDs beyond `num_diagonals - 1` silently repeat earlier diagonals.\n- LatinSquare adds no SAT/ILP clauses; the per-participant trial reduction happens in `synthesize_trials`, not at constraint-creation time.\n- `outer_factors` must be the *external* factors of the NestedBlock (i.e., listed in NestedBlock\'s `design` but not in the inner CrossBlock\'s design); passing inner-block factors raises a `ValueError` at NestedBlock validation time, not at LatinSquare construction time.\n- Balance warnings are printed to stdout, not raised as exceptions, so a misconfigured grid will not fail loudly unless you inspect stdout.'
TOOL_PARAMETERS = { 'properties': { 'num_diagonals': { 'description': 'Number of diagonals (unique '
                                                    'participant assignments). '
                                                    'Defaults to the maximum level '
                                                    'count across all outer_factors. '
                                                    'Increase this to accommodate more '
                                                    'participants than the default '
                                                    'diagonal count.',
                                     'type': 'integer'},
                  'outer_factors': { 'description': 'Handle strings for the Factor '
                                                    'objects that form the outer grid '
                                                    'of the NestedBlock. Each string '
                                                    'must be a handle returned by a '
                                                    'prior Factor-creation tool call.',
                                     'items': {'type': 'string'},
                                     'type': 'array'},
                  'require_balanced_grid': { 'default': True,
                                             'description': 'When true (default), '
                                                            'prints a WARNING to '
                                                            'stdout if outer factors '
                                                            'have different numbers of '
                                                            'levels (rectangular '
                                                            'grid). Set to false to '
                                                            'suppress these warnings '
                                                            'when an unbalanced grid '
                                                            'is intentional.',
                                             'type': 'boolean'}},
  'required': ['outer_factors'],
  'type': 'object'}
TOOL_NOTES = "- `num_diagonals` defaults to `max(len(f.levels) for f in outer_factors)`, so the default participant capacity equals the largest factor's level count — explicitly set it if you need more participants.\n- Participant IDs passed to `synthesize_trials` wrap cyclically via `participant % num_participants`, so IDs beyond `num_diagonals - 1` silently repeat earlier diagonals.\n- LatinSquare adds no SAT/ILP clauses; the per-participant trial reduction happens in `synthesize_trials`, not at constraint-creation time.\n- `outer_factors` must be the *external* factors of the NestedBlock (i.e., listed in NestedBlock's `design` but not in the inner CrossBlock's design); passing inner-block factors raises a `ValueError` at NestedBlock validation time, not at LatinSquare construction time.\n- Balance warnings are printed to stdout, not raised as exceptions, so a misconfigured grid will not fail loudly unless you inspect stdout."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.LatinSquare
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
    def create_latin_square(args: dict[str, Any] | None = None) -> Any:
        'Call this tool before constructing a NestedBlock when you need Latin Square counterbalancing — i.e., when each participant should see only one diagonal slice of the outer factor grid rather than all combinations.'
        return _impl(args or {})
