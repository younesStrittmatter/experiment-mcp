"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '5dbc835589d3ebf4c5776da9c85fdf3d6181f4372e5aaa292cd441b98ccb2b47'
__exp_qualname__ = 'sweetpea.Window'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_window'
TOOL_DESCRIPTION = 'Call this tool during SweetPea design construction when you need a derived factor that inspects values across the current trial and one or more preceding trials — for example, to flag repetitions, label transitions, or implement any look-back logic. Provide a callable predicate (as a handle), the Factor handles it will receive, and the window size; pass the returned Window handle as the `window` argument to a derivation class such as `WithinTrial` or `Transition`. The result is a handle to a `sweetpea.Window` object.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "factors": {\n      "description": "Ordered list of handle strings for the sweetpea.Factor objects this window depends on. No factor may appear more than once.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "predicate": {\n      "description": "Handle string for a callable previously registered in the handle registry. The function receives one argument per factor per trial in the window (width \\u00d7 len(factors) values) and returns a bool. Argument types vary by derivation subclass \\u2014 check that subclass\'s docs.",\n      "type": "string"\n    },\n    "start": {\n      "description": "0-based index of the first trial where this derivation applies. Omit to let SweetPea auto-compute the earliest trial where all dependent factors are defined. If set earlier than that auto value, the predicate must handle None for undefined levels.",\n      "minimum": 0,\n      "type": "integer"\n    },\n    "stride": {\n      "default": 1,\n      "description": "How often the factor is derived. stride=1 (default) derives on every trial; stride=N skips N-1 trials between derivations.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "width": {\n      "description": "Number of consecutive trials this window spans, including the current trial. Must be >= 1. Use width > 1 for transition- or repetition-style derivations.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "predicate",\n    "factors",\n    "width"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `predicate` must be a handle string pointing to a Python callable registered in the handle registry — raw Python functions cannot be serialized through MCP JSON. The number of arguments the predicate receives equals `width × len(factors)` (factors vary fastest, then trials from oldest to current). `start` defaults to `width - 1` plus any additional delay imposed by complex dependent factors; only override it if you specifically need the predicate to run on earlier trials and are prepared to handle `None` arguments. Repeated Factor handles in `factors` raise a ValueError at construction time. This class is a low-level building block; most agents should prefer the higher-level `Transition` or `WithinTrial` derivation constructors that wrap Window automatically.'
TOOL_PARAMETERS = { 'properties': { 'factors': { 'description': 'Ordered list of handle strings for the '
                                              'sweetpea.Factor objects this window '
                                              'depends on. No factor may appear more '
                                              'than once.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'predicate': { 'description': 'Handle string for a callable '
                                                'previously registered in the handle '
                                                'registry. The function receives one '
                                                'argument per factor per trial in the '
                                                'window (width × len(factors) values) '
                                                'and returns a bool. Argument types '
                                                'vary by derivation subclass — check '
                                                "that subclass's docs.",
                                 'type': 'string'},
                  'start': { 'description': '0-based index of the first trial where '
                                            'this derivation applies. Omit to let '
                                            'SweetPea auto-compute the earliest trial '
                                            'where all dependent factors are defined. '
                                            'If set earlier than that auto value, the '
                                            'predicate must handle None for undefined '
                                            'levels.',
                             'minimum': 0,
                             'type': 'integer'},
                  'stride': { 'default': 1,
                              'description': 'How often the factor is derived. '
                                             'stride=1 (default) derives on every '
                                             'trial; stride=N skips N-1 trials between '
                                             'derivations.',
                              'minimum': 1,
                              'type': 'integer'},
                  'width': { 'description': 'Number of consecutive trials this window '
                                            'spans, including the current trial. Must '
                                            'be >= 1. Use width > 1 for transition- or '
                                            'repetition-style derivations.',
                             'minimum': 1,
                             'type': 'integer'}},
  'required': ['predicate', 'factors', 'width'],
  'type': 'object'}
TOOL_NOTES = 'The `predicate` must be a handle string pointing to a Python callable registered in the handle registry — raw Python functions cannot be serialized through MCP JSON. The number of arguments the predicate receives equals `width × len(factors)` (factors vary fastest, then trials from oldest to current). `start` defaults to `width - 1` plus any additional delay imposed by complex dependent factors; only override it if you specifically need the predicate to run on earlier trials and are prepared to handle `None` arguments. Repeated Factor handles in `factors` raise a ValueError at construction time. This class is a low-level building block; most agents should prefer the higher-level `Transition` or `WithinTrial` derivation constructors that wrap Window automatically.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Window
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
    def create_window(args: dict[str, Any] | None = None) -> Any:
        'Call this tool during SweetPea design construction when you need a derived factor that inspects values across the current trial and one or more preceding trials — for example, to flag repetitions, label transitions, or implement any look-back logic.'
        return _impl(args or {})
