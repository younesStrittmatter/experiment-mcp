"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '87f5dd5abfbd5e4cbfd718464a244672c9523f14069df226cf1e44fa6c590b23'
__exp_qualname__ = 'sweetpea.WithinTrial'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_within_trial'
TOOL_DESCRIPTION = 'Call this tool when defining a derived factor whose level depends on the levels of other factors within the same trial (not across trials). Use it during the SweetPea design phase — before calling a gen tool — to pass as the `window` argument when constructing a derived Factor. The result is a WithinTrial window object (returned as a handle string) that encodes a same-trial predicate over one or more existing factors.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "factors": {\n      "description": "Ordered list of handle strings for the Factor objects this derivation depends on, in the same positional order as the predicate\'s arguments. Each handle was returned by a prior sweetpea_factor tool call.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "predicate": {\n      "description": "A Python lambda expression string (e.g. \\"lambda color, shape: color == \'red\' and shape == \'circle\'\\") that accepts one string argument per factor in `factors` (the level name of each factor) and returns a bool. The runtime evaluates this string to produce the callable passed to WithinTrial.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "predicate",\n    "factors"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `width`, `stride`, and `start` are hard-coded to 1, 1, and None respectively — they are NOT init parameters and cannot be overridden.\n- The predicate receives level **names** (strings), not level objects; compare against the string values you used when defining levels.\n- The positional order of arguments in the predicate lambda must exactly match the order of handles in `factors`.\n- `WithinTrial` is a window, not a Factor itself; pass the resulting handle as the `window` argument to a derived Factor (sweetpea_factor tool), not directly to a crossing or block tool.\n- Contrast with `Transition`: use `WithinTrial` when the derivation is purely within one trial; use `Transition` when it must look at the previous trial\'s levels.'
TOOL_PARAMETERS = { 'properties': { 'factors': { 'description': 'Ordered list of handle strings for the '
                                              'Factor objects this derivation depends '
                                              'on, in the same positional order as the '
                                              "predicate's arguments. Each handle was "
                                              'returned by a prior sweetpea_factor '
                                              'tool call.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'predicate': { 'description': 'A Python lambda expression string '
                                                '(e.g. "lambda color, shape: color == '
                                                '\'red\' and shape == \'circle\'") '
                                                'that accepts one string argument per '
                                                'factor in `factors` (the level name '
                                                'of each factor) and returns a bool. '
                                                'The runtime evaluates this string to '
                                                'produce the callable passed to '
                                                'WithinTrial.',
                                 'type': 'string'}},
  'required': ['predicate', 'factors'],
  'type': 'object'}
TOOL_NOTES = "- `width`, `stride`, and `start` are hard-coded to 1, 1, and None respectively — they are NOT init parameters and cannot be overridden.\n- The predicate receives level **names** (strings), not level objects; compare against the string values you used when defining levels.\n- The positional order of arguments in the predicate lambda must exactly match the order of handles in `factors`.\n- `WithinTrial` is a window, not a Factor itself; pass the resulting handle as the `window` argument to a derived Factor (sweetpea_factor tool), not directly to a crossing or block tool.\n- Contrast with `Transition`: use `WithinTrial` when the derivation is purely within one trial; use `Transition` when it must look at the previous trial's levels."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.WithinTrial
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
    def create_within_trial(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when defining a derived factor whose level depends on the levels of other factors within the same trial (not across trials).'
        return _impl(args or {})
