"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'e6ca0fcaa3029ed87df2a9e00b166466abdfca69b1c493d2708642b0dc069d6f'
__exp_qualname__ = 'sweetpea.ExactlyK'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_exactly_k'
TOOL_DESCRIPTION = 'Call this tool during the SweetPea design phase (step 1) when you need to enforce that a specific factor level appears in a trial sequence exactly `k` times — no more, no less. Pass the returned constraint object (a handle string) into the `constraints` list of a block-builder tool such as `sweetpea_fully_cross_block` or `sweetpea_multiple_cross_block`. The constraint is silently skipped for any trial in which the level is absent.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "k": {\n      "description": "The exact number of times the constrained level must appear across the trial sequence (or within each window if within_block is true).",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "within_block": {\n      "default": false,\n      "description": "When true, the count of k is enforced within each crossing block window rather than globally across the full sequence. Defaults to false.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "k"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe constraint object produced here must be added to the `constraints` argument of a block-builder call — it does nothing on its own. The target level (Factor + Level pair) is bound at block-build time, not at construction time, so this tool only sets the `k` and `within_block` parameters. If the level never appears in the design, the constraint is silently satisfied; it does not force the level into the design. Using `within_block=true` subdivides the variable list into fixed-length windows equal to the crossing\'s trial count, which can produce unexpected SAT conflicts if `k` exceeds the window size.'
TOOL_PARAMETERS = { 'properties': { 'k': { 'description': 'The exact number of times the constrained '
                                        'level must appear across the trial sequence '
                                        '(or within each window if within_block is '
                                        'true).',
                         'minimum': 1,
                         'type': 'integer'},
                  'within_block': { 'default': False,
                                    'description': 'When true, the count of k is '
                                                   'enforced within each crossing '
                                                   'block window rather than globally '
                                                   'across the full sequence. Defaults '
                                                   'to false.',
                                    'type': 'boolean'}},
  'required': ['k'],
  'type': 'object'}
TOOL_NOTES = "The constraint object produced here must be added to the `constraints` argument of a block-builder call — it does nothing on its own. The target level (Factor + Level pair) is bound at block-build time, not at construction time, so this tool only sets the `k` and `within_block` parameters. If the level never appears in the design, the constraint is silently satisfied; it does not force the level into the design. Using `within_block=true` subdivides the variable list into fixed-length windows equal to the crossing's trial count, which can produce unexpected SAT conflicts if `k` exceeds the window size."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.ExactlyK
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
    def create_exactly_k(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during the SweetPea design phase (step 1) when you need to enforce that a specific factor level appears in a trial sequence exactly `k` times — no more, no less.'
        return _impl(args or {})
