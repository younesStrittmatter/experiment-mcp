"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '5894a5ad5ad734e49c540b818be8ce178c85f27026e0f3522ce27f18b825ac3d'
__exp_qualname__ = 'sweetpea.Factor'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_factor'
TOOL_DESCRIPTION = 'Call this tool at the start of a SweetPea experimental design to declare an independent variable and its possible values (levels). The result is a Factor handle — pass it to CrossBlock or a constraint tool to define the crossing and trial-sequence structure. Use before any block, constraint, or sequence-generation step.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "initial_levels": {\n      "description": "The discrete values this factor can take. Each item may be: a plain string (becomes a SimpleLevel), a two-element array [name, weight] for a weighted SimpleLevel, or a handle string pointing to a DerivedLevel or ElseLevel object produced by another tool. If the first item is a DerivedLevel or ElseLevel handle, a DerivedFactor is created automatically; otherwise a SimpleFactor is created.",\n      "items": {\n        "oneOf": [\n          {\n            "description": "Level name or handle string to an existing Level object.",\n            "type": "string"\n          },\n          {\n            "description": "Weighted simple level: [level_name, weight].",\n            "maxItems": 2,\n            "minItems": 2,\n            "prefixItems": [\n              {\n                "type": "string"\n              },\n              {\n                "minimum": 1,\n                "type": "integer"\n              }\n            ],\n            "type": "array"\n          }\n        ]\n      },\n      "minItems": 1,\n      "type": "array"\n    },\n    "name": {\n      "description": "Display name for this factor (e.g. \'color\', \'congruency\'). Must be a non-empty string; used as a column header in the sampled trial sequence.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "name",\n    "initial_levels"\n  ],\n  "type": "object"\n}\n\nNotes:\nAt least one level is required; passing an empty list raises ValueError. Factor equality is identity-based (not name-based), so two Factor calls with the same name produce distinct objects — do not recreate a factor when you mean to reuse it; store and pass the handle instead. If the very first element of initial_levels is a DerivedLevel or ElseLevel handle, the result is a DerivedFactor with transition/window semantics; all other elements must also be DerivedLevel or ElseLevel handles in that case. Duplicate level names within a single factor raise ValueError unless the levels are synthesized internally by SweetPea.'
TOOL_PARAMETERS = { 'properties': { 'initial_levels': { 'description': 'The discrete values this factor '
                                                     'can take. Each item may be: a '
                                                     'plain string (becomes a '
                                                     'SimpleLevel), a two-element '
                                                     'array [name, weight] for a '
                                                     'weighted SimpleLevel, or a '
                                                     'handle string pointing to a '
                                                     'DerivedLevel or ElseLevel object '
                                                     'produced by another tool. If the '
                                                     'first item is a DerivedLevel or '
                                                     'ElseLevel handle, a '
                                                     'DerivedFactor is created '
                                                     'automatically; otherwise a '
                                                     'SimpleFactor is created.',
                                      'items': { 'oneOf': [ { 'description': 'Level '
                                                                             'name or '
                                                                             'handle '
                                                                             'string '
                                                                             'to an '
                                                                             'existing '
                                                                             'Level '
                                                                             'object.',
                                                              'type': 'string'},
                                                            { 'description': 'Weighted '
                                                                             'simple '
                                                                             'level: '
                                                                             '[level_name, '
                                                                             'weight].',
                                                              'maxItems': 2,
                                                              'minItems': 2,
                                                              'prefixItems': [ { 'type': 'string'},
                                                                               { 'minimum': 1,
                                                                                 'type': 'integer'}],
                                                              'type': 'array'}]},
                                      'minItems': 1,
                                      'type': 'array'},
                  'name': { 'description': 'Display name for this factor (e.g. '
                                           "'color', 'congruency'). Must be a "
                                           'non-empty string; used as a column header '
                                           'in the sampled trial sequence.',
                            'type': 'string'}},
  'required': ['name', 'initial_levels'],
  'type': 'object'}
TOOL_NOTES = 'At least one level is required; passing an empty list raises ValueError. Factor equality is identity-based (not name-based), so two Factor calls with the same name produce distinct objects — do not recreate a factor when you mean to reuse it; store and pass the handle instead. If the very first element of initial_levels is a DerivedLevel or ElseLevel handle, the result is a DerivedFactor with transition/window semantics; all other elements must also be DerivedLevel or ElseLevel handles in that case. Duplicate level names within a single factor raise ValueError unless the levels are synthesized internally by SweetPea.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Factor
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
    def create_factor(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at the start of a SweetPea experimental design to declare an independent variable and its possible values (levels).'
        return _impl(args or {})
