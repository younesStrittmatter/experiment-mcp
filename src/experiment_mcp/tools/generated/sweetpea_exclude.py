"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'efc680e36e99eca851259b59a7bbce608fe689030b650a9fac7d66d7343eb1a1'
__exp_qualname__ = 'sweetpea.Exclude'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_exclude'
TOOL_DESCRIPTION = 'Call this tool to create an `Exclude` constraint that prevents a specific factor level from appearing in any synthesized trial sequence. Use it in the SweetPea pipeline after defining factors and levels but before passing constraints to `CrossBlock` or `synthesize_trials`. The result is a constraint handle that must be included in the `constraints` list when building the block.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "level": {\n      "description": "Handle string for the Level object (SimpleLevel or DerivedLevel) to exclude. Produced by a factor-creation tool (e.g. sweetpea_factor or sweetpea_derived_level). The factor that owns this level is inferred automatically.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "level"\n  ],\n  "type": "object"\n}\n\nNotes:\nExcluding a level that participates in a complete crossing will produce a WARNING and may result in an incomplete crossing — the block-level error set is updated but synthesis is not halted. Works with both SimpleLevel and DerivedLevel; for derived levels without a complex window, the constraint is expanded into the underlying simple-level combinations automatically. Pass the returned handle in the `constraints` list of `CrossBlock` or equivalent block-construction tool — `Exclude` has no effect on its own.'
TOOL_PARAMETERS = { 'properties': { 'level': { 'description': 'Handle string for the Level object '
                                            '(SimpleLevel or DerivedLevel) to exclude. '
                                            'Produced by a factor-creation tool (e.g. '
                                            'sweetpea_factor or '
                                            'sweetpea_derived_level). The factor that '
                                            'owns this level is inferred '
                                            'automatically.',
                             'type': 'string'}},
  'required': ['level'],
  'type': 'object'}
TOOL_NOTES = 'Excluding a level that participates in a complete crossing will produce a WARNING and may result in an incomplete crossing — the block-level error set is updated but synthesis is not halted. Works with both SimpleLevel and DerivedLevel; for derived levels without a complex window, the constraint is expanded into the underlying simple-level combinations automatically. Pass the returned handle in the `constraints` list of `CrossBlock` or equivalent block-construction tool — `Exclude` has no effect on its own.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Exclude
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
    def create_exclude(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create an `Exclude` constraint that prevents a specific factor level from appearing in any synthesized trial sequence.'
        return _impl(args or {})
