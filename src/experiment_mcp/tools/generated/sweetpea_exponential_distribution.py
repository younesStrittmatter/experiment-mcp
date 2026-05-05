"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'fa47db5a1ec194026f08bd84754cc55f51d25c5995f88d95a0a5834bfb671c90'
__exp_qualname__ = 'sweetpea.ExponentialDistribution'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_exponential_distribution'
TOOL_DESCRIPTION = 'Call this tool during SweetPea factor definition (step 1 of the pipeline) when a factor\'s level values should be drawn from a continuous exponential distribution — e.g., inter-stimulus intervals or reaction-time thresholds. Returns a handle to an ExponentialDistribution object that can be passed wherever SweetPea accepts a Distribution (e.g., as a factor\'s value generator).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "rate": {\n      "description": "Rate parameter (\\u03bb) of the exponential distribution. The mean of the resulting samples equals 1/rate. Must be positive.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "rate"\n  ],\n  "type": "object"\n}\n\nNotes:\nrate is the inverse of the mean, not the mean itself — passing rate=1.0 gives a mean sample of 1.0, but passing rate=0.1 gives a mean sample of 10.0. rate must be strictly positive; zero or negative values will cause Python\'s random.expovariate to raise ValueError at sample time, not at construction time.'
TOOL_PARAMETERS = { 'properties': { 'rate': { 'description': 'Rate parameter (λ) of the exponential '
                                           'distribution. The mean of the resulting '
                                           'samples equals 1/rate. Must be positive.',
                            'type': 'number'}},
  'required': ['rate'],
  'type': 'object'}
TOOL_NOTES = "rate is the inverse of the mean, not the mean itself — passing rate=1.0 gives a mean sample of 1.0, but passing rate=0.1 gives a mean sample of 10.0. rate must be strictly positive; zero or negative values will cause Python's random.expovariate to raise ValueError at sample time, not at construction time."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.ExponentialDistribution
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
    def create_exponential_distribution(args: dict[str, Any] | None = None) -> Any:
        "Call this tool during SweetPea factor definition (step 1 of the pipeline) when a factor's level values should be drawn from a continuous exponential distribution — e.g., inter-stimulus intervals or reaction-time thresholds."
        return _impl(args or {})
