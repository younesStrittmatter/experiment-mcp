"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'c56360f5e4477b86db748d77eafb6086223eddd072bbdacf8b7f0453b8ffc6a5'
__exp_qualname__ = 'sweetbean.stimulus_spec.load_spec_library'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'load_spec_library'
TOOL_DESCRIPTION = 'Call this tool at the start of experiment construction when you have a JSON library of reusable trial-spec templates on disk and want to load them into the agent context before wiring SweetPea trial sequences into SweetBean stimuli. Returns a plain dict mapping spec IDs (strings) to raw spec dicts, which you can then look up by name when constructing stimuli or blocks — no handle needed, the result is used directly as argument values in downstream SweetBean tool calls.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "path": {\n      "description": "Absolute or relative filesystem path to a JSON file whose top-level \'specs\' key maps non-empty string IDs to spec-template objects.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "path"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe JSON file must contain a top-level "specs" key whose value is a non-empty object; any other shape raises ValueError. Every key in "specs" must be a non-empty string and every value must be a JSON object — bare strings, arrays, or nulls are rejected. The function returns a raw Python dict (not a handle); pass individual entries directly to downstream SweetBean tools rather than storing the whole dict as a handle.'
TOOL_PARAMETERS = { 'properties': { 'path': { 'description': 'Absolute or relative filesystem path to a '
                                           "JSON file whose top-level 'specs' key maps "
                                           'non-empty string IDs to spec-template '
                                           'objects.',
                            'type': 'string'}},
  'required': ['path'],
  'type': 'object'}
TOOL_NOTES = 'The JSON file must contain a top-level "specs" key whose value is a non-empty object; any other shape raises ValueError. Every key in "specs" must be a non-empty string and every value must be a JSON object — bare strings, arrays, or nulls are rejected. The function returns a raw Python dict (not a handle); pass individual entries directly to downstream SweetBean tools rather than storing the whole dict as a handle.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.load_spec_library
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
    def load_spec_library(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at the start of experiment construction when you have a JSON library of reusable trial-spec templates on disk and want to load them into the agent context before wiring SweetPea trial sequences into SweetBean stimuli.'
        return _impl(args or {})
