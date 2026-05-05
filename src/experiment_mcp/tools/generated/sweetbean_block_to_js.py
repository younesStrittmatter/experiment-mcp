"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'c0b9c733c7686f8594581bcc87655a05918ff74093a433c493296a38790a2dc4'
__exp_qualname__ = 'sweetbean.Block.to_js'
__exp_kind__ = 'method'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'to_js'
TOOL_DESCRIPTION = 'Call this tool in pipeline step 4, after constructing a SweetBean `Block` via its constructor tool, to emit the jsPsych JavaScript source for that block\'s trials. The result is a JS string (stored on the block handle) of the form `{timeline: [...], timeline_variables: [...]}`, ready to be embedded in a full experiment. Pass `template_timeline_token` only when building multi-condition experiments via `Experiment.compile`\'s template path, to defer timeline-variable injection until `Experiment.to_js_string_from_template` is called.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the Block instance whose jsPsych source should be built. Returned by the sweetbean.Block constructor tool.",\n      "type": "string"\n    },\n    "template_timeline_token": {\n      "description": "Optional placeholder token string (e.g. a JS variable name) to be substituted for timeline_variables instead of inlining the data. Use only when Experiment.compile was invoked with a template_timeline_token for deferred multi-condition builds.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "block"\n  ],\n  "type": "object"\n}\n\nNotes:\nPassing `template_timeline_token` when the block\'s timeline is a `CodeVariable` raises `ValueError` — these two features are mutually exclusive. When `template_timeline_token` is omitted, the full timeline data is inlined into the emitted JS immediately. The generated JS is also written to the `block.js` attribute on the live object behind the handle, so subsequent tools that read the same handle will see it.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the Block instance '
                                            'whose jsPsych source should be built. '
                                            'Returned by the sweetbean.Block '
                                            'constructor tool.',
                             'type': 'string'},
                  'template_timeline_token': { 'description': 'Optional placeholder '
                                                              'token string (e.g. a JS '
                                                              'variable name) to be '
                                                              'substituted for '
                                                              'timeline_variables '
                                                              'instead of inlining the '
                                                              'data. Use only when '
                                                              'Experiment.compile was '
                                                              'invoked with a '
                                                              'template_timeline_token '
                                                              'for deferred '
                                                              'multi-condition builds.',
                                               'type': 'string'}},
  'required': ['block'],
  'type': 'object'}
TOOL_NOTES = "Passing `template_timeline_token` when the block's timeline is a `CodeVariable` raises `ValueError` — these two features are mutually exclusive. When `template_timeline_token` is omitted, the full timeline data is inlined into the emitted JS immediately. The generated JS is also written to the `block.js` attribute on the live object behind the handle, so subsequent tools that read the same handle will see it."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = sb.Block
    resolved = handles.resolve_in(kwargs)
    instance = resolved.pop('block', None)
    if instance is None:
        raise TypeError(
            f"{TOOL_NAME} requires kwarg 'block' "
            f"(handle returned by create_block)."
        )
    if not isinstance(instance, cls):
        raise TypeError(
            f"{TOOL_NAME} got 'block'={type(instance).__name__}, "
            f"expected Block."
        )
    result = instance.to_js(**resolved)
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
    def to_js(args: dict[str, Any] | None = None) -> Any:
        "Call this tool in pipeline step 4, after constructing a SweetBean `Block` via its constructor tool, to emit the jsPsych JavaScript source for that block's trials."
        return _impl(args or {})
