"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'acc525644a72ee8cedfd94b1c473c7130f0f4132dd628e964f4d99889f1d7564'
__exp_qualname__ = 'sweetpea.experiments_to_tuples'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'experiments_to_tuples'
TOOL_DESCRIPTION = 'Call this tool after synthesizing trials (via `sweetpea_synthesize_trials` or similar) to convert the raw experiment dicts into a compact tuple representation — one tuple per crossing per trial. Use it to inspect, log, or feed crossing-level combinations into downstream SweetBean stimulus wiring without carrying the full dict payload.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the Block object that defines the experimental design (returned by sweetpea_fully_cross_block or similar block-construction tool).",\n      "type": "string"\n    },\n    "experiments": {\n      "description": "List of experiment dicts as returned by synthesize_trials \\u2014 each dict maps factor names to lists of level-name strings, one entry per trial.",\n      "items": {\n        "additionalProperties": {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        "type": "object"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "block",\n    "experiments"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe return value is a list-of-lists-of-tuples: outer list indexes experiments, inner list indexes crossings within that experiment, each tuple contains the simple surface-level names for that crossing. Hidden factors (internal SweetPea bookkeeping factors) are stripped before building the tuples — the agent should not expect them to appear. The `experiments` argument must be the raw list-of-dicts structure from synthesize_trials, not a handle string.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the Block object that '
                                            'defines the experimental design (returned '
                                            'by sweetpea_fully_cross_block or similar '
                                            'block-construction tool).',
                             'type': 'string'},
                  'experiments': { 'description': 'List of experiment dicts as '
                                                  'returned by synthesize_trials — '
                                                  'each dict maps factor names to '
                                                  'lists of level-name strings, one '
                                                  'entry per trial.',
                                   'items': { 'additionalProperties': { 'items': { 'type': 'string'},
                                                                        'type': 'array'},
                                              'type': 'object'},
                                   'type': 'array'}},
  'required': ['block', 'experiments'],
  'type': 'object'}
TOOL_NOTES = 'The return value is a list-of-lists-of-tuples: outer list indexes experiments, inner list indexes crossings within that experiment, each tuple contains the simple surface-level names for that crossing. Hidden factors (internal SweetPea bookkeeping factors) are stripped before building the tuples — the agent should not expect them to appear. The `experiments` argument must be the raw list-of-dicts structure from synthesize_trials, not a handle string.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.experiments_to_tuples
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
    def experiments_to_tuples(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after synthesizing trials (via `sweetpea_synthesize_trials` or similar) to convert the raw experiment dicts into a compact tuple representation — one tuple per crossing per trial.'
        return _impl(args or {})
