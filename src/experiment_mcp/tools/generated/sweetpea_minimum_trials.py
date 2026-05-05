"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '79844790c82508d512701191de8212f47359cea26f6efe7931dc4c2ce9a4c64a'
__exp_qualname__ = 'sweetpea.MinimumTrials'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_minimum_trials'
TOOL_DESCRIPTION = 'Call this tool during SweetPea design setup (before block creation) when the fully-crossed design produces fewer trials than your experiment requires — e.g., for statistical power or counterbalancing goals. It returns a constraint handle that you pass into a block-creation tool (such as `sweetpea_cross_block`) alongside other constraints; at synthesis time, SweetPea will pad the sequence so the block contains at least `trials` total trials. If the block already carries a higher minimum from another constraint, the larger value wins.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "trials": {\n      "description": "Minimum number of trials the block must contain. Must be a positive integer. If the block already has a minimum trial count set by another constraint, the larger of the two values is used.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "trials"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `trials` argument is checked to be an `int` at construction time — passing a float (e.g. `100.0`) will raise a TypeError even though the value looks valid. The `validate` method has an `and` condition (`<= 0 and not isinstance(int)`) that means non-positive integers technically pass validation at validate-time while being rejected at construction-time by `argcheck`; rely on the constructor check, not the validator. Returns a constraint object (handle string); it has no effect until passed to a block-creation call.'
TOOL_PARAMETERS = { 'properties': { 'trials': { 'description': 'Minimum number of trials the block must '
                                             'contain. Must be a positive integer. If '
                                             'the block already has a minimum trial '
                                             'count set by another constraint, the '
                                             'larger of the two values is used.',
                              'type': 'integer'}},
  'required': ['trials'],
  'type': 'object'}
TOOL_NOTES = 'The `trials` argument is checked to be an `int` at construction time — passing a float (e.g. `100.0`) will raise a TypeError even though the value looks valid. The `validate` method has an `and` condition (`<= 0 and not isinstance(int)`) that means non-positive integers technically pass validation at validate-time while being rejected at construction-time by `argcheck`; rely on the constructor check, not the validator. Returns a constraint object (handle string); it has no effect until passed to a block-creation call.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.MinimumTrials
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
    def create_minimum_trials(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during SweetPea design setup (before block creation) when the fully-crossed design produces fewer trials than your experiment requires — e.g., for statistical power or counterbalancing goals.'
        return _impl(args or {})
