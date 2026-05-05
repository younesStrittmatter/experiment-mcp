"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '4a5a7b8ff10ad02495f58c9cce10b0bbca3481002a36371befbd93944a003434'
__exp_qualname__ = 'sweetpea.ContinuousFactor'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_continuous_factor'
TOOL_DESCRIPTION = 'Call this tool during the SweetPea design phase (step 1) when you need a factor whose values are drawn from a statistical distribution rather than from a fixed discrete set. Use it in place of a plain `Factor` whenever trial-level values should vary continuously — e.g., stimulus onset asynchrony drawn from a uniform distribution, or a response-time prior. Returns a handle string referencing a `ContinuousFactor` object that can be passed to `CrossBlock` or `MultiCrossBlock` alongside ordinary discrete factors.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "distribution": {\n      "description": "Handle string referencing a Distribution object produced by a distribution-constructor tool (e.g. sweetpea_uniform_distribution, sweetpea_normal_distribution). The Distribution controls how values are sampled and which dependency factors or ContinuousFactorWindows it consumes.",\n      "type": "string"\n    },\n    "name": {\n      "description": "Human-readable name for this factor (e.g. \'stimulus_duration\'). Must be unique among all factors in the design.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "name",\n    "distribution"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `distribution` argument is mandatory and must resolve to a `Distribution` instance — passing anything else raises `ValueError` at construction time. `initial_levels` is derived automatically from `distribution.get_init()` and cannot be set directly; every element returned must be either a `Factor` handle or a `ContinuousFactorWindow` handle, otherwise construction fails. The factor exposes a single hidden level internally, so it will not appear as a discrete level list in design-graph output. `__hash__` is based solely on `name`, so two `ContinuousFactor` objects with the same name are considered identical in sets/dicts.'
TOOL_PARAMETERS = { 'properties': { 'distribution': { 'description': 'Handle string referencing a '
                                                   'Distribution object produced by a '
                                                   'distribution-constructor tool '
                                                   '(e.g. '
                                                   'sweetpea_uniform_distribution, '
                                                   'sweetpea_normal_distribution). The '
                                                   'Distribution controls how values '
                                                   'are sampled and which dependency '
                                                   'factors or ContinuousFactorWindows '
                                                   'it consumes.',
                                    'type': 'string'},
                  'name': { 'description': 'Human-readable name for this factor (e.g. '
                                           "'stimulus_duration'). Must be unique among "
                                           'all factors in the design.',
                            'type': 'string'}},
  'required': ['name', 'distribution'],
  'type': 'object'}
TOOL_NOTES = 'The `distribution` argument is mandatory and must resolve to a `Distribution` instance — passing anything else raises `ValueError` at construction time. `initial_levels` is derived automatically from `distribution.get_init()` and cannot be set directly; every element returned must be either a `Factor` handle or a `ContinuousFactorWindow` handle, otherwise construction fails. The factor exposes a single hidden level internally, so it will not appear as a discrete level list in design-graph output. `__hash__` is based solely on `name`, so two `ContinuousFactor` objects with the same name are considered identical in sets/dicts.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.ContinuousFactor
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
    def create_continuous_factor(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during the SweetPea design phase (step 1) when you need a factor whose values are drawn from a statistical distribution rather than from a fixed discrete set.'
        return _impl(args or {})
