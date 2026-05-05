"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'd21c9738d487280f673e68cc339bde5aca0eab1cf347d81e0db33fba70ff627d'
__exp_qualname__ = 'sweetpea.Derivation'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_derivation'
TOOL_DESCRIPTION = 'Call this tool only when you need to manually construct a low-level SAT-encoding constraint that links a derived level (by its internal boolean variable index) to its dependency indices. This is an internal SweetPea class — in nearly all workflows, `DerivedFactor` with a derivation function is the correct entry point; reach for `Derivation` only if you are directly manipulating SweetPea\'s constraint backend or inspecting/reconstructing existing derivation objects. Returns a handle to a `Derivation` constraint object that can be passed to backend-level APIs.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "dependent_idxs": {\n      "description": "The dependency formula expressed as a list of AND-groups that are OR-ed together, i.e. `[[0, 2], [1, 3]]` encodes `(0 AND 2) OR (1 AND 3)`. Each inner list is one AND-clause of internal variable indices.",\n      "items": {\n        "items": {\n          "type": "integer"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "derived_idx": {\n      "description": "The internal boolean-variable index of the derived level in SweetPea\'s SAT encoding. This is a 0-based offset into the per-trial variable block, NOT a user-facing factor or level index.",\n      "type": "integer"\n    },\n    "factor": {\n      "description": "Handle string referencing the `DerivedFactor` this derivation belongs to, as returned by a prior tool that constructed or resolved a DerivedFactor.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "derived_idx",\n    "dependent_idxs",\n    "factor"\n  ],\n  "type": "object"\n}\n\nNotes:\nThis is `sweetpea._internal.constraint.Derivation` — an internal implementation class, not part of the public API. Typical agent workflows never construct `Derivation` directly; use `DerivedFactor` + a Python derivation function instead, and let SweetPea build the `Derivation` objects automatically during compilation. The indices in `derived_idx` and `dependent_idxs` refer to SweetPea\'s internal SAT boolean-variable numbering (0-based offsets into the per-trial variable block), which has no stable correspondence to user-visible factor or level indices without inspecting `block.grid_variables()` and `block.variables_per_trial()`. Window-based derivations involving `BeforeStart` sentinel values cannot be fully expressed through this JSON interface because `BeforeStart` objects are not serializable; those cases must go through the normal `DerivedFactor` API.'
TOOL_PARAMETERS = { 'properties': { 'dependent_idxs': { 'description': 'The dependency formula expressed '
                                                     'as a list of AND-groups that are '
                                                     'OR-ed together, i.e. `[[0, 2], '
                                                     '[1, 3]]` encodes `(0 AND 2) OR '
                                                     '(1 AND 3)`. Each inner list is '
                                                     'one AND-clause of internal '
                                                     'variable indices.',
                                      'items': { 'items': {'type': 'integer'},
                                                 'type': 'array'},
                                      'type': 'array'},
                  'derived_idx': { 'description': 'The internal boolean-variable index '
                                                  "of the derived level in SweetPea's "
                                                  'SAT encoding. This is a 0-based '
                                                  'offset into the per-trial variable '
                                                  'block, NOT a user-facing factor or '
                                                  'level index.',
                                   'type': 'integer'},
                  'factor': { 'description': 'Handle string referencing the '
                                             '`DerivedFactor` this derivation belongs '
                                             'to, as returned by a prior tool that '
                                             'constructed or resolved a DerivedFactor.',
                              'type': 'string'}},
  'required': ['derived_idx', 'dependent_idxs', 'factor'],
  'type': 'object'}
TOOL_NOTES = "This is `sweetpea._internal.constraint.Derivation` — an internal implementation class, not part of the public API. Typical agent workflows never construct `Derivation` directly; use `DerivedFactor` + a Python derivation function instead, and let SweetPea build the `Derivation` objects automatically during compilation. The indices in `derived_idx` and `dependent_idxs` refer to SweetPea's internal SAT boolean-variable numbering (0-based offsets into the per-trial variable block), which has no stable correspondence to user-visible factor or level indices without inspecting `block.grid_variables()` and `block.variables_per_trial()`. Window-based derivations involving `BeforeStart` sentinel values cannot be fully expressed through this JSON interface because `BeforeStart` objects are not serializable; those cases must go through the normal `DerivedFactor` API."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Derivation
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
    def create_derivation(args: dict[str, Any] | None = None) -> Any:
        'Call this tool only when you need to manually construct a low-level SAT-encoding constraint that links a derived level (by its internal boolean variable index) to its dependency indices.'
        return _impl(args or {})
