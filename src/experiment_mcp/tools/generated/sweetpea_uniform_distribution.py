"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '7845170d8941096a2d7f7efa3a3364734124b32fc25cf73019219fc704b377d9'
__exp_qualname__ = 'sweetpea.UniformDistribution'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_uniform_distribution'
TOOL_DESCRIPTION = 'Call this tool when building a SweetPea factor whose level values should be drawn from a continuous uniform distribution over [low, high]. Use it at factor-definition time (step 1 of the pipeline, before crossing or sampling) to attach a stochastic draw to a numeric factor — e.g. stimulus duration, ISI, or jitter. Returns a UniformDistribution handle that can be passed as the `distribution` argument to a factor-construction tool.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "high": {\n      "description": "Upper bound of the uniform distribution (inclusive).",\n      "type": "number"\n    },\n    "low": {\n      "description": "Lower bound of the uniform distribution (inclusive).",\n      "type": "number"\n    }\n  },\n  "required": [\n    "low",\n    "high"\n  ],\n  "type": "object"\n}\n\nNotes:\nBoth bounds are passed directly to Python\'s `random.uniform(low, high)`, so the draw is inclusive on both ends. `low` must be strictly less than `high`; the class does not validate this — passing equal or reversed bounds will silently produce degenerate or negative-range samples. Units are whatever the consuming factor expects (milliseconds, degrees, etc.) — no unit conversion is applied.'
TOOL_PARAMETERS = { 'properties': { 'high': { 'description': 'Upper bound of the uniform distribution '
                                           '(inclusive).',
                            'type': 'number'},
                  'low': { 'description': 'Lower bound of the uniform distribution '
                                          '(inclusive).',
                           'type': 'number'}},
  'required': ['low', 'high'],
  'type': 'object'}
TOOL_NOTES = "Both bounds are passed directly to Python's `random.uniform(low, high)`, so the draw is inclusive on both ends. `low` must be strictly less than `high`; the class does not validate this — passing equal or reversed bounds will silently produce degenerate or negative-range samples. Units are whatever the consuming factor expects (milliseconds, degrees, etc.) — no unit conversion is applied."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.UniformDistribution
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
    def create_uniform_distribution(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when building a SweetPea factor whose level values should be drawn from a continuous uniform distribution over [low, high].'
        return _impl(args or {})
