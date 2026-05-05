"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '07c92489729fd0bba58a7ca36a7e145bc77adb2367c3ae2673813e695d7117f7'
__exp_qualname__ = 'sweetpea.AtLeastKInARow'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_at_least_k_in_a_row'
TOOL_DESCRIPTION = 'Call this tool during the SweetPea design phase (step 1 of the pipeline, before sampling) to add a minimum-run-length constraint: whenever the specified level appears in the sampled trial sequence, it must appear in consecutive blocks of at least K trials. Pass the returned handle to `synthesize_trials` inside its `constraints` list alongside your crossing and other constraints.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "k": {\n      "description": "Minimum number of consecutive trials the level must appear when it occurs. Must be >= 1; k=1 is a no-op.",\n      "type": "integer"\n    },\n    "levels": {\n      "description": "Two-element array [factor_handle, level_name]. factor_handle is the handle string of a SweetPea Factor produced by a factor-creation tool; level_name is the string name of the level on that factor to constrain (e.g. \'red\').",\n      "items": {\n        "type": "string"\n      },\n      "maxItems": 2,\n      "minItems": 2,\n      "type": "array"\n    }\n  },\n  "required": [\n    "k",\n    "levels"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis constraint enforces a lower bound on run length only when the level appears — it does not force the level to appear at all. To guarantee both presence and run length, combine with an `Exclude` or crossing constraint. Large `k` values significantly increase the minimum sequence length needed to satisfy the constraint; if `synthesize_trials` times out or fails, reduce `k` or increase the trial count. Unlike `AtMostKInARow`, the internal `max_trials_required` is left as `None` and inferred at synthesis time — do not assume a fixed sequence length when using this constraint.'
TOOL_PARAMETERS = { 'properties': { 'k': { 'description': 'Minimum number of consecutive trials the '
                                        'level must appear when it occurs. Must be >= '
                                        '1; k=1 is a no-op.',
                         'type': 'integer'},
                  'levels': { 'description': 'Two-element array [factor_handle, '
                                             'level_name]. factor_handle is the handle '
                                             'string of a SweetPea Factor produced by '
                                             'a factor-creation tool; level_name is '
                                             'the string name of the level on that '
                                             "factor to constrain (e.g. 'red').",
                              'items': {'type': 'string'},
                              'maxItems': 2,
                              'minItems': 2,
                              'type': 'array'}},
  'required': ['k', 'levels'],
  'type': 'object'}
TOOL_NOTES = 'This constraint enforces a lower bound on run length only when the level appears — it does not force the level to appear at all. To guarantee both presence and run length, combine with an `Exclude` or crossing constraint. Large `k` values significantly increase the minimum sequence length needed to satisfy the constraint; if `synthesize_trials` times out or fails, reduce `k` or increase the trial count. Unlike `AtMostKInARow`, the internal `max_trials_required` is left as `None` and inferred at synthesis time — do not assume a fixed sequence length when using this constraint.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.AtLeastKInARow
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
    def create_at_least_k_in_a_row(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during the SweetPea design phase (step 1 of the pipeline, before sampling) to add a minimum-run-length constraint: whenever the specified level appears in the sampled trial sequence, it must appear in consecutive blocks of at least K trials.'
        return _impl(args or {})
