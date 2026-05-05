"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'bf032c3d8d075c47ab91410772e1b6c1673c0b567f8a93407bad004e35c305d5'
__exp_qualname__ = 'sweetpea.DerivedLevel'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_derived_level'
TOOL_DESCRIPTION = 'Call this tool during the SweetPea factor-definition phase (step 1 of the pipeline) when a level\'s identity depends on the values of other factors in the same or previous trials — for example, "congruent" when color and word match, or "repeat" when the current stimulus matches the previous one. Pass a Window handle (produced by the sweetpea_window tool) that encodes the predicate and the factors it ranges over. Returns a DerivedLevel handle that can be passed into a DerivedFactor alongside other DerivedLevel handles.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "Human-readable label for this level (e.g. \'congruent\', \'repeat\', \'switch\'). Used in sampled trial sequences and SweetBean stimulus bindings.",\n      "type": "string"\n    },\n    "weight": {\n      "default": 1,\n      "description": "Relative sampling weight for this level. Defaults to 1 (equal probability). A weight of 2 makes this level appear twice as often as a weight-1 sibling.",\n      "type": "integer"\n    },\n    "window": {\n      "description": "Handle string for a Window object produced by the sweetpea_window tool. Encodes the predicate function, the factors it draws from, and the sliding-window width/stride/start.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "name",\n    "window"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `window` argument MUST be a Window instance — passing a plain factor or level handle will raise TypeError at construction time. Factors referenced inside the Window must not have stride > 1 in their own complex windows; SweetPea raises ValueError if they do. The `weight` parameter shifts sampling frequency but does not affect the logical cross product — all level combinations remain reachable. DerivedLevel depth is computed automatically from its dependency graph; do not try to control evaluation order manually.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'Human-readable label for this level (e.g. '
                                           "'congruent', 'repeat', 'switch'). Used in "
                                           'sampled trial sequences and SweetBean '
                                           'stimulus bindings.',
                            'type': 'string'},
                  'weight': { 'default': 1,
                              'description': 'Relative sampling weight for this level. '
                                             'Defaults to 1 (equal probability). A '
                                             'weight of 2 makes this level appear '
                                             'twice as often as a weight-1 sibling.',
                              'type': 'integer'},
                  'window': { 'description': 'Handle string for a Window object '
                                             'produced by the sweetpea_window tool. '
                                             'Encodes the predicate function, the '
                                             'factors it draws from, and the '
                                             'sliding-window width/stride/start.',
                              'type': 'string'}},
  'required': ['name', 'window'],
  'type': 'object'}
TOOL_NOTES = 'The `window` argument MUST be a Window instance — passing a plain factor or level handle will raise TypeError at construction time. Factors referenced inside the Window must not have stride > 1 in their own complex windows; SweetPea raises ValueError if they do. The `weight` parameter shifts sampling frequency but does not affect the logical cross product — all level combinations remain reachable. DerivedLevel depth is computed automatically from its dependency graph; do not try to control evaluation order manually.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.DerivedLevel
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
    def create_derived_level(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during the SweetPea factor-definition phase (step 1 of the pipeline) when a level\'s identity depends on the values of other factors in the same or previous trials — for example, "congruent" when color and word match, or "repeat" when the current stimulus matches the previous one.'
        return _impl(args or {})
