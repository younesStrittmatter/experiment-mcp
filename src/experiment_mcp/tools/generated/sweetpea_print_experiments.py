"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '5facb2c7664434c7c325544c4b34d1dcd9b5148f278f4fe0bc701200ed4f6bef'
__exp_qualname__ = 'sweetpea.print_experiments'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'print_experiments'
TOOL_DESCRIPTION = 'Call this tool after `synthesize_trials` to render a trial sequence (or Latin Square multi-participant sequence) as human-readable text. Use it for debugging and inspection before passing the sequence to SweetBean — it shows factor levels per trial, grouped by experiment index and (for Latin Square designs) by participant ID. Output goes to stdout; it is not returned as a value.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the Block (e.g. CrossBlock) that produced the experiments. Must be the same block used with synthesize_trials.",\n      "type": "string"\n    },\n    "experiments": {\n      "description": "Handle string for the experiments returned by synthesize_trials. Accepts both standard List[dict] output and Latin Square Dict[int, List[dict]] output \\u2014 the tool detects the shape automatically.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "block",\n    "experiments"\n  ],\n  "type": "object"\n}\n\nNotes:\nOutput is written to stdout via print() — it is not returned to the agent. In an MCP server context the agent cannot read the printed output; use this only when stdout is observable (e.g. local dev / inspector session) or for side-effect logging. If you need to programmatically inspect the experiment data, use `experiments_to_dicts` or `experiments_to_tuples` instead. The block\'s continuous factors are mutated (restored) as a side effect before printing.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the Block (e.g. '
                                            'CrossBlock) that produced the '
                                            'experiments. Must be the same block used '
                                            'with synthesize_trials.',
                             'type': 'string'},
                  'experiments': { 'description': 'Handle string for the experiments '
                                                  'returned by synthesize_trials. '
                                                  'Accepts both standard List[dict] '
                                                  'output and Latin Square Dict[int, '
                                                  'List[dict]] output — the tool '
                                                  'detects the shape automatically.',
                                   'type': 'string'}},
  'required': ['block', 'experiments'],
  'type': 'object'}
TOOL_NOTES = "Output is written to stdout via print() — it is not returned to the agent. In an MCP server context the agent cannot read the printed output; use this only when stdout is observable (e.g. local dev / inspector session) or for side-effect logging. If you need to programmatically inspect the experiment data, use `experiments_to_dicts` or `experiments_to_tuples` instead. The block's continuous factors are mutated (restored) as a side effect before printing."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.print_experiments
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
    def print_experiments(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after `synthesize_trials` to render a trial sequence (or Latin Square multi-participant sequence) as human-readable text.'
        return _impl(args or {})
