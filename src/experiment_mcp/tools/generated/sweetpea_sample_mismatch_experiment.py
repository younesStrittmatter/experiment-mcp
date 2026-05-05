"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'f1f78e83837c8d5e22e5979954ccf6a31134819ddefe43d222960a715c4a4de2'
__exp_qualname__ = 'sweetpea.sample_mismatch_experiment'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'sample_mismatch_experiment'
TOOL_DESCRIPTION = 'Call this tool after synthesizing a trial sequence (e.g., via `sweetpea_synthesize_trials`) to validate that the sample satisfies the block\'s factors, constraints, and crossings. Returns an empty dict if the sample is fully valid; otherwise returns a dict with keys `"trial_count"`, `"factors"`, `"constraints"`, and/or `"crossings"` describing each category of mismatch.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for a SweetPea Block (produced by fully_cross_block or multiple_cross_block).",\n      "type": "string"\n    },\n    "sample": {\n      "additionalProperties": {\n        "items": {},\n        "type": "array"\n      },\n      "description": "Trial sequence to validate, as a dict mapping factor names (strings) to lists of level values \\u2014 the same shape returned by synthesize_trials.",\n      "type": "object"\n    }\n  },\n  "required": [\n    "block",\n    "sample"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturns an empty dict (no keys) when the sample is valid — treat an empty return as a pass. Mismatch categories are checked in order: trial_count first, then factors/constraints/crossings only if trial count matches. The docstring says `sample` is a list but the implementation treats it as a dict keyed by factor name; always pass the dict form returned by synthesize_trials.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for a SweetPea Block '
                                            '(produced by fully_cross_block or '
                                            'multiple_cross_block).',
                             'type': 'string'},
                  'sample': { 'additionalProperties': {'items': {}, 'type': 'array'},
                              'description': 'Trial sequence to validate, as a dict '
                                             'mapping factor names (strings) to lists '
                                             'of level values — the same shape '
                                             'returned by synthesize_trials.',
                              'type': 'object'}},
  'required': ['block', 'sample'],
  'type': 'object'}
TOOL_NOTES = 'Returns an empty dict (no keys) when the sample is valid — treat an empty return as a pass. Mismatch categories are checked in order: trial_count first, then factors/constraints/crossings only if trial count matches. The docstring says `sample` is a list but the implementation treats it as a dict keyed by factor name; always pass the dict form returned by synthesize_trials.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.sample_mismatch_experiment
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
    def sample_mismatch_experiment(args: dict[str, Any] | None = None) -> Any:
        "Call this tool after synthesizing a trial sequence (e.g., via `sweetpea_synthesize_trials`) to validate that the sample satisfies the block's factors, constraints, and crossings."
        return _impl(args or {})
