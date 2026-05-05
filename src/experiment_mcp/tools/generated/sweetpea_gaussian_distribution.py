"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '67899fba218c6d5ff1af24196adf8de1aaafed415aa0850fcf9cfbfa69c25a86'
__exp_qualname__ = 'sweetpea.GaussianDistribution'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gaussian_distribution'
TOOL_DESCRIPTION = 'Call this tool when you need to attach a continuous Gaussian (normal) distribution to a SweetPea factor — for example, to randomize stimulus durations, inter-trial intervals, or any numeric level drawn from a bell curve rather than a fixed set of discrete values. The result is a GaussianDistribution object (returned as a handle string) that you pass as a level value when constructing a Factor with `sweetpea_factor`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "mean": {\n      "description": "The mean (center) of the Gaussian distribution. Units match whatever the factor represents (e.g., milliseconds for a duration factor).",\n      "type": "number"\n    },\n    "sigma": {\n      "description": "The standard deviation of the Gaussian distribution. Must be positive; controls the spread of sampled values around the mean.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "mean",\n    "sigma"\n  ],\n  "type": "object"\n}\n\nNotes:\nsigma must be positive — passing zero or a negative value will not raise an error at construction time but will produce degenerate or nonsensical samples at design-synthesis time. The distribution is sampled independently for each trial; there is no seeding or correlation control at this layer. If you need reproducible sequences, set `random.seed` in the enclosing script before calling SweetPea\'s synthesis functions, not here.'
TOOL_PARAMETERS = { 'properties': { 'mean': { 'description': 'The mean (center) of the Gaussian '
                                           'distribution. Units match whatever the '
                                           'factor represents (e.g., milliseconds for '
                                           'a duration factor).',
                            'type': 'number'},
                  'sigma': { 'description': 'The standard deviation of the Gaussian '
                                            'distribution. Must be positive; controls '
                                            'the spread of sampled values around the '
                                            'mean.',
                             'type': 'number'}},
  'required': ['mean', 'sigma'],
  'type': 'object'}
TOOL_NOTES = "sigma must be positive — passing zero or a negative value will not raise an error at construction time but will produce degenerate or nonsensical samples at design-synthesis time. The distribution is sampled independently for each trial; there is no seeding or correlation control at this layer. If you need reproducible sequences, set `random.seed` in the enclosing script before calling SweetPea's synthesis functions, not here."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.GaussianDistribution
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
    def create_gaussian_distribution(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to attach a continuous Gaussian (normal) distribution to a SweetPea factor — for example, to randomize stimulus durations, inter-trial intervals, or any numeric level drawn from a bell curve rather than a fixed set of discrete values.'
        return _impl(args or {})
