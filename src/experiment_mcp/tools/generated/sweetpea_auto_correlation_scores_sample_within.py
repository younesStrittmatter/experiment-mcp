"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '9d5c793160f002eae75bfd9edc7a912265c2cb08faf8c7852aa251e6060800b2'
__exp_qualname__ = 'sweetpea.auto_correlation_scores_sample_within'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'auto_correlation_scores_sample_within'
TOOL_DESCRIPTION = 'Call this tool after sampling a trial sequence (e.g., via `sweetpea_gen` or `sweetpea_random_gen`) to check whether any factor\'s level can be predicted from preceding trials — a measure of unwanted serial autocorrelation. A score near 0 means the factor is well-randomized; a high score signals that the sequence has detectable order patterns an agent or participant could exploit. Returns a dict mapping each tested factor name to its predictability score.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "factor_names": {\n      "default": [],\n      "description": "Subset of factor names from `sample` to test. Omit or pass an empty list to test all factors.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "number_trials": {\n      "default": 10,\n      "description": "Maximum number of preceding trials to use as predictors. Effective value is clamped to half the sequence length.",\n      "type": "integer"\n    },\n    "sample": {\n      "additionalProperties": {\n        "items": {},\n        "type": "array"\n      },\n      "description": "A dict mapping each factor name (string) to a list of level values (one per trial), as returned by a SweetPea sampling tool such as sweetpea_gen.",\n      "type": "object"\n    },\n    "starts": {\n      "default": 10,\n      "description": "Number of independently initialized neural networks to train. The reported score is the maximum across all runs, so higher values give a more conservative (pessimistic) estimate of predictability.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "sample"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe effective look-back window is `min(number_trials, len(sequence) // 2)`, so very short sequences reduce sensitivity regardless of `number_trials`. The score is the *maximum* over `starts` networks, not the average — it reflects the worst-case predictability discovered. Empty `factor_names` (the default) tests every key in `sample`. The neural-network training is non-deterministic; results may vary slightly across runs even with the same inputs.'
TOOL_PARAMETERS = { 'properties': { 'factor_names': { 'default': [],
                                    'description': 'Subset of factor names from '
                                                   '`sample` to test. Omit or pass an '
                                                   'empty list to test all factors.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'number_trials': { 'default': 10,
                                     'description': 'Maximum number of preceding '
                                                    'trials to use as predictors. '
                                                    'Effective value is clamped to '
                                                    'half the sequence length.',
                                     'type': 'integer'},
                  'sample': { 'additionalProperties': {'items': {}, 'type': 'array'},
                              'description': 'A dict mapping each factor name (string) '
                                             'to a list of level values (one per '
                                             'trial), as returned by a SweetPea '
                                             'sampling tool such as sweetpea_gen.',
                              'type': 'object'},
                  'starts': { 'default': 10,
                              'description': 'Number of independently initialized '
                                             'neural networks to train. The reported '
                                             'score is the maximum across all runs, so '
                                             'higher values give a more conservative '
                                             '(pessimistic) estimate of '
                                             'predictability.',
                              'type': 'integer'}},
  'required': ['sample'],
  'type': 'object'}
TOOL_NOTES = 'The effective look-back window is `min(number_trials, len(sequence) // 2)`, so very short sequences reduce sensitivity regardless of `number_trials`. The score is the *maximum* over `starts` networks, not the average — it reflects the worst-case predictability discovered. Empty `factor_names` (the default) tests every key in `sample`. The neural-network training is non-deterministic; results may vary slightly across runs even with the same inputs.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.auto_correlation_scores_sample_within
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
    def auto_correlation_scores_sample_within(args: dict[str, Any] | None = None) -> Any:
        "Call this tool after sampling a trial sequence (e.g., via `sweetpea_gen` or `sweetpea_random_gen`) to check whether any factor's level can be predicted from preceding trials — a measure of unwanted serial autocorrelation."
        return _impl(args or {})
