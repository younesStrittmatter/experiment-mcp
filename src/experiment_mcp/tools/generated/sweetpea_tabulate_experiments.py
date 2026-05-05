"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'ea70e3cd58d7449138ecfcc4493e67d9a0965321ffe43db7b6db6884f7290939'
__exp_qualname__ = 'sweetpea.tabulate_experiments'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'tabulate_experiments'
TOOL_DESCRIPTION = 'Call this tool after `synthesize_trials` to inspect the frequency distribution of factor-level combinations across the sampled sequences. Use it to verify that the crossing constraints are satisfied before wiring trial sequences into SweetBean stimuli. The tool prints a human-readable table (absolute counts + percentages) to stdout for each experiment in the list; it returns nothing.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for a MultiCrossBlockRepeat with exactly one crossing. Used as an alternative source of factors when factors is not provided. Either block or factors is required.",\n      "type": "string"\n    },\n    "experiments": {\n      "description": "Handle strings for the experiment dicts produced by synthesize_trials (one handle per sequence).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "factors": {\n      "description": "Handle strings for the Factor objects whose combinations should appear in the table. Must be a subset of the design factors. Either factors or block is required.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "trials": {\n      "description": "Zero-based indices of trials to include in the tabulation. The same index list is applied to every sequence. Omit to include all trials.",\n      "items": {\n        "type": "integer"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "experiments"\n  ],\n  "type": "object"\n}\n\nNotes:\nAt least one of `factors` or `block` must be supplied; passing neither raises RuntimeError. If `block` is supplied instead of `factors`, it must be a MultiCrossBlockRepeat with exactly one crossing — any other block type raises RuntimeError. The function prints to stdout and returns None; the agent cannot programmatically inspect the table values. When `trials` is omitted the first call mutates the default (the function rebinds the local `trials` variable on the first experiment and reuses it for subsequent ones — all experiments see the same trial-index list, which is the full range derived from the first experiment).'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for a MultiCrossBlockRepeat '
                                            'with exactly one crossing. Used as an '
                                            'alternative source of factors when '
                                            'factors is not provided. Either block or '
                                            'factors is required.',
                             'type': 'string'},
                  'experiments': { 'description': 'Handle strings for the experiment '
                                                  'dicts produced by synthesize_trials '
                                                  '(one handle per sequence).',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'factors': { 'description': 'Handle strings for the Factor objects '
                                              'whose combinations should appear in the '
                                              'table. Must be a subset of the design '
                                              'factors. Either factors or block is '
                                              'required.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'trials': { 'description': 'Zero-based indices of trials to include '
                                             'in the tabulation. The same index list '
                                             'is applied to every sequence. Omit to '
                                             'include all trials.',
                              'items': {'type': 'integer'},
                              'type': 'array'}},
  'required': ['experiments'],
  'type': 'object'}
TOOL_NOTES = 'At least one of `factors` or `block` must be supplied; passing neither raises RuntimeError. If `block` is supplied instead of `factors`, it must be a MultiCrossBlockRepeat with exactly one crossing — any other block type raises RuntimeError. The function prints to stdout and returns None; the agent cannot programmatically inspect the table values. When `trials` is omitted the first call mutates the default (the function rebinds the local `trials` variable on the first experiment and reuses it for subsequent ones — all experiments see the same trial-index list, which is the full range derived from the first experiment).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.tabulate_experiments
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
    def tabulate_experiments(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after `synthesize_trials` to inspect the frequency distribution of factor-level combinations across the sampled sequences.'
        return _impl(args or {})
