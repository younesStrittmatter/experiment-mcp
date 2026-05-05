"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'f38a8534c5ea85bdab516f8c32075d3bd175c32fa72d55527e9f402df86a9f4b'
__exp_qualname__ = 'sweetpea.Pin'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_pin'
TOOL_DESCRIPTION = 'Call this tool during SweetPea experiment design — after creating Factors and Levels but before calling a generation function (e.g. `sweetpea_gen`) — when you need to fix a specific Factor Level to a specific trial position in the sequence. Returns a Pin constraint handle that must be passed in the `constraints` list of a block-creation tool (e.g. `sweetpea_fully_cross_block`).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "index": {\n      "description": "0-based trial position at which to pin the level. For example, 0 pins the level to the very first trial. Must be within the number of trials per sample or a WARNING is recorded and the constraint becomes unsatisfiable.",\n      "type": "integer"\n    },\n    "level": {\n      "description": "Handle string for a SweetPea Level object (returned by a level-creation tool such as `sweetpea_level`). The level\'s parent Factor is inferred automatically.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "index",\n    "level"\n  ],\n  "type": "object"\n}\n\nNotes:\nIndex is 0-based: trial position 0 is the first trial. If `index` falls outside the valid range for the block\'s `trials_per_sample`, SweetPea records a WARNING (not a hard error) and the constraint will be unsatisfiable at solve time — generation may succeed but the pin will silently have no effect. `Pin` marks itself as complex for combinatoric generation (`is_complex_for_combinatoric` returns `True`), so use `sweetpea_gen` (SAT/ILP backend) rather than the combinatoric backend when this constraint is present.'
TOOL_PARAMETERS = { 'properties': { 'index': { 'description': '0-based trial position at which to pin '
                                            'the level. For example, 0 pins the level '
                                            'to the very first trial. Must be within '
                                            'the number of trials per sample or a '
                                            'WARNING is recorded and the constraint '
                                            'becomes unsatisfiable.',
                             'type': 'integer'},
                  'level': { 'description': 'Handle string for a SweetPea Level object '
                                            '(returned by a level-creation tool such '
                                            "as `sweetpea_level`). The level's parent "
                                            'Factor is inferred automatically.',
                             'type': 'string'}},
  'required': ['index', 'level'],
  'type': 'object'}
TOOL_NOTES = "Index is 0-based: trial position 0 is the first trial. If `index` falls outside the valid range for the block's `trials_per_sample`, SweetPea records a WARNING (not a hard error) and the constraint will be unsatisfiable at solve time — generation may succeed but the pin will silently have no effect. `Pin` marks itself as complex for combinatoric generation (`is_complex_for_combinatoric` returns `True`), so use `sweetpea_gen` (SAT/ILP backend) rather than the combinatoric backend when this constraint is present."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Pin
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
    def create_pin(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during SweetPea experiment design — after creating Factors and Levels but before calling a generation function (e.g.'
        return _impl(args or {})
