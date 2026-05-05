"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '6ea16e8e8c069db5df854f83dad84fcc5fe503500bee547e5ed680538d7d0968'
__exp_qualname__ = 'sweetpea.UniformGen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_uniform_gen'
TOOL_DESCRIPTION = 'Call this tool after defining a SweetPea block (CrossBlock, MultiCrossBlock, etc.) to sample one or more trial sequences from it. UniformGen automatically selects the optimal sampling strategy — uniform enumeration for simple blocks, SAT-based sampling for blocks with complex factors or constraints — so it is the right default sampler when the agent does not need to force a specific strategy. The result is a SamplingResult handle containing the sampled trial sequences, ready to be passed to SweetBean stimulus/trial constructors in the next pipeline step.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string referencing a SweetPea Block object (e.g. the return value of a CrossBlock or MultiCrossBlock tool call). The runtime resolves this to the live Block before dispatch.",\n      "type": "string"\n    },\n    "sample_count": {\n      "description": "Number of independent trial sequences to sample from the block.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "block",\n    "sample_count"\n  ],\n  "type": "object"\n}\n\nNotes:\nUniformGen silently dispatches to UniGen (uniform exhaustive enumeration) when the block has no complex factors or constraints, and to RandomGen (random sampling) otherwise — the agent cannot override this routing. If you need to force a specific strategy, use the Sweetpea UniGen, SweetpeaRandomGen, or SweetpeaIterateGen tools directly. The returned SamplingResult is a handle; pass it to SweetBean wiring tools rather than inspecting it raw.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string referencing a SweetPea '
                                            'Block object (e.g. the return value of a '
                                            'CrossBlock or MultiCrossBlock tool call). '
                                            'The runtime resolves this to the live '
                                            'Block before dispatch.',
                             'type': 'string'},
                  'sample_count': { 'description': 'Number of independent trial '
                                                   'sequences to sample from the '
                                                   'block.',
                                    'minimum': 1,
                                    'type': 'integer'}},
  'required': ['block', 'sample_count'],
  'type': 'object'}
TOOL_NOTES = 'UniformGen silently dispatches to UniGen (uniform exhaustive enumeration) when the block has no complex factors or constraints, and to RandomGen (random sampling) otherwise — the agent cannot override this routing. If you need to force a specific strategy, use the Sweetpea UniGen, SweetpeaRandomGen, or SweetpeaIterateGen tools directly. The returned SamplingResult is a handle; pass it to SweetBean wiring tools rather than inspecting it raw.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.UniformGen
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
    def create_uniform_gen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after defining a SweetPea block (CrossBlock, MultiCrossBlock, etc.) to sample one or more trial sequences from it.'
        return _impl(args or {})
