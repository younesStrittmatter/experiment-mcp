"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '3f81d064a2cb0ac472daccf8e3ea89c5f69d5109e0877bd7f698259a8113d692'
__exp_qualname__ = 'sweetbean.block.sb_to_js'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'sb_to_js'
TOOL_DESCRIPTION = 'Call this tool to convert a SweetBean variable (a stimulus property value, timeline variable, or code variable handle) to its JavaScript string representation. Use it mid-pipeline when you need the raw JS expression for a SweetBean object — for example, to inspect or splice a variable\'s JS form before the full block or experiment compiles to HTML. Returns a JavaScript expression string.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "var": {\n      "description": "Handle string referencing the SweetBean variable, stimulus property value, or code variable to convert to JavaScript. Produced by earlier SweetBean tool calls (e.g. sweetbean_code_variable, sweetbean_text_stimulus_spec).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "var"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe underlying implementation delegates to an internal `_var_to_js` helper whose accepted types are not documented. Only SweetBean variable-like objects (e.g. CodeVariable, timeline-variable references, primitive wrappers) are expected to round-trip correctly; passing a raw Block or Experiment handle will likely produce unexpected output or raise. Use sweetbean_block_to_js or sweetbean_experiment_to_js to compile full blocks and experiments instead.'
TOOL_PARAMETERS = { 'properties': { 'var': { 'description': 'Handle string referencing the SweetBean '
                                          'variable, stimulus property value, or code '
                                          'variable to convert to JavaScript. Produced '
                                          'by earlier SweetBean tool calls (e.g. '
                                          'sweetbean_code_variable, '
                                          'sweetbean_text_stimulus_spec).',
                           'type': 'string'}},
  'required': ['var'],
  'type': 'object'}
TOOL_NOTES = 'The underlying implementation delegates to an internal `_var_to_js` helper whose accepted types are not documented. Only SweetBean variable-like objects (e.g. CodeVariable, timeline-variable references, primitive wrappers) are expected to round-trip correctly; passing a raw Block or Experiment handle will likely produce unexpected output or raise. Use sweetbean_block_to_js or sweetbean_experiment_to_js to compile full blocks and experiments instead.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.sb_to_js
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
    def sb_to_js(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to convert a SweetBean variable (a stimulus property value, timeline variable, or code variable handle) to its JavaScript string representation.'
        return _impl(args or {})
