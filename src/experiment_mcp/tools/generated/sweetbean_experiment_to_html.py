"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '4ba0fde9b3129183e17269cc0e2a1326b0abd1c501b1d4223b1a29f83be0241c'
__exp_qualname__ = 'sweetbean.Experiment.to_html'
__exp_kind__ = 'method'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'to_html'
TOOL_DESCRIPTION = 'Call this tool as the final step of the experiment pipeline, after an Experiment handle has been obtained from the sweetbean_experiment tool, to serialize the compiled jsPsych experiment to a self-contained HTML file ready for browser delivery or human participants. The tool writes the file to `path` and returns nothing meaningful; use the resulting file path to serve or distribute the experiment.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "experiment": {\n      "description": "Handle string returned by the sweetbean_experiment tool representing the compiled Experiment instance to serialize.",\n      "type": "string"\n    },\n    "path": {\n      "description": "Filesystem path (including filename) where the HTML file will be written, e.g. \'/tmp/my_experiment.html\'.",\n      "type": "string"\n    },\n    "path_local_download": {\n      "description": "Optional alternative path used when generating the embedded JS for local-download scenarios. If omitted, `path` governs JS generation as well.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "experiment",\n    "path"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe file is written with `open(path, \'w\')` — no directory creation is performed, so the parent directory must already exist. `path_local_download` is forwarded to `to_js` internally; omit it unless you specifically need the generated JS to reference a different local path than the HTML output location. Any bot-detection protection assets configured on the Experiment are automatically injected into the HTML head; this happens silently with no extra arguments required.'
TOOL_PARAMETERS = { 'properties': { 'experiment': { 'description': 'Handle string returned by the '
                                                 'sweetbean_experiment tool '
                                                 'representing the compiled Experiment '
                                                 'instance to serialize.',
                                  'type': 'string'},
                  'path': { 'description': 'Filesystem path (including filename) where '
                                           'the HTML file will be written, e.g. '
                                           "'/tmp/my_experiment.html'.",
                            'type': 'string'},
                  'path_local_download': { 'description': 'Optional alternative path '
                                                          'used when generating the '
                                                          'embedded JS for '
                                                          'local-download scenarios. '
                                                          'If omitted, `path` governs '
                                                          'JS generation as well.',
                                           'type': 'string'}},
  'required': ['experiment', 'path'],
  'type': 'object'}
TOOL_NOTES = "The file is written with `open(path, 'w')` — no directory creation is performed, so the parent directory must already exist. `path_local_download` is forwarded to `to_js` internally; omit it unless you specifically need the generated JS to reference a different local path than the HTML output location. Any bot-detection protection assets configured on the Experiment are automatically injected into the HTML head; this happens silently with no extra arguments required."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = sb.Experiment
    resolved = handles.resolve_in(kwargs)
    instance = resolved.pop('experiment', None)
    if instance is None:
        raise TypeError(
            f"{TOOL_NAME} requires kwarg 'experiment' "
            f"(handle returned by create_experiment)."
        )
    if not isinstance(instance, cls):
        raise TypeError(
            f"{TOOL_NAME} got 'experiment'={type(instance).__name__}, "
            f"expected Experiment."
        )
    result = instance.to_html(**resolved)
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
    def to_html(args: dict[str, Any] | None = None) -> Any:
        'Call this tool as the final step of the experiment pipeline, after an Experiment handle has been obtained from the sweetbean_experiment tool, to serialize the compiled jsPsych experiment to a self-contained HTML file ready for browser delivery or human participants.'
        return _impl(args or {})
