"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'c3e814fff0f0152c7be56def4fcffb771e9d67b8445321ec07d951c4bfe572b6'
__exp_qualname__ = 'sweetpea.Level'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_level'
TOOL_DESCRIPTION = 'Call this tool in Step 1 of the SweetPea pipeline to create a named discrete value that will be passed as an element of a Factor\'s level list. The result is a handle string representing a SimpleLevel object; pass it (inside an array) to the `sweetpea_factor` tool\'s `levels` parameter to build a fully declared Factor.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "The display name for this level (e.g. \\"red\\", \\"congruent\\", \\"left\\"). Used in output trial sequences and design graphs.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "name"\n  ],\n  "type": "object"\n}\n\nNotes:\nEquality is identity-based: two Level objects with the same name are NOT equal. Reuse the handle string returned by this tool rather than recreating a level with the same name, otherwise SweetPea will treat them as distinct levels. Calling `Level(name)` actually instantiates `SimpleLevel` internally — this is intentional and transparent. The `factor` field is assigned automatically when the level is added to a Factor; never pass it. To create a conditional/derived level (one whose value depends on other factors), use `sweetpea_derived_level` instead. Weight is always 1 for levels created via this tool; use `DerivedLevel` with a weight argument if non-uniform sampling is needed.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'The display name for this level (e.g. '
                                           '"red", "congruent", "left"). Used in '
                                           'output trial sequences and design graphs.',
                            'type': 'string'}},
  'required': ['name'],
  'type': 'object'}
TOOL_NOTES = 'Equality is identity-based: two Level objects with the same name are NOT equal. Reuse the handle string returned by this tool rather than recreating a level with the same name, otherwise SweetPea will treat them as distinct levels. Calling `Level(name)` actually instantiates `SimpleLevel` internally — this is intentional and transparent. The `factor` field is assigned automatically when the level is added to a Factor; never pass it. To create a conditional/derived level (one whose value depends on other factors), use `sweetpea_derived_level` instead. Weight is always 1 for levels created via this tool; use `DerivedLevel` with a weight argument if non-uniform sampling is needed.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Level
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
    def create_level(args: dict[str, Any] | None = None) -> Any:
        "Call this tool in Step 1 of the SweetPea pipeline to create a named discrete value that will be passed as an element of a Factor's level list."
        return _impl(args or {})
