"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '59ab3cc45146f09d7f6f1da481486db23f4f0151cc5491c5427425a4141c3dae'
__exp_qualname__ = 'sweetpea.ElseLevel'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_else_level'
TOOL_DESCRIPTION = 'Call this tool when defining a derived factor that needs a catch-all "else" level — a level that activates whenever none of the other DerivedLevels\' predicates match, analogous to an else-branch in conditional logic. Use it in SweetPea\'s factor-construction phase (step 1 of the pipeline) after defining the positive DerivedLevels for a factor, to ensure complete coverage of the trial space. The result is an ElseLevel object (returned as a handle string) that you pass alongside your DerivedLevel handles when constructing a Factor.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "description": "The name of this catch-all level, e.g. \'other\' or \'else\'. Appears in the sampled trial sequence output.",\n      "type": "string"\n    },\n    "weight": {\n      "default": 1,\n      "description": "Relative sampling weight for this level. Defaults to 1. Higher values increase how often this level appears in the generated trial sequence relative to other levels in the same factor.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "name"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe SweetPea source contains a TODO noting that the precise semantics of ElseLevel are unclear to the library authors — treat it as a logical complement: its predicate evaluates to true when *none* of the DerivedLevels it is paired with (via `derive_level_from_levels`) are active for a given trial. The ElseLevel must be passed to a Factor together with the DerivedLevel handles it complements; it cannot stand alone. Weight applies only after `derive_level_from_levels` converts it into a DerivedLevel internally — passing weight here is equivalent to weighting the derived catch-all case.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'description': 'The name of this catch-all level, e.g. '
                                           "'other' or 'else'. Appears in the sampled "
                                           'trial sequence output.',
                            'type': 'string'},
                  'weight': { 'default': 1,
                              'description': 'Relative sampling weight for this level. '
                                             'Defaults to 1. Higher values increase '
                                             'how often this level appears in the '
                                             'generated trial sequence relative to '
                                             'other levels in the same factor.',
                              'type': 'integer'}},
  'required': ['name'],
  'type': 'object'}
TOOL_NOTES = 'The SweetPea source contains a TODO noting that the precise semantics of ElseLevel are unclear to the library authors — treat it as a logical complement: its predicate evaluates to true when *none* of the DerivedLevels it is paired with (via `derive_level_from_levels`) are active for a given trial. The ElseLevel must be passed to a Factor together with the DerivedLevel handles it complements; it cannot stand alone. Weight applies only after `derive_level_from_levels` converts it into a DerivedLevel internally — passing weight here is equivalent to weighting the derived catch-all case.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.ElseLevel
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
    def create_else_level(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when defining a derived factor that needs a catch-all "else" level — a level that activates whenever none of the other DerivedLevels\' predicates match, analogous to an else-branch in conditional logic.'
        return _impl(args or {})
