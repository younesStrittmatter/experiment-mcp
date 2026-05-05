"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '8a5803a359238255735bc7d7ec86cfdf40e017bd1eb623264cea41a3c6884a98'
__exp_qualname__ = 'sweetpea.IterateILPGen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_iterate_ilp_gen'
TOOL_DESCRIPTION = 'Call this tool at step 2 of the SweetPea pipeline — after constructing a Block (via CrossBlock or similar) — when you need to sample multiple valid trial sequences using an iterative ILP solver. Pass the block handle and how many sequences you want; the tool returns a SamplingResult whose trial lists can be passed directly into SweetBean stimuli/trials for experiment construction.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the SweetPea Block (e.g. CrossBlock) produced by a prior tool. The runtime resolves this to the live Block object before dispatch.",\n      "type": "string"\n    },\n    "sample_count": {\n      "description": "Number of distinct trial sequences to generate. Each sequence satisfies all crossing and constraint requirements of the block.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "block",\n    "sample_count"\n  ],\n  "type": "object"\n}\n\nNotes:\nIf the block has validation errors, sampling silently returns an empty SamplingResult (no exception is raised) — verify the block is error-free before calling. The ILP solver enumerates solutions iteratively; requesting many sequences from a large, heavily-constrained design can be slow. IterateILPGen is stateless (all methods are static); instantiation carries no configuration options — there is currently no way to disable metrics or pass feature flags (per the TODO in the docstring).'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the SweetPea Block '
                                            '(e.g. CrossBlock) produced by a prior '
                                            'tool. The runtime resolves this to the '
                                            'live Block object before dispatch.',
                             'type': 'string'},
                  'sample_count': { 'description': 'Number of distinct trial sequences '
                                                   'to generate. Each sequence '
                                                   'satisfies all crossing and '
                                                   'constraint requirements of the '
                                                   'block.',
                                    'minimum': 1,
                                    'type': 'integer'}},
  'required': ['block', 'sample_count'],
  'type': 'object'}
TOOL_NOTES = 'If the block has validation errors, sampling silently returns an empty SamplingResult (no exception is raised) — verify the block is error-free before calling. The ILP solver enumerates solutions iteratively; requesting many sequences from a large, heavily-constrained design can be slow. IterateILPGen is stateless (all methods are static); instantiation carries no configuration options — there is currently no way to disable metrics or pass feature flags (per the TODO in the docstring).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.IterateILPGen
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
    def create_iterate_ilp_gen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at step 2 of the SweetPea pipeline — after constructing a Block (via CrossBlock or similar) — when you need to sample multiple valid trial sequences using an iterative ILP solver.'
        return _impl(args or {})
