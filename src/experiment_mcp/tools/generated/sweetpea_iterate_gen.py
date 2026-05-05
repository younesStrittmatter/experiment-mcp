"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'f779b20b5847c43cec2f93d276605770c5a7a0aea3ceea62457ff0ca7f2173df'
__exp_qualname__ = 'sweetpea.IterateGen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_iterate_gen'
TOOL_DESCRIPTION = 'Call this tool in the sampling phase of a SweetPea pipeline — after a Block has been constructed with `CrossBlock` or `MultiCrossBlock` — to draw one or more complete trial sequences from it. `IterateGen` automatically selects SAT-based sampling for blocks with complex factors or constraints, and faster random sampling otherwise; the result is a `SamplingResult` handle whose sequences are ready to pass into SweetBean stimulus/trial wiring.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the SweetPea Block to sample from (returned by CrossBlock, MultiCrossBlock, or similar block-construction tools).",\n      "type": "string"\n    },\n    "sample_count": {\n      "description": "Number of independent trial sequences to generate.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "block",\n    "sample_count"\n  ],\n  "type": "object"\n}\n\nNotes:\nIterateGen dispatches internally: blocks with complex factors or explicit constraints use the SAT solver (IterateSATGen), which is correct but can be slow for large sample_count values; simple blocks use RandomGen, which is fast. There is no option to override this dispatch — if you need to force a specific strategy, use IterateSATGen or RandomGen directly. The class exposes no constructor parameters; all meaningful arguments are on the static `sample` method. sample_count must be a positive integer; there is no built-in upper bound, so large values against SAT-heavy blocks may time out.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the SweetPea Block to '
                                            'sample from (returned by CrossBlock, '
                                            'MultiCrossBlock, or similar '
                                            'block-construction tools).',
                             'type': 'string'},
                  'sample_count': { 'description': 'Number of independent trial '
                                                   'sequences to generate.',
                                    'minimum': 1,
                                    'type': 'integer'}},
  'required': ['block', 'sample_count'],
  'type': 'object'}
TOOL_NOTES = 'IterateGen dispatches internally: blocks with complex factors or explicit constraints use the SAT solver (IterateSATGen), which is correct but can be slow for large sample_count values; simple blocks use RandomGen, which is fast. There is no option to override this dispatch — if you need to force a specific strategy, use IterateSATGen or RandomGen directly. The class exposes no constructor parameters; all meaningful arguments are on the static `sample` method. sample_count must be a positive integer; there is no built-in upper bound, so large values against SAT-heavy blocks may time out.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.IterateGen
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
    def create_iterate_gen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in the sampling phase of a SweetPea pipeline — after a Block has been constructed with `CrossBlock` or `MultiCrossBlock` — to draw one or more complete trial sequences from it.'
        return _impl(args or {})
