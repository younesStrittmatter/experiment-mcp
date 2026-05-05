"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '78e763adfd3dbd8ff0dba0eb89cf9f5b183a2e5a33eea7c28642e3f89ff66998'
__exp_qualname__ = 'sweetpea.AlignmentMode'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_alignment_mode'
TOOL_DESCRIPTION = 'Call this tool when you need to specify how multiple crossings should be aligned relative to preamble sequences before passing the result to a SweetPea crossing function (e.g., `multiple_cross_block`). Returns an `AlignmentMode` enum member that controls whether all crossings start after the shared preamble ends, start in parallel from the beginning, or use equal-length preambles.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "value": {\n      "description": "Which alignment strategy to select. \'post preamble\': all crossings begin after the shared preamble finishes (default for most designs). \'parallel start\': all crossings begin at trial 1 simultaneously. \'equal preamble\': each crossing is given a preamble of equal length.",\n      "enum": [\n        "post preamble",\n        "parallel start",\n        "equal preamble"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "value"\n  ],\n  "type": "object"\n}\n\nNotes:\nPass the string value (e.g., "post preamble"), not the member name ("POST_PREAMBLE") — AlignmentMode is constructed by value. This enum is only relevant when a design has multiple crossings; single-crossing designs ignore the alignment mode entirely. EQUAL_PREAMBLE has no inline comment in the source explaining its exact semantics — prefer POST_PREAMBLE or PARALLEL_START unless the experiment design explicitly requires equal-length preambles.'
TOOL_PARAMETERS = { 'properties': { 'value': { 'description': "Which alignment strategy to select. 'post "
                                            "preamble': all crossings begin after the "
                                            'shared preamble finishes (default for '
                                            "most designs). 'parallel start': all "
                                            'crossings begin at trial 1 '
                                            "simultaneously. 'equal preamble': each "
                                            'crossing is given a preamble of equal '
                                            'length.',
                             'enum': [ 'post preamble',
                                       'parallel start',
                                       'equal preamble'],
                             'type': 'string'}},
  'required': ['value'],
  'type': 'object'}
TOOL_NOTES = 'Pass the string value (e.g., "post preamble"), not the member name ("POST_PREAMBLE") — AlignmentMode is constructed by value. This enum is only relevant when a design has multiple crossings; single-crossing designs ignore the alignment mode entirely. EQUAL_PREAMBLE has no inline comment in the source explaining its exact semantics — prefer POST_PREAMBLE or PARALLEL_START unless the experiment design explicitly requires equal-length preambles.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.AlignmentMode
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
    def create_alignment_mode(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to specify how multiple crossings should be aligned relative to preamble sequences before passing the result to a SweetPea crossing function (e.g., `multiple_cross_block`).'
        return _impl(args or {})
