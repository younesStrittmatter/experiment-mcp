"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'c2d1f28d8c2a1f71d310f78564e59de66bc819f1303bf96a2b1f2353b566e749'
__exp_qualname__ = 'sweetpea.ContinuousFactorWindow'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_continuous_factor_window'
TOOL_DESCRIPTION = 'Call this tool during SweetPea design declaration (step 1 of the pipeline) when you need a derived continuous factor whose value depends on a sliding window of previous trial values — e.g., a recency signal, a running delta, or a lag-N predictor. Pass the resulting handle to a ContinuousFactor\'s derivation function so SweetPea can resolve the window during sequence sampling.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "factors": {\n      "description": "Handle strings for the ContinuousFactor objects whose past values this window should expose. Every element must resolve to a ContinuousFactor; other factor types raise TypeError.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "start": {\n      "description": "Zero-based trial index at which the window first becomes active. Trials before this index return NaN-filled dicts. Omit to use the default of width-1 (window activates once a full width of prior trials exists).",\n      "type": "integer"\n    },\n    "stride": {\n      "default": 1,\n      "description": "Step size between active window positions. Trials whose index does not land on a stride boundary return NaN-filled dicts. Defaults to 1 (every trial is active).",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "width": {\n      "description": "Number of consecutive trials (including the current one) to include in the window. A width of 3 exposes the current trial and the two immediately preceding it.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "factors",\n    "width"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `start` silently defaults to `width - 1` when omitted; this means the very first (width-1) trials always yield NaN dicts regardless of stride. Pass an explicit value only if you need the window to activate earlier or later than that.\n- With stride > 1, any trial where `(idx - start) % stride != 0` also returns a NaN dict, even if idx >= start and idx >= width-1. Account for this when writing the derivation function that consumes the window.\n- The window dict uses *negative* integer keys: `{0: current, -1: one back, -2: two back, …}`. Your derivation function must index with negative integers, not zero-based positives.\n- When `factors` contains a single element the return value is a single dict; when it contains two or more, the return value is a list of dicts in the same order. Your derivation function must handle both arities.\n- Only `ContinuousFactor` handles are accepted; passing a `Factor` (discrete) raises `TypeError` at construction time, not at sampling time.'
TOOL_PARAMETERS = { 'properties': { 'factors': { 'description': 'Handle strings for the ContinuousFactor '
                                              'objects whose past values this window '
                                              'should expose. Every element must '
                                              'resolve to a ContinuousFactor; other '
                                              'factor types raise TypeError.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'start': { 'description': 'Zero-based trial index at which the '
                                            'window first becomes active. Trials '
                                            'before this index return NaN-filled '
                                            'dicts. Omit to use the default of width-1 '
                                            '(window activates once a full width of '
                                            'prior trials exists).',
                             'type': 'integer'},
                  'stride': { 'default': 1,
                              'description': 'Step size between active window '
                                             'positions. Trials whose index does not '
                                             'land on a stride boundary return '
                                             'NaN-filled dicts. Defaults to 1 (every '
                                             'trial is active).',
                              'minimum': 1,
                              'type': 'integer'},
                  'width': { 'description': 'Number of consecutive trials (including '
                                            'the current one) to include in the '
                                            'window. A width of 3 exposes the current '
                                            'trial and the two immediately preceding '
                                            'it.',
                             'minimum': 1,
                             'type': 'integer'}},
  'required': ['factors', 'width'],
  'type': 'object'}
TOOL_NOTES = '- `start` silently defaults to `width - 1` when omitted; this means the very first (width-1) trials always yield NaN dicts regardless of stride. Pass an explicit value only if you need the window to activate earlier or later than that.\n- With stride > 1, any trial where `(idx - start) % stride != 0` also returns a NaN dict, even if idx >= start and idx >= width-1. Account for this when writing the derivation function that consumes the window.\n- The window dict uses *negative* integer keys: `{0: current, -1: one back, -2: two back, …}`. Your derivation function must index with negative integers, not zero-based positives.\n- When `factors` contains a single element the return value is a single dict; when it contains two or more, the return value is a list of dicts in the same order. Your derivation function must handle both arities.\n- Only `ContinuousFactor` handles are accepted; passing a `Factor` (discrete) raises `TypeError` at construction time, not at sampling time.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.ContinuousFactorWindow
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
    def create_continuous_factor_window(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during SweetPea design declaration (step 1 of the pipeline) when you need a derived continuous factor whose value depends on a sliding window of previous trial values — e.g., a recency signal, a running delta, or a lag-N predictor.'
        return _impl(args or {})
