"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '92822cf0f9737db2804ccbdd09c10812357c260c0a64c8288eec1efd3a1438f6'
__exp_qualname__ = 'sweetpea.ContinuousConstraint'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_continuous_constraint'
TOOL_DESCRIPTION = 'Call this tool during SweetPea design setup — after declaring ContinuousFactor objects but before calling `sweetpea_experiment_compile` — to attach a filtering predicate that rejects sampled continuous-factor combinations violating a constraint. The tool returns a handle to a ContinuousConstraint object that must be passed in the `constraints` list when constructing an Experiment or CrossBlock.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "constraint_function": {\n      "description": "Handle string pointing to a Python callable registered in the handle registry. The callable must accept exactly as many positional arguments as there are entries in `factors` and return a truthy value when the sampled combination is acceptable.",\n      "type": "string"\n    },\n    "factors": {\n      "description": "Ordered list of handle strings, each pointing to a ContinuousFactor object produced by a prior sweetpea_continuous_factor call. The constraint function will receive values in this same order.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "factors",\n    "constraint_function"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe constraint function is only evaluated during continuous sampling — it has no effect on combinatorial (discrete) CrossBlock designs. The number of parameters in the callable must exactly match the length of `factors`; a mismatch raises RuntimeError at validate-time, not at construction. Because JSON cannot represent Python callables, `constraint_function` must be a handle to a pre-registered callable; passing a raw lambda or function expression string will fail. All entries in `factors` must also appear in the `continuous_factors` list of the Block this constraint is attached to, otherwise validation raises RuntimeError.'
TOOL_PARAMETERS = { 'properties': { 'constraint_function': { 'description': 'Handle string pointing to a '
                                                          'Python callable registered '
                                                          'in the handle registry. The '
                                                          'callable must accept '
                                                          'exactly as many positional '
                                                          'arguments as there are '
                                                          'entries in `factors` and '
                                                          'return a truthy value when '
                                                          'the sampled combination is '
                                                          'acceptable.',
                                           'type': 'string'},
                  'factors': { 'description': 'Ordered list of handle strings, each '
                                              'pointing to a ContinuousFactor object '
                                              'produced by a prior '
                                              'sweetpea_continuous_factor call. The '
                                              'constraint function will receive values '
                                              'in this same order.',
                               'items': {'type': 'string'},
                               'type': 'array'}},
  'required': ['factors', 'constraint_function'],
  'type': 'object'}
TOOL_NOTES = 'The constraint function is only evaluated during continuous sampling — it has no effect on combinatorial (discrete) CrossBlock designs. The number of parameters in the callable must exactly match the length of `factors`; a mismatch raises RuntimeError at validate-time, not at construction. Because JSON cannot represent Python callables, `constraint_function` must be a handle to a pre-registered callable; passing a raw lambda or function expression string will fail. All entries in `factors` must also appear in the `continuous_factors` list of the Block this constraint is attached to, otherwise validation raises RuntimeError.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.ContinuousConstraint
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
    def create_continuous_constraint(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during SweetPea design setup — after declaring ContinuousFactor objects but before calling `sweetpea_experiment_compile` — to attach a filtering predicate that rejects sampled continuous-factor combinations violating a constraint.'
        return _impl(args or {})
