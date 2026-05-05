"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'a60b9469e5ff93b21ee3965dc2a42bcc70037859d60f3f15c39a70eb66f54db6'
__exp_qualname__ = 'sweetpea.LogNormalDistribution'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_log_normal_distribution'
TOOL_DESCRIPTION = 'Call this tool when you need a log-normal distribution object to assign to a continuous SweetPea factor (e.g., stimulus onset asynchrony, reaction time, inter-trial interval). Use it at the factor-definition stage of the pipeline — before crossing factors or sampling sequences — whenever the factor\'s values should be strictly positive and right-skewed. Returns a handle string representing a `LogNormalDistribution` instance that can be passed as the distribution argument to factor-creation tools.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "mean": {\n      "description": "Mean of the underlying normal distribution (i.e., log-space mean, not the arithmetic mean of the resulting samples). Positive or negative float.",\n      "type": "number"\n    },\n    "sigma": {\n      "description": "Standard deviation of the underlying normal distribution (log-space sigma). Must be positive; larger values produce heavier right tails.",\n      "type": "number"\n    }\n  },\n  "required": [\n    "mean",\n    "sigma"\n  ],\n  "type": "object"\n}\n\nNotes:\n`mean` and `sigma` parameterize the *underlying* normal distribution, not the log-normal moments. For example, to target a median of 500 ms set mean=log(0.5) ≈ −0.693 (if working in seconds) or mean=log(500) ≈ 6.215 (if working in milliseconds). There is no input validation in the constructor — passing sigma ≤ 0 will not raise immediately but will cause `random.lognormvariate` to produce nonsensical or error results at sample time. No units are enforced; the agent must keep units consistent with downstream SweetBean stimulus/timing parameters.'
TOOL_PARAMETERS = { 'properties': { 'mean': { 'description': 'Mean of the underlying normal distribution '
                                           '(i.e., log-space mean, not the arithmetic '
                                           'mean of the resulting samples). Positive '
                                           'or negative float.',
                            'type': 'number'},
                  'sigma': { 'description': 'Standard deviation of the underlying '
                                            'normal distribution (log-space sigma). '
                                            'Must be positive; larger values produce '
                                            'heavier right tails.',
                             'type': 'number'}},
  'required': ['mean', 'sigma'],
  'type': 'object'}
TOOL_NOTES = '`mean` and `sigma` parameterize the *underlying* normal distribution, not the log-normal moments. For example, to target a median of 500 ms set mean=log(0.5) ≈ −0.693 (if working in seconds) or mean=log(500) ≈ 6.215 (if working in milliseconds). There is no input validation in the constructor — passing sigma ≤ 0 will not raise immediately but will cause `random.lognormvariate` to produce nonsensical or error results at sample time. No units are enforced; the agent must keep units consistent with downstream SweetBean stimulus/timing parameters.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.LogNormalDistribution
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
    def create_log_normal_distribution(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need a log-normal distribution object to assign to a continuous SweetPea factor (e.g., stimulus onset asynchrony, reaction time, inter-trial interval).'
        return _impl(args or {})
