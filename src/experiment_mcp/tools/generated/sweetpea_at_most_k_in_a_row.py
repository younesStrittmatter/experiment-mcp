"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '8eee589dad3aacf75e0b1fa1a65edda4e239339e6acc3b1204b92ca1a651e8cf'
__exp_qualname__ = 'sweetpea.AtMostKInARow'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_at_most_k_in_a_row'
TOOL_DESCRIPTION = 'Call this tool during the SweetPea design phase (step 1 of the pipeline) when you want to constrain how many consecutive trials may show a particular factor level. Pass the returned constraint object — along with factors and crossings — to a block-creation tool (e.g. `sweetpea_fully_crossed_block` or `sweetpea_cross_block`). The constraint guarantees that no sliding window of k+1 consecutive trials contains the specified level more than k times.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "k": {\n      "description": "Maximum number of consecutive trials in which the specified level may appear. Must be >= 1.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "level": {\n      "description": "Two-element array identifying the constrained level: [factor_handle, level_name]. factor_handle is the handle string returned by the tool that created the Factor; level_name is the string name of the level within that factor.",\n      "items": {\n        "type": "string"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    }\n  },\n  "required": [\n    "k",\n    "level"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe constraint is applied as a set of sliding-window sums, each of size k+1, all required to be strictly less than k+1. This means exactly k consecutive occurrences are allowed; k+1 in a row is forbidden. The `level` array must be [factor_handle, level_name_string] — passing a raw Factor object instead of a handle string will cause a dispatch error. This constraint object is not usable standalone; it must be passed inside the `constraints` list of a block-creation call.'
TOOL_PARAMETERS = { 'properties': { 'k': { 'description': 'Maximum number of consecutive trials in which '
                                        'the specified level may appear. Must be >= 1.',
                         'minimum': 1,
                         'type': 'integer'},
                  'level': { 'description': 'Two-element array identifying the '
                                            'constrained level: [factor_handle, '
                                            'level_name]. factor_handle is the handle '
                                            'string returned by the tool that created '
                                            'the Factor; level_name is the string name '
                                            'of the level within that factor.',
                             'items': {'type': 'string'},
                             'maxItems': 2,
                             'minItems': 2,
                             'type': 'array'}},
  'required': ['k', 'level'],
  'type': 'object'}
TOOL_NOTES = 'The constraint is applied as a set of sliding-window sums, each of size k+1, all required to be strictly less than k+1. This means exactly k consecutive occurrences are allowed; k+1 in a row is forbidden. The `level` array must be [factor_handle, level_name_string] — passing a raw Factor object instead of a handle string will cause a dispatch error. This constraint object is not usable standalone; it must be passed inside the `constraints` list of a block-creation call.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.AtMostKInARow
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
    def create_at_most_k_in_a_row(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during the SweetPea design phase (step 1 of the pipeline) when you want to constrain how many consecutive trials may show a particular factor level.'
        return _impl(args or {})
