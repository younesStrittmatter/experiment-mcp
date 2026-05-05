"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'a9f4ba9e35d197281d399418fb5ec2405c11e75b13b7bbdf2a1924b818832cf7'
__exp_qualname__ = 'sweetbean.stimulus_spec.trial_specs_from_files'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'trial_specs_from_files'
TOOL_DESCRIPTION = 'Call this tool when you have a JSON spec-library file (defining named trial templates) and a CSV timeline file (mapping rows to spec IDs and parameter overrides) and want to produce a validated list of TrialSpec objects ready to pass into SweetBean trial/block construction. This sits between the SweetPea sampling step (which produces a timeline CSV) and the SweetBean compilation step (which consumes TrialSpecs). The result is a list of fully-resolved, Pydantic-validated TrialSpec objects.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "spec_json_path": {\n      "description": "Absolute or relative path to the JSON file containing the named trial-template library. Each top-level key is a spec_id; values are the template dicts that get resolved against timeline row values.",\n      "type": "string"\n    },\n    "timeline_csv_path": {\n      "description": "Absolute or relative path to the CSV file whose rows define the trial sequence. Must contain a \'spec_id\' column whose values match keys in the JSON spec library. Additional columns supply per-trial parameter overrides that are interpolated into the template.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "spec_json_path",\n    "timeline_csv_path"\n  ],\n  "type": "object"\n}\n\nNotes:\nEvery row in the CSV must have a `spec_id` that exists as a top-level key in the JSON spec library; a missing key raises `KeyError` with no partial output. The function returns a plain Python list of TrialSpec objects — not a handle string — so downstream tools that accept a handle should be given the result of a tool that wraps this list in the handle registry. Paths are passed straight to `pathlib.Path`, so both absolute and relative paths work, but relative paths resolve against the server\'s working directory, not the caller\'s.'
TOOL_PARAMETERS = { 'properties': { 'spec_json_path': { 'description': 'Absolute or relative path to the '
                                                     'JSON file containing the named '
                                                     'trial-template library. Each '
                                                     'top-level key is a spec_id; '
                                                     'values are the template dicts '
                                                     'that get resolved against '
                                                     'timeline row values.',
                                      'type': 'string'},
                  'timeline_csv_path': { 'description': 'Absolute or relative path to '
                                                        'the CSV file whose rows '
                                                        'define the trial sequence. '
                                                        "Must contain a 'spec_id' "
                                                        'column whose values match '
                                                        'keys in the JSON spec '
                                                        'library. Additional columns '
                                                        'supply per-trial parameter '
                                                        'overrides that are '
                                                        'interpolated into the '
                                                        'template.',
                                         'type': 'string'}},
  'required': ['spec_json_path', 'timeline_csv_path'],
  'type': 'object'}
TOOL_NOTES = "Every row in the CSV must have a `spec_id` that exists as a top-level key in the JSON spec library; a missing key raises `KeyError` with no partial output. The function returns a plain Python list of TrialSpec objects — not a handle string — so downstream tools that accept a handle should be given the result of a tool that wraps this list in the handle registry. Paths are passed straight to `pathlib.Path`, so both absolute and relative paths work, but relative paths resolve against the server's working directory, not the caller's."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.trial_specs_from_files
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
    def trial_specs_from_files(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you have a JSON spec-library file (defining named trial templates) and a CSV timeline file (mapping rows to spec IDs and parameter overrides) and want to produce a validated list of TrialSpec objects ready to pass into SweetBean trial/block construction.'
        return _impl(args or {})
