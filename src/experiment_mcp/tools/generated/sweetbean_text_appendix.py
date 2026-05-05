"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '53174c962780cd36cdbe99415cb14ebd1593b6d6a532b59ec96c18c1d75f01f9'
__exp_qualname__ = 'sweetbean.experiment.TEXT_APPENDIX'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'text_appendix'
TOOL_DESCRIPTION = 'Call this tool at the end of a manual jsPsych script assembly to emit the closing `jsPsych.run(trials)` line and any post-run JavaScript. It belongs at step 4 of the pipeline — after preamble and trial/block body code have been assembled — and returns a ready-to-append JS string that closes the top-level (non-function) script.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "is_async": {\n      "description": "If true, prefixes the jsPsych.run call with \'await\', producing \'await jsPsych.run(trials)\'. Set to true when the surrounding script context is an async function or top-level await is supported.",\n      "type": "boolean"\n    },\n    "post_run_js": {\n      "default": "",\n      "description": "Optional JavaScript code to append after jsPsych.run completes. Trailing semicolons, newlines, and spaces are stripped before appending. Defaults to empty string (nothing appended).",\n      "type": "string"\n    }\n  },\n  "required": [\n    "is_async"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis tool generates raw JS text — it does not register or execute the experiment. `is_async` has no default and must always be supplied explicitly; pass false for standard synchronous jsPsych setups. The `post_run_js` value is right-stripped of trailing `;\\n ` before insertion, so the caller need not worry about trailing punctuation but should not rely on it being preserved verbatim.'
TOOL_PARAMETERS = { 'properties': { 'is_async': { 'description': 'If true, prefixes the jsPsych.run call '
                                               "with 'await', producing 'await "
                                               "jsPsych.run(trials)'. Set to true when "
                                               'the surrounding script context is an '
                                               'async function or top-level await is '
                                               'supported.',
                                'type': 'boolean'},
                  'post_run_js': { 'default': '',
                                   'description': 'Optional JavaScript code to append '
                                                  'after jsPsych.run completes. '
                                                  'Trailing semicolons, newlines, and '
                                                  'spaces are stripped before '
                                                  'appending. Defaults to empty string '
                                                  '(nothing appended).',
                                   'type': 'string'}},
  'required': ['is_async'],
  'type': 'object'}
TOOL_NOTES = 'This tool generates raw JS text — it does not register or execute the experiment. `is_async` has no default and must always be supplied explicitly; pass false for standard synchronous jsPsych setups. The `post_run_js` value is right-stripped of trailing `;\\n ` before insertion, so the caller need not worry about trailing punctuation but should not rely on it being preserved verbatim.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.TEXT_APPENDIX
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
    def text_appendix(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at the end of a manual jsPsych script assembly to emit the closing `jsPsych.run(trials)` line and any post-run JavaScript.'
        return _impl(args or {})
