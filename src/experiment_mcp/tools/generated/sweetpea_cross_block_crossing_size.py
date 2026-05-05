"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'd007becf54bc304da7f24cbdda1da10a59c32cce1d3f3831f3abbb7ebea3a73f'
__exp_qualname__ = 'sweetpea.CrossBlock.crossing_size'
__exp_kind__ = 'method'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'crossing_size'
TOOL_DESCRIPTION = 'Call this tool after creating a CrossBlock (via `sweetpea_cross_block`) to determine how many unique trial combinations exist in a given crossing, net of any exclusion constraints. Use this before sampling to anticipate sequence length or to validate design feasibility. Returns a non-negative integer.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "cross_block": {\n      "description": "Handle string for the CrossBlock instance, as returned by the sweetpea_cross_block tool.",\n      "type": "string"\n    },\n    "crossing": {\n      "description": "Optional list of Factor handle strings identifying which crossing to measure. Each handle must correspond to a Factor that belongs to one of the block\'s declared crossings. If omitted, defaults to the block\'s first (or only) crossing.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "cross_block"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `crossing` argument, when provided, must exactly match one of the crossings declared in the CrossBlock — passing an arbitrary subset of factors that was not declared as a crossing will raise an error. The returned count subtracts excluded trial combinations (those ruled out by `WithinTrial` exclusion constraints), so it may be smaller than the raw Cartesian product of factor levels. If the block has only one crossing, omitting `crossing` is safe and idiomatic.'
TOOL_PARAMETERS = { 'properties': { 'cross_block': { 'description': 'Handle string for the CrossBlock '
                                                  'instance, as returned by the '
                                                  'sweetpea_cross_block tool.',
                                   'type': 'string'},
                  'crossing': { 'description': 'Optional list of Factor handle strings '
                                               'identifying which crossing to measure. '
                                               'Each handle must correspond to a '
                                               'Factor that belongs to one of the '
                                               "block's declared crossings. If "
                                               "omitted, defaults to the block's first "
                                               '(or only) crossing.',
                                'items': {'type': 'string'},
                                'type': 'array'}},
  'required': ['cross_block'],
  'type': 'object'}
TOOL_NOTES = 'The `crossing` argument, when provided, must exactly match one of the crossings declared in the CrossBlock — passing an arbitrary subset of factors that was not declared as a crossing will raise an error. The returned count subtracts excluded trial combinations (those ruled out by `WithinTrial` exclusion constraints), so it may be smaller than the raw Cartesian product of factor levels. If the block has only one crossing, omitting `crossing` is safe and idiomatic.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = sp.CrossBlock
    resolved = handles.resolve_in(kwargs)
    instance = resolved.pop('cross_block', None)
    if instance is None:
        raise TypeError(
            f"{TOOL_NAME} requires kwarg 'cross_block' "
            f"(handle returned by create_cross_block)."
        )
    if not isinstance(instance, cls):
        raise TypeError(
            f"{TOOL_NAME} got 'cross_block'={type(instance).__name__}, "
            f"expected CrossBlock."
        )
    result = instance.crossing_size(**resolved)
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
    def crossing_size(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after creating a CrossBlock (via `sweetpea_cross_block`) to determine how many unique trial combinations exist in a given crossing, net of any exclusion constraints.'
        return _impl(args or {})
