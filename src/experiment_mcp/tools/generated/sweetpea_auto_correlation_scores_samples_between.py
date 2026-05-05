"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '19215a678a68cd88a78d150aa06dc5f0bda489de387078913eed3b3369293702'
__exp_qualname__ = 'sweetpea.auto_correlation_scores_samples_between'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'auto_correlation_scores_samples_between'
TOOL_DESCRIPTION = 'Call this tool after generating multiple trial sequence samples (e.g., via `iterate_gen`, `iterate_sat_gen`, or `iterate_ilp_gen`) to measure how predictable each factor\'s levels are from preceding trials across the sample set. Returns a dict mapping each factor name to a scalar auto-correlation score (higher = more predictable / more sequentially biased); use it to compare designs or verify that a sampling method produces sufficiently counterbalanced sequences before wiring them into SweetBean.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "factor_names": {\n      "default": [],\n      "description": "Factors to evaluate. Pass an empty array (or omit) to evaluate all factors present in the samples.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "number_trials": {\n      "default": 10,\n      "description": "Maximum number of preceding trials to use as predictors. Silently clamped to half the sequence length if the sequences are short.",\n      "type": "integer"\n    },\n    "samples": {\n      "description": "List of trial sets, each produced by a SweetPea sampling call. Each trial set is an object mapping factor names (strings) to arrays of level values (strings or numbers), one entry per trial.",\n      "items": {\n        "additionalProperties": {\n          "items": {},\n          "type": "array"\n        },\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "starts": {\n      "default": 10,\n      "description": "Number of independent neural network restarts. The final score is the maximum across restarts; higher values improve reliability at the cost of compute time.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "samples"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `factor_names=[]` (the default empty list) silently means "test all factors" — passing an explicit empty list and passing nothing have the same effect.\n- The effective look-back window is `min(number_trials, len(sequence) // 2)`, so `number_trials` may be silently clamped for short sequences.\n- This is the **between**-samples variant: it trains a neural network across the full list of samples. For single-sample analysis use `auto_correlation_scores_sample_within`.\n- Scores are not normalized to a fixed [0, 1] range by the docstring — treat them as relative indicators rather than absolute probabilities.\n- Increasing `starts` beyond 10 can meaningfully stabilize noisy scores on small sample sets but has diminishing returns on large ones.'
TOOL_PARAMETERS = { 'properties': { 'factor_names': { 'default': [],
                                    'description': 'Factors to evaluate. Pass an empty '
                                                   'array (or omit) to evaluate all '
                                                   'factors present in the samples.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'number_trials': { 'default': 10,
                                     'description': 'Maximum number of preceding '
                                                    'trials to use as predictors. '
                                                    'Silently clamped to half the '
                                                    'sequence length if the sequences '
                                                    'are short.',
                                     'type': 'integer'},
                  'samples': { 'description': 'List of trial sets, each produced by a '
                                              'SweetPea sampling call. Each trial set '
                                              'is an object mapping factor names '
                                              '(strings) to arrays of level values '
                                              '(strings or numbers), one entry per '
                                              'trial.',
                               'items': { 'additionalProperties': { 'items': {},
                                                                    'type': 'array'},
                                          'type': 'object'},
                               'type': 'array'},
                  'starts': { 'default': 10,
                              'description': 'Number of independent neural network '
                                             'restarts. The final score is the maximum '
                                             'across restarts; higher values improve '
                                             'reliability at the cost of compute time.',
                              'type': 'integer'}},
  'required': ['samples'],
  'type': 'object'}
TOOL_NOTES = '- `factor_names=[]` (the default empty list) silently means "test all factors" — passing an explicit empty list and passing nothing have the same effect.\n- The effective look-back window is `min(number_trials, len(sequence) // 2)`, so `number_trials` may be silently clamped for short sequences.\n- This is the **between**-samples variant: it trains a neural network across the full list of samples. For single-sample analysis use `auto_correlation_scores_sample_within`.\n- Scores are not normalized to a fixed [0, 1] range by the docstring — treat them as relative indicators rather than absolute probabilities.\n- Increasing `starts` beyond 10 can meaningfully stabilize noisy scores on small sample sets but has diminishing returns on large ones.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.auto_correlation_scores_samples_between
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
    def auto_correlation_scores_samples_between(args: dict[str, Any] | None = None) -> Any:
        "Call this tool after generating multiple trial sequence samples (e.g., via `iterate_gen`, `iterate_sat_gen`, or `iterate_ilp_gen`) to measure how predictable each factor's levels are from preceding trials across the sample set."
        return _impl(args or {})
