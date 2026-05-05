"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '72f4cfea50f9e3997b7c083b1e2086f9ef9969eb168539418b8cc14d482d52b4'
__exp_qualname__ = 'sweetpea.RandomGen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_random_gen'
TOOL_DESCRIPTION = 'Call this tool to create a `RandomGen` sampling-strategy handle to pass as the `gen` argument to sequence-generation tools (e.g. `sweetpea_gen`). Use it in step 2 of the pipeline — after declaring factors and a `CrossBlock` — when you want gold-standard uniform sampling of valid trial sequences. The returned handle represents the strategy object; pass it wherever a `Gen` is expected.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "acceptable_error": {\n      "description": "Maximum number of crossing-combination mismatches tolerated before a candidate sequence is rejected. Pass 0 for strict uniform sampling (no constraint violations allowed). Increase only for complex multi-crossing or window-constrained designs where strict rejection sampling is prohibitively slow \\u2014 higher values trade distributional purity for speed.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "acceptable_error"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `acceptable_error` has no default and must always be supplied; `0` is the correct value for most designs.\n- The static `RandomGen.sample()` method always uses `acceptable_error=0`; only the instance (produced by this tool) respects a non-zero value via `sample_object`.\n- Rejection sampling on designs with complex windows or multiple crossings can be very slow; the library prints progress every 10 000 rejections. If sampling stalls, consider increasing `acceptable_error` or simplifying the design.\n- If the enumerator finds zero valid sequences (overconstrained design), generation returns an empty result silently — verify your `CrossBlock` constraints before sampling.'
TOOL_PARAMETERS = { 'properties': { 'acceptable_error': { 'description': 'Maximum number of '
                                                       'crossing-combination '
                                                       'mismatches tolerated before a '
                                                       'candidate sequence is '
                                                       'rejected. Pass 0 for strict '
                                                       'uniform sampling (no '
                                                       'constraint violations '
                                                       'allowed). Increase only for '
                                                       'complex multi-crossing or '
                                                       'window-constrained designs '
                                                       'where strict rejection '
                                                       'sampling is prohibitively slow '
                                                       '— higher values trade '
                                                       'distributional purity for '
                                                       'speed.',
                                        'type': 'integer'}},
  'required': ['acceptable_error'],
  'type': 'object'}
TOOL_NOTES = '- `acceptable_error` has no default and must always be supplied; `0` is the correct value for most designs.\n- The static `RandomGen.sample()` method always uses `acceptable_error=0`; only the instance (produced by this tool) respects a non-zero value via `sample_object`.\n- Rejection sampling on designs with complex windows or multiple crossings can be very slow; the library prints progress every 10 000 rejections. If sampling stalls, consider increasing `acceptable_error` or simplifying the design.\n- If the enumerator finds zero valid sequences (overconstrained design), generation returns an empty result silently — verify your `CrossBlock` constraints before sampling.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.RandomGen
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
    def create_random_gen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a `RandomGen` sampling-strategy handle to pass as the `gen` argument to sequence-generation tools (e.g.'
        return _impl(args or {})
