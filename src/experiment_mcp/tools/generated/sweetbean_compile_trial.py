"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '7e305a4c676197e249ec5456eea98bf0d17617f7cde4f815daaf2c9dcff93028'
__exp_qualname__ = 'sweetbean.compile_trial'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'compile_trial'
TOOL_DESCRIPTION = 'Call this tool after building a TrialSpec (via sweetbean_trial_spec) to convert it into a concrete SweetBean stimulus object (HtmlKeyboardResponse, HtmlChoice, or HtmlSliderResponse). Use this in step 3–4 of the pipeline, between wiring SweetPea-sampled levels into SweetBean trial specs and assembling those stimuli into a Block or Experiment. The returned handle references the compiled stimulus object, ready to be passed to sweetbean_block or sweetbean_experiment tools.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "spec": {\n      "description": "Handle string for the TrialSpec to compile, as returned by sweetbean_trial_spec. The runtime resolves this to the live TrialSpec object before dispatch.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "spec"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe current renderer supports exactly one response spec per trial — passing a TrialSpec with zero responses produces an HtmlKeyboardResponse with no allowed keys and no time limit; passing one with more than one response raises a ValueError. For keyboard responses, at most one correct_keys entry is accepted. For keyboard and mouse-click responses, max_responses > 1 is unsupported. For slider responses, start_value defaults to the midpoint of [min_value, max_value] when omitted. Mouse-click responses will raise if no clickable targets survive target_ids filtering.'
TOOL_PARAMETERS = { 'properties': { 'spec': { 'description': 'Handle string for the TrialSpec to '
                                           'compile, as returned by '
                                           'sweetbean_trial_spec. The runtime resolves '
                                           'this to the live TrialSpec object before '
                                           'dispatch.',
                            'type': 'string'}},
  'required': ['spec'],
  'type': 'object'}
TOOL_NOTES = 'The current renderer supports exactly one response spec per trial — passing a TrialSpec with zero responses produces an HtmlKeyboardResponse with no allowed keys and no time limit; passing one with more than one response raises a ValueError. For keyboard responses, at most one correct_keys entry is accepted. For keyboard and mouse-click responses, max_responses > 1 is unsupported. For slider responses, start_value defaults to the midpoint of [min_value, max_value] when omitted. Mouse-click responses will raise if no clickable targets survive target_ids filtering.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.compile_trial
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
    def compile_trial(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after building a TrialSpec (via sweetbean_trial_spec) to convert it into a concrete SweetBean stimulus object (HtmlKeyboardResponse, HtmlChoice, or HtmlSliderResponse).'
        return _impl(args or {})
