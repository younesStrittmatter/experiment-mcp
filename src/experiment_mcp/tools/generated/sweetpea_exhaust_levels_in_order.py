"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'a7c0f9314effdd31a2b5b82da3d10cd398dd046ef76fd575a2aee6ee6e777b62'
__exp_qualname__ = 'sweetpea.ExhaustLevelsInOrder'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_exhaust_levels_in_order'
TOOL_DESCRIPTION = 'Call this tool during SweetPea experimental design (step 1 of the pipeline, before sampling) when you need to enforce a strict sequential block structure across levels of a factor — e.g., all "practice" trials before all "test" trials, or all low-difficulty trials before all high-difficulty trials. Pass the returned constraint object handle to `CrossBlock` or `MultiCrossBlock` alongside other constraints. The result is a constraint handle that the SAT solver uses to partition the trial sequence into contiguous, ordered level-blocks.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "factor": {\n      "description": "Handle string returned by a factor-creation tool (e.g. sweetpea_factor). The factor whose levels must be exhausted in order. Must have at least 2 levels and must not have a complex window (no transition or window factors).",\n      "type": "string"\n    },\n    "order": {\n      "description": "Exact sequence in which levels should be exhausted. Must contain every level name of the factor exactly once \\u2014 no omissions, no duplicates. Example: [\'practice\', \'test\'] means all practice trials appear before any test trial.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "factor",\n    "order"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `order` list must include ALL levels of the factor with no duplicates — passing a partial list raises a ValueError at construction time. This constraint is incompatible with factors that have complex windows (transitions, window-based derivations); use only on simple factors. The constraint uses SAT auxiliary variables internally and is marked `is_complex_for_combinatoric`, so it may increase solve time on large designs.'
TOOL_PARAMETERS = { 'properties': { 'factor': { 'description': 'Handle string returned by a '
                                             'factor-creation tool (e.g. '
                                             'sweetpea_factor). The factor whose '
                                             'levels must be exhausted in order. Must '
                                             'have at least 2 levels and must not have '
                                             'a complex window (no transition or '
                                             'window factors).',
                              'type': 'string'},
                  'order': { 'description': 'Exact sequence in which levels should be '
                                            'exhausted. Must contain every level name '
                                            'of the factor exactly once — no '
                                            'omissions, no duplicates. Example: '
                                            "['practice', 'test'] means all practice "
                                            'trials appear before any test trial.',
                             'items': {'type': 'string'},
                             'type': 'array'}},
  'required': ['factor', 'order'],
  'type': 'object'}
TOOL_NOTES = 'The `order` list must include ALL levels of the factor with no duplicates — passing a partial list raises a ValueError at construction time. This constraint is incompatible with factors that have complex windows (transitions, window-based derivations); use only on simple factors. The constraint uses SAT auxiliary variables internally and is marked `is_complex_for_combinatoric`, so it may increase solve time on large designs.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.ExhaustLevelsInOrder
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
    def create_exhaust_levels_in_order(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during SweetPea experimental design (step 1 of the pipeline, before sampling) when you need to enforce a strict sequential block structure across levels of a factor — e.g., all "practice" trials before all "test" trials, or all low-difficulty trials before all high-difficulty trials.'
        return _impl(args or {})
