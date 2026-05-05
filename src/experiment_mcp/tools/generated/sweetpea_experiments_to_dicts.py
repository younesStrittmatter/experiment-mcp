"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'b2be46b4923b8efbe85963f93c0a5add33581a30f3f8bff344889ca869e7d8df'
__exp_qualname__ = 'sweetpea.experiments_to_dicts'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'experiments_to_dicts'
TOOL_DESCRIPTION = 'Call this after `synthesize_trials` when you need the raw trial-sequence output converted into plain, human- and SweetBean-readable dicts — with hidden factors stripped and only surface-level level names retained. Returns a list-of-lists: outer index = experiment, inner index = crossing, leaf = `{factor_name: level_name}` dict. Use this as the bridge step before wiring SweetPea trial sequences into SweetBean stimuli or before inspecting / logging the sampled design.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the Block object that defines the experimental design (returned by sweetpea_fully_cross_block or sweetpea_multi_cross_block). Used to resolve factor names and filter hidden factors.",\n      "type": "string"\n    },\n    "experiments": {\n      "description": "Raw experiment output from synthesize_trials \\u2014 a list of dicts where keys are factor names and values are lists of level names, one entry per trial.",\n      "items": {\n        "additionalProperties": {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        "type": "object"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "block",\n    "experiments"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `experiments` argument must come directly from `synthesize_trials` (or equivalent synthesis functions like `synthesize_trials_uniform`); passing a re-shaped or hand-built dict will produce wrong output. Hidden factors (those not in the user-visible design) are silently dropped from the output — the returned dicts contain only the non-hidden factors in `block.design`. The outer list length equals `len(experiments)`; each inner list length equals the number of crossings in the block.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the Block object that '
                                            'defines the experimental design (returned '
                                            'by sweetpea_fully_cross_block or '
                                            'sweetpea_multi_cross_block). Used to '
                                            'resolve factor names and filter hidden '
                                            'factors.',
                             'type': 'string'},
                  'experiments': { 'description': 'Raw experiment output from '
                                                  'synthesize_trials — a list of dicts '
                                                  'where keys are factor names and '
                                                  'values are lists of level names, '
                                                  'one entry per trial.',
                                   'items': { 'additionalProperties': { 'items': { 'type': 'string'},
                                                                        'type': 'array'},
                                              'type': 'object'},
                                   'type': 'array'}},
  'required': ['block', 'experiments'],
  'type': 'object'}
TOOL_NOTES = 'The `experiments` argument must come directly from `synthesize_trials` (or equivalent synthesis functions like `synthesize_trials_uniform`); passing a re-shaped or hand-built dict will produce wrong output. Hidden factors (those not in the user-visible design) are silently dropped from the output — the returned dicts contain only the non-hidden factors in `block.design`. The outer list length equals `len(experiments)`; each inner list length equals the number of crossings in the block.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.experiments_to_dicts
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
    def experiments_to_dicts(args: dict[str, Any] | None = None) -> Any:
        'Call this after `synthesize_trials` when you need the raw trial-sequence output converted into plain, human- and SweetBean-readable dicts — with hidden factors stripped and only surface-level level names retained.'
        return _impl(args or {})
