"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '9a4def14a6960aa5f00307c0fe4b0ea2720d67283c8291e58713786a61b3d76c'
__exp_qualname__ = 'sweetpea.Repeat'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_repeat'
TOOL_DESCRIPTION = 'Call this tool after creating a `MultiCrossBlock` (via `sweetpea_multi_cross_block`) when you need to wrap that block in a repeating structure with additional trial-level constraints applied within each repeat. The result is a `Repeat` block handle that can be passed to `sweetpea_gen` / `sweetpea_iterate_gen` in place of a standard block to sample sequences where the crossing repeats under those constraints.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for a MultiCrossBlock produced by sweetpea_multi_cross_block. The Repeat wraps this block and inherits its design, crossings, and original constraints.",\n      "type": "string"\n    },\n    "constraints": {\n      "description": "List of handle strings for Constraint objects (e.g. from sweetpea_minimum_trials, sweetpea_exactly_k_in_a_row, etc.) to apply within each repeat. Exclude constraints are forbidden here and will raise a ValueError.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "block",\n    "constraints"\n  ],\n  "type": "object"\n}\n\nNotes:\nExclude constraints are explicitly disallowed in the `constraints` list — passing one raises `ValueError`. The block\'s own original constraints are automatically copied and scoped within-block before the new constraints are merged in, so do not re-pass the block\'s existing constraints. This is an internal SweetPea class; its primary purpose is composing multi-crossing repeat structures, not standalone use.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for a MultiCrossBlock '
                                            'produced by sweetpea_multi_cross_block. '
                                            'The Repeat wraps this block and inherits '
                                            'its design, crossings, and original '
                                            'constraints.',
                             'type': 'string'},
                  'constraints': { 'description': 'List of handle strings for '
                                                  'Constraint objects (e.g. from '
                                                  'sweetpea_minimum_trials, '
                                                  'sweetpea_exactly_k_in_a_row, etc.) '
                                                  'to apply within each repeat. '
                                                  'Exclude constraints are forbidden '
                                                  'here and will raise a ValueError.',
                                   'items': {'type': 'string'},
                                   'type': 'array'}},
  'required': ['block', 'constraints'],
  'type': 'object'}
TOOL_NOTES = "Exclude constraints are explicitly disallowed in the `constraints` list — passing one raises `ValueError`. The block's own original constraints are automatically copied and scoped within-block before the new constraints are merged in, so do not re-pass the block's existing constraints. This is an internal SweetPea class; its primary purpose is composing multi-crossing repeat structures, not standalone use."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Repeat
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
    def create_repeat(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after creating a `MultiCrossBlock` (via `sweetpea_multi_cross_block`) when you need to wrap that block in a repeating structure with additional trial-level constraints applied within each repeat.'
        return _impl(args or {})
