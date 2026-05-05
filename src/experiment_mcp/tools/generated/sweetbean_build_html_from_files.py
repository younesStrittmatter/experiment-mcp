"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'be4f1bf6339d663818a862604905157698c88954d9f38e1310679b3eb55fb800'
__exp_qualname__ = 'sweetbean.build_html_from_files'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'build_html_from_files'
TOOL_DESCRIPTION = 'Call this tool at the final step of the pipeline when you have a declarative stimulus spec on disk (JSON) and a trial timeline CSV (e.g., exported from SweetPea\'s sequence sampler) and want to produce a self-contained, runnable jsPsych HTML file in one operation. Returns the path to the written HTML file. Use this instead of the programmatic Experiment/Block/compile_trial path when both input files already exist on disk.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "out_html_path": {\n      "description": "Destination filesystem path where the compiled, self-contained jsPsych HTML will be written. The file is created or overwritten.",\n      "type": "string"\n    },\n    "spec_json_path": {\n      "description": "Filesystem path to the JSON file containing the declarative stimulus/trial spec (produced by the spec authoring step or exported from a SweetBean TrialSpec).",\n      "type": "string"\n    },\n    "timeline_csv_path": {\n      "description": "Filesystem path to the CSV file containing the trial timeline \\u2014 typically the sequence CSV exported from SweetPea\'s sampler (one row per trial, columns matching factor names in the spec).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "spec_json_path",\n    "timeline_csv_path",\n    "out_html_path"\n  ],\n  "type": "object"\n}\n\nNotes:\nAll compiled trials are wrapped in a single Block before being passed to Experiment; if the design requires multiple blocks with different inter-block logic, use the programmatic API (compile_trial / Block / Experiment) instead. The output file is silently overwritten if it already exists. The return value is the resolved output path (as a string handle); the HTML is self-contained and can be opened directly in a browser or deployed to a jsPsych hosting endpoint.'
TOOL_PARAMETERS = { 'properties': { 'out_html_path': { 'description': 'Destination filesystem path where '
                                                    'the compiled, self-contained '
                                                    'jsPsych HTML will be written. The '
                                                    'file is created or overwritten.',
                                     'type': 'string'},
                  'spec_json_path': { 'description': 'Filesystem path to the JSON file '
                                                     'containing the declarative '
                                                     'stimulus/trial spec (produced by '
                                                     'the spec authoring step or '
                                                     'exported from a SweetBean '
                                                     'TrialSpec).',
                                      'type': 'string'},
                  'timeline_csv_path': { 'description': 'Filesystem path to the CSV '
                                                        'file containing the trial '
                                                        'timeline — typically the '
                                                        'sequence CSV exported from '
                                                        "SweetPea's sampler (one row "
                                                        'per trial, columns matching '
                                                        'factor names in the spec).',
                                         'type': 'string'}},
  'required': ['spec_json_path', 'timeline_csv_path', 'out_html_path'],
  'type': 'object'}
TOOL_NOTES = 'All compiled trials are wrapped in a single Block before being passed to Experiment; if the design requires multiple blocks with different inter-block logic, use the programmatic API (compile_trial / Block / Experiment) instead. The output file is silently overwritten if it already exists. The return value is the resolved output path (as a string handle); the HTML is self-contained and can be opened directly in a browser or deployed to a jsPsych hosting endpoint.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.build_html_from_files
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
    def build_html_from_files(args: dict[str, Any] | None = None) -> Any:
        "Call this tool at the final step of the pipeline when you have a declarative stimulus spec on disk (JSON) and a trial timeline CSV (e.g., exported from SweetPea's sequence sampler) and want to produce a self-contained, runnable jsPsych HTML file in one operation."
        return _impl(args or {})
