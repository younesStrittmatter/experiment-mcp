"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '5757f911af5f686c76ade4d4af5b4431d0839fc5b9077a3569762530b5a2e1af'
__exp_qualname__ = 'sweetpea.Gen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gen'
TOOL_DESCRIPTION = 'Call this tool in step 2 of the SweetPea pipeline — after a Block has been built with `CrossBlock` (or similar) — to draw one or more concrete trial sequences from the design. Returns a `SamplingResult` (a handle string) containing the sampled sequences as lists of dicts mapping factor names to level labels; pass the result to SweetBean stimulus/trial wiring or inspect it directly with `experiment_to_csv`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string referencing the SweetPea Block to sample from (returned by CrossBlock, MultiCrossBlock, or similar block-construction tools).",\n      "type": "string"\n    },\n    "sample_count": {\n      "description": "Number of independent trial sequences to generate. Each sequence satisfies the full crossing and constraint set; most single-experiment uses pass 1.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "block",\n    "sample_count"\n  ],\n  "type": "object"\n}\n\nNotes:\n`Gen` is an abstract base class; the runtime dispatches to a concrete strategy (e.g. `Iterate`, `CMSGen`, `UnigenGen`, `RandomGen`) selected by environment or block type — the agent does not choose the strategy through this tool. Transition factors and other complex-window factors produce empty-string entries (`\'\'`) in the dict for trials where the factor does not apply (e.g. the first trial of a transition). `sample_count > 1` is useful for power analysis but multiplies solve time linearly; for interactive use keep it at 1.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string referencing the SweetPea '
                                            'Block to sample from (returned by '
                                            'CrossBlock, MultiCrossBlock, or similar '
                                            'block-construction tools).',
                             'type': 'string'},
                  'sample_count': { 'description': 'Number of independent trial '
                                                   'sequences to generate. Each '
                                                   'sequence satisfies the full '
                                                   'crossing and constraint set; most '
                                                   'single-experiment uses pass 1.',
                                    'minimum': 1,
                                    'type': 'integer'}},
  'required': ['block', 'sample_count'],
  'type': 'object'}
TOOL_NOTES = "`Gen` is an abstract base class; the runtime dispatches to a concrete strategy (e.g. `Iterate`, `CMSGen`, `UnigenGen`, `RandomGen`) selected by environment or block type — the agent does not choose the strategy through this tool. Transition factors and other complex-window factors produce empty-string entries (`''`) in the dict for trials where the factor does not apply (e.g. the first trial of a transition). `sample_count > 1` is useful for power analysis but multiplies solve time linearly; for interactive use keep it at 1."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Gen
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
    def create_gen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 2 of the SweetPea pipeline — after a Block has been built with `CrossBlock` (or similar) — to draw one or more concrete trial sequences from the design.'
        return _impl(args or {})
