"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '1fc142c6c6261e8cdf8c14c8542be0422618247ccb81900a8e50f1a629256066'
__exp_qualname__ = 'sweetbean.Experiment.to_js_string'
__exp_kind__ = 'method'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'to_js_string'
TOOL_DESCRIPTION = 'Call this tool after constructing a SweetBean Experiment (step 4 of the pipeline) when you need the raw JavaScript string rather than a full HTML page — for example, to embed the experiment logic in a custom HTML shell, inspect the generated jsPsych code, or pass it to a downstream bundler. Returns a JavaScript string containing jsPsych trial definitions and (optionally) a wrapping async function; use `sweetbean_experiment_to_html` instead if you want a self-contained HTML file.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "as_function": {\n      "default": true,\n      "description": "When true (default), wraps the output in a named JS function with a preamble and appendix. Set to false to emit a bare script fragment without any function wrapper.",\n      "type": "boolean"\n    },\n    "experiment": {\n      "description": "Handle string returned by the sweetbean_experiment constructor tool identifying the live Experiment instance to serialize.",\n      "type": "string"\n    },\n    "is_async": {\n      "default": true,\n      "description": "When true (default), the wrapping function (or appendix) is declared async. Only meaningful when as_function is true or when the TEXT_APPENDIX expects async syntax.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "experiment"\n  ],\n  "type": "object"\n}\n\nNotes:\nWhen `as_function=False` the `is_async` flag still influences the `TEXT_APPENDIX` (the post-run block appended after the trial array), so it is not fully ignored even without a function wrapper. The returned string contains jsPsych `initJsPsych(...)` and the `trials` array inline; any bot-detection or protection runtime JS is prepended automatically from the Experiment\'s configured protections — the agent does not need to handle those separately. The summary/addProperties call is placed in a post-run hook rather than `initJsPsych`\'s `on_finish` to avoid racing with the run loop; this is invisible to the caller but explains why the string may look longer than expected.'
TOOL_PARAMETERS = { 'properties': { 'as_function': { 'default': True,
                                   'description': 'When true (default), wraps the '
                                                  'output in a named JS function with '
                                                  'a preamble and appendix. Set to '
                                                  'false to emit a bare script '
                                                  'fragment without any function '
                                                  'wrapper.',
                                   'type': 'boolean'},
                  'experiment': { 'description': 'Handle string returned by the '
                                                 'sweetbean_experiment constructor '
                                                 'tool identifying the live Experiment '
                                                 'instance to serialize.',
                                  'type': 'string'},
                  'is_async': { 'default': True,
                                'description': 'When true (default), the wrapping '
                                               'function (or appendix) is declared '
                                               'async. Only meaningful when '
                                               'as_function is true or when the '
                                               'TEXT_APPENDIX expects async syntax.',
                                'type': 'boolean'}},
  'required': ['experiment'],
  'type': 'object'}
TOOL_NOTES = "When `as_function=False` the `is_async` flag still influences the `TEXT_APPENDIX` (the post-run block appended after the trial array), so it is not fully ignored even without a function wrapper. The returned string contains jsPsych `initJsPsych(...)` and the `trials` array inline; any bot-detection or protection runtime JS is prepended automatically from the Experiment's configured protections — the agent does not need to handle those separately. The summary/addProperties call is placed in a post-run hook rather than `initJsPsych`'s `on_finish` to avoid racing with the run loop; this is invisible to the caller but explains why the string may look longer than expected."


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
    result = instance.to_js_string(**resolved)
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
    def to_js_string(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after constructing a SweetBean Experiment (step 4 of the pipeline) when you need the raw JavaScript string rather than a full HTML page — for example, to embed the experiment logic in a custom HTML shell, inspect the generated jsPsych code, or pass it to a downstream bundler.'
        return _impl(args or {})
