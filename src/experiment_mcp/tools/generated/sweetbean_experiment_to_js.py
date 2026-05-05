"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '378629a13eaa7364a39d9e3e23564e17d2a5cc5d22dcd719614a8d60462ba3e1'
__exp_qualname__ = 'sweetbean.Experiment.to_js'
__exp_kind__ = 'method'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'to_js'
TOOL_DESCRIPTION = 'Call this tool at step 4 of the pipeline, after constructing an `Experiment` from SweetBean blocks, when you need to extract the raw jsPsych JavaScript (not a full HTML page). Pass the experiment handle returned by the Experiment constructor tool. The generated JS is stored back on the experiment object and can subsequently be embedded in a custom HTML shell; if you need a self-contained HTML file, use `sweetbean_experiment_to_html` instead.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "experiment": {\n      "description": "Handle string for the SweetBean Experiment object, as returned by the sweetbean_experiment constructor tool.",\n      "type": "string"\n    },\n    "path_local_download": {\n      "description": "Optional file path (must end in \'.json\' or \'.csv\') that jsPsych will use to trigger a local data download when the experiment finishes. Omit or pass null to skip local saving.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "experiment"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `path_local_download` must end in exactly `.json` or `.csv`; any other extension raises a hard exception at runtime.\n- The method mutates the experiment object in-place (writes to `self.js`) rather than returning the JS string — the caller should access the JS via the same experiment handle afterward.\n- Protection runtime libraries and jsPsych extension initializers are prepended automatically; do not inject them manually.\n- If no blocks have been added to the experiment or blocks have no stimuli, the output JS will be empty/minimal and `jsPsych.run` will receive an empty trials array.'
TOOL_PARAMETERS = { 'properties': { 'experiment': { 'description': 'Handle string for the SweetBean '
                                                 'Experiment object, as returned by '
                                                 'the sweetbean_experiment constructor '
                                                 'tool.',
                                  'type': 'string'},
                  'path_local_download': { 'description': 'Optional file path (must '
                                                          "end in '.json' or '.csv') "
                                                          'that jsPsych will use to '
                                                          'trigger a local data '
                                                          'download when the '
                                                          'experiment finishes. Omit '
                                                          'or pass null to skip local '
                                                          'saving.',
                                           'type': 'string'}},
  'required': ['experiment'],
  'type': 'object'}
TOOL_NOTES = '- `path_local_download` must end in exactly `.json` or `.csv`; any other extension raises a hard exception at runtime.\n- The method mutates the experiment object in-place (writes to `self.js`) rather than returning the JS string — the caller should access the JS via the same experiment handle afterward.\n- Protection runtime libraries and jsPsych extension initializers are prepended automatically; do not inject them manually.\n- If no blocks have been added to the experiment or blocks have no stimuli, the output JS will be empty/minimal and `jsPsych.run` will receive an empty trials array.'


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
        'Call this tool at step 4 of the pipeline, after constructing an `Experiment` from SweetBean blocks, when you need to extract the raw jsPsych JavaScript (not a full HTML page).'
        return _impl(args or {})
