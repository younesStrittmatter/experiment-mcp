"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '26df1500485a207ca0976dcfb92b0412f9e6bec1d8be7f346fd5d9e8f68e3e46'
__exp_qualname__ = 'sweetpea.RepeatMode'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_repeat_mode'
TOOL_DESCRIPTION = 'Call this tool to obtain a RepeatMode enum member that controls how SweetPea handles trial repetition when building a crossing (CrossBlock / MultiCrossBlock). Use it at design-declaration time — step 1 of the pipeline — before sampling a sequence. The result is a handle string resolving to one of RepeatMode.WEIGHT, RepeatMode.REPEAT, or RepeatMode.EQUAL, which you pass to the repeat_mode parameter of a block constructor.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "The repeat-mode variant to select. \'weight\' weights trials by crossing counts; \'repeat\' repeats trial types until quotas are met; \'equal\' forces equal counts across all trial types.",\n      "enum": [\n        "weight",\n        "repeat",\n        "equal"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nRepeatMode is an Enum; the tool is invoked as RepeatMode(value), so pass the lowercase string value (e.g. "weight"), not the member name ("WEIGHT"). The returned handle resolves to the enum member itself, not a numeric code. If the downstream block constructor does not accept a repeat_mode keyword, this handle is silently unused — confirm the target block type supports it before calling.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': 'The repeat-mode variant to select. '
                                            "'weight' weights trials by crossing "
                                            "counts; 'repeat' repeats trial types "
                                            "until quotas are met; 'equal' forces "
                                            'equal counts across all trial types.',
                             'enum': ['weight', 'repeat', 'equal'],
                             'type': 'string'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'RepeatMode is an Enum; the tool is invoked as RepeatMode(value), so pass the lowercase string value (e.g. "weight"), not the member name ("WEIGHT"). The returned handle resolves to the enum member itself, not a numeric code. If the downstream block constructor does not accept a repeat_mode keyword, this handle is silently unused — confirm the target block type supports it before calling.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.RepeatMode
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
    def create_repeat_mode(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to obtain a RepeatMode enum member that controls how SweetPea handles trial repetition when building a crossing (CrossBlock / MultiCrossBlock).'
        return _impl(args or {})
