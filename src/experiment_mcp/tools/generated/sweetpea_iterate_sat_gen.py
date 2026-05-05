"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '3f7cedc042f39be12d15d9dc5d6801db9b7bc1a27dd306723ddc78640c725782'
__exp_qualname__ = 'sweetpea.IterateSATGen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_iterate_sat_gen'
TOOL_DESCRIPTION = 'Use this tool to create an IterateSATGen sampling-strategy handle at the strategy-selection step of the SweetPea pipeline — after declaring factors and crossings (e.g. via CrossBlock) but before calling synthesize_trials. Pass the returned handle as the sampling_strategy argument to a synthesis tool. IterateSATGen drives SAT-based iteration to produce trial sequences; it is the non-uniform alternative to UnigenGen and is the default strategy for most experimental designs.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nIterateSATGen takes no constructor arguments — the sample_count that controls how many sequences are drawn is supplied later by the synthesis tool (e.g. synthesize_trials), not here. Sampling is non-uniform (iterates SAT solutions via pycryptosat/pycmsgen); if your design requires uniform sampling, use UnigenGen instead. Silent errors: if the block has constraint violations, sample() returns an empty SamplingResult rather than raising — check that the block is valid before requesting synthesis.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'IterateSATGen takes no constructor arguments — the sample_count that controls how many sequences are drawn is supplied later by the synthesis tool (e.g. synthesize_trials), not here. Sampling is non-uniform (iterates SAT solutions via pycryptosat/pycmsgen); if your design requires uniform sampling, use UnigenGen instead. Silent errors: if the block has constraint violations, sample() returns an empty SamplingResult rather than raising — check that the block is valid before requesting synthesis.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.IterateSATGen
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
    def create_iterate_sat_gen(args: dict[str, Any] | None = None) -> Any:
        'Use this tool to create an IterateSATGen sampling-strategy handle at the strategy-selection step of the SweetPea pipeline — after declaring factors and crossings (e.g.'
        return _impl(args or {})
