"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '8343d8f4ab21072ba91c47551ca4d0c05f32aabf7e7eb32359e06fefa7c05a5e'
__exp_qualname__ = 'sweetbean.stimulus_spec.write_prompt_schema_markdown'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'write_prompt_schema_markdown'
TOOL_DESCRIPTION = 'Call this tool to write a markdown reference file documenting all SweetBean Trial, Stimulus, and Response spec schemas to disk. Use it at the start of an experiment-building session to produce a local schema guide that an agent can read to understand valid stimulus/response field names and types before constructing SweetBean objects. Returns the absolute path of the written file.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "out_path": {\n      "description": "Filesystem path where the markdown file should be written (e.g. \'/tmp/sweetbean_schemas.md\'). Any parent directories must already exist.",\n      "type": "string"\n    },\n    "verbosity": {\n      "default": 1,\n      "description": "Controls how much detail is included in the generated docs. 1 (default) = standard descriptions; higher values add more detail.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "out_path"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function writes to the path exactly as given — it does not create parent directories. Ensure the parent directory exists before calling. The return value is the resolved Path of the written file (as a string handle). Verbosity values above 1 are accepted but their behavior depends on `build_prompt_schema_markdown`; the safe default is 1.'
TOOL_PARAMETERS = { 'properties': { 'out_path': { 'description': 'Filesystem path where the markdown '
                                               'file should be written (e.g. '
                                               "'/tmp/sweetbean_schemas.md'). Any "
                                               'parent directories must already exist.',
                                'type': 'string'},
                  'verbosity': { 'default': 1,
                                 'description': 'Controls how much detail is included '
                                                'in the generated docs. 1 (default) = '
                                                'standard descriptions; higher values '
                                                'add more detail.',
                                 'type': 'integer'}},
  'required': ['out_path'],
  'type': 'object'}
TOOL_NOTES = 'The function writes to the path exactly as given — it does not create parent directories. Ensure the parent directory exists before calling. The return value is the resolved Path of the written file (as a string handle). Verbosity values above 1 are accepted but their behavior depends on `build_prompt_schema_markdown`; the safe default is 1.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.write_prompt_schema_markdown
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
    def write_prompt_schema_markdown(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to write a markdown reference file documenting all SweetBean Trial, Stimulus, and Response spec schemas to disk.'
        return _impl(args or {})
