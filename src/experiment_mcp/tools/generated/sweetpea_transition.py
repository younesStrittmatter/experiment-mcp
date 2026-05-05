"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '8fa5288ec6307d506282f6260e066bc52a7d88b2a23359854ec3e84deca78de3'
__exp_qualname__ = 'sweetpea.Transition'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_transition'
TOOL_DESCRIPTION = 'Call this tool during SweetPea design declaration (step 1 of the pipeline) when you need a derived level whose value depends on the transition between two consecutive trials — for example "repeat vs. switch" or "same color as previous trial." The result is a handle to a `Transition` window object; pass it as the `window` argument to `DerivedLevel` together with a predicate that inspects the paired factor levels. Do not use this tool for within-trial derivations (use `Window` directly) or for derivations that look more than one trial back (use `Window` with a larger width).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "factors": {\n      "description": "Ordered list of handle strings referencing the Factor objects this derivation window depends on. Each factor handle must have been produced by a prior `sweetpea_factor` tool call. The order must match the positional arguments expected by `predicate`.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "predicate": {\n      "description": "Handle string referencing a Python callable (registered in the handle registry by a prior tool call) that accepts one sequence-of-levels argument per factor listed in `factors` and returns a bool. The callable receives two elements per factor sequence \\u2014 the value from the preceding trial followed by the value from the current trial \\u2014 because the window width is fixed at 2.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "predicate",\n    "factors"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `width`, `stride`, and `start` fields are fixed at 2, 1, and 1 respectively and are not exposed as parameters — they encode the "look back exactly one trial" semantics of a transition. Because `predicate` must be a live Python callable, you cannot pass an inline lambda as JSON; you must first register the callable via a handle-producing tool (or a prior tool call that stored the function) and pass the resulting handle string here. If no such tool exists in the current session, this tool cannot be called — note the limitation to the user and ask them to provide the predicate via a different mechanism.'
TOOL_PARAMETERS = { 'properties': { 'factors': { 'description': 'Ordered list of handle strings '
                                              'referencing the Factor objects this '
                                              'derivation window depends on. Each '
                                              'factor handle must have been produced '
                                              'by a prior `sweetpea_factor` tool call. '
                                              'The order must match the positional '
                                              'arguments expected by `predicate`.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'predicate': { 'description': 'Handle string referencing a Python '
                                                'callable (registered in the handle '
                                                'registry by a prior tool call) that '
                                                'accepts one sequence-of-levels '
                                                'argument per factor listed in '
                                                '`factors` and returns a bool. The '
                                                'callable receives two elements per '
                                                'factor sequence — the value from the '
                                                'preceding trial followed by the value '
                                                'from the current trial — because the '
                                                'window width is fixed at 2.',
                                 'type': 'string'}},
  'required': ['predicate', 'factors'],
  'type': 'object'}
TOOL_NOTES = 'The `width`, `stride`, and `start` fields are fixed at 2, 1, and 1 respectively and are not exposed as parameters — they encode the "look back exactly one trial" semantics of a transition. Because `predicate` must be a live Python callable, you cannot pass an inline lambda as JSON; you must first register the callable via a handle-producing tool (or a prior tool call that stored the function) and pass the resulting handle string here. If no such tool exists in the current session, this tool cannot be called — note the limitation to the user and ask them to provide the predicate via a different mechanism.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Transition
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
    def create_transition(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during SweetPea design declaration (step 1 of the pipeline) when you need a derived level whose value depends on the transition between two consecutive trials — for example "repeat vs.'
        return _impl(args or {})
