"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'b5cec82232530861ef8ddacad54e9371fdba050836a8841f4ad80a6fd7d37e91'
__exp_qualname__ = 'sweetpea.NestedBlock'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_nested_block'
TOOL_DESCRIPTION = 'Call this tool when you need a hierarchical (nested) experimental block where an inner block (e.g., a CrossBlock of within-block factors) repeats across levels of one or more external (between-block) factors. Use it during SweetPea design declaration — before calling `gen`, `iterate_gen`, or `iterate_sat_gen` — whenever your design has a mini-block structure that must tile across outer conditions. Returns a NestedBlock handle you pass directly to the sequence-generation tools.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "constraints": {\n      "default": [],\n      "description": "Optional list of Constraint handle strings (e.g., MinimumTrials, Exclude) to apply at the outer level.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "crossing": {\n      "description": "Handle strings for what to counterbalance at the outer level. Pass Factor handles to cross external factors across inner-block windows (nested mode). Pass the inner Block handle here \\u2014 in addition to any external Factor handles \\u2014 to enable permuted mode, which exhausts all orderings of the inner crossing.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "design": {\n      "description": "Handle strings for the components of this level\'s design. Must contain exactly one Block handle (the inner block) plus zero or more Factor handles for external (between-block) variables. Order does not matter but exactly one Block is required.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "num_permutations": {\n      "description": "Only valid in permuted mode (inner Block handle present in `crossing`). Limits how many of the inner crossing\'s orderings are used. Must be between 1 and factorial(inner_crossing_size). Omit to use all permutations.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "design",\n    "crossing"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `design` must contain exactly one Block handle; passing zero or more than one raises ValueError.\n- Every Factor handle in `crossing` must also appear in `design`; omitting one raises ValueError.\n- `num_permutations` is only accepted when the inner Block handle is listed in `crossing` (permuted mode); using it in nested mode raises ValueError.\n- In permuted mode the inner block must itself have exactly one crossing, otherwise ValueError is raised.\n- In nested mode the minimum trial count is automatically computed as (preamble of outer derived factors) + (product of outer level weights) × (inner block\'s trials_per_sample). You do not need to add a MinimumTrials constraint yourself unless you want a higher value.\n- In permuted mode a hidden `order` Factor is injected into the design; it will appear in the synthesized trial table but carries no semantic meaning for downstream SweetBean wiring.\n- Pass the returned NestedBlock handle as the `block` argument to `gen`, `iterate_gen`, `iterate_sat_gen`, or `iterate_ilp_gen`.'
TOOL_PARAMETERS = { 'properties': { 'constraints': { 'default': [],
                                   'description': 'Optional list of Constraint handle '
                                                  'strings (e.g., MinimumTrials, '
                                                  'Exclude) to apply at the outer '
                                                  'level.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'crossing': { 'description': 'Handle strings for what to '
                                               'counterbalance at the outer level. '
                                               'Pass Factor handles to cross external '
                                               'factors across inner-block windows '
                                               '(nested mode). Pass the inner Block '
                                               'handle here — in addition to any '
                                               'external Factor handles — to enable '
                                               'permuted mode, which exhausts all '
                                               'orderings of the inner crossing.',
                                'items': {'type': 'string'},
                                'type': 'array'},
                  'design': { 'description': 'Handle strings for the components of '
                                             "this level's design. Must contain "
                                             'exactly one Block handle (the inner '
                                             'block) plus zero or more Factor handles '
                                             'for external (between-block) variables. '
                                             'Order does not matter but exactly one '
                                             'Block is required.',
                              'items': {'type': 'string'},
                              'type': 'array'},
                  'num_permutations': { 'description': 'Only valid in permuted mode '
                                                       '(inner Block handle present in '
                                                       '`crossing`). Limits how many '
                                                       "of the inner crossing's "
                                                       'orderings are used. Must be '
                                                       'between 1 and '
                                                       'factorial(inner_crossing_size). '
                                                       'Omit to use all permutations.',
                                        'type': 'integer'}},
  'required': ['design', 'crossing'],
  'type': 'object'}
TOOL_NOTES = "- `design` must contain exactly one Block handle; passing zero or more than one raises ValueError.\n- Every Factor handle in `crossing` must also appear in `design`; omitting one raises ValueError.\n- `num_permutations` is only accepted when the inner Block handle is listed in `crossing` (permuted mode); using it in nested mode raises ValueError.\n- In permuted mode the inner block must itself have exactly one crossing, otherwise ValueError is raised.\n- In nested mode the minimum trial count is automatically computed as (preamble of outer derived factors) + (product of outer level weights) × (inner block's trials_per_sample). You do not need to add a MinimumTrials constraint yourself unless you want a higher value.\n- In permuted mode a hidden `order` Factor is injected into the design; it will appear in the synthesized trial table but carries no semantic meaning for downstream SweetBean wiring.\n- Pass the returned NestedBlock handle as the `block` argument to `gen`, `iterate_gen`, `iterate_sat_gen`, or `iterate_ilp_gen`."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.NestedBlock
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
    def create_nested_block(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need a hierarchical (nested) experimental block where an inner block (e.g., a CrossBlock of within-block factors) repeats across levels of one or more external (between-block) factors.'
        return _impl(args or {})
