"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '8999cbf4afdf9ed8a784b5e522fd562a4f1d0984c6893897061f2b4bc92ff80e'
__exp_qualname__ = 'sweetpea.CustomDistribution'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_custom_distribution'
TOOL_DESCRIPTION = 'Call this tool during the SweetPea design phase (step 1) when you need a factor\'s trial-to-trial sampling to follow a user-defined statistical distribution rather than a built-in one. Pass the returned handle to a SweetPea `Factor` or timing distribution slot; the callable `func` is invoked each time SweetPea draws a sample. In cumulative mode the tool accumulates the running sum across samples instead of returning independent draws.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "cumulative": {\n      "default": false,\n      "description": "If true, each call to sample() adds func\'s return value to a running sum and returns the accumulated total instead of the raw sample. Useful for simulating drift or cumulative timing offsets. Defaults to false.",\n      "type": "boolean"\n    },\n    "dependents": {\n      "default": [],\n      "description": "Optional list of Factor handle strings whose sampled levels are forwarded as positional arguments to func on each call. Length must match the number of arguments func expects. Omit or pass [] if func takes no arguments.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "func": {\n      "description": "Handle string pointing to a callable (previously registered in the handle registry) that accepts zero or more float positional arguments (one per dependent factor level) and returns a float sample.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "func"\n  ],\n  "type": "object"\n}\n\nNotes:\n1. `func` is a Python callable, not a plain value — it MUST be supplied as a handle string pointing to a live callable in the handle registry; passing a plain string literal will fail at dispatch.\n2. The constructor\'s `*args[0]` pattern (dependent factors) is flattened into the `dependents` parameter here; the template maps it back to the positional arg before constructing.\n3. In cumulative mode the internal sum is never reset automatically between experiment blocks; call `reset()` on the returned object (via its handle) between blocks to avoid cross-block drift.\n4. `func` must return a numeric float; returning an int is accepted but non-numeric returns raise a TypeError downstream in SweetPea\'s sampler, not at construction time.\n5. Length of `dependents` must exactly match the arity of `func`; a mismatch raises a RuntimeError at sample time, not at construction.'
TOOL_PARAMETERS = { 'properties': { 'cumulative': { 'default': False,
                                  'description': 'If true, each call to sample() adds '
                                                 "func's return value to a running sum "
                                                 'and returns the accumulated total '
                                                 'instead of the raw sample. Useful '
                                                 'for simulating drift or cumulative '
                                                 'timing offsets. Defaults to false.',
                                  'type': 'boolean'},
                  'dependents': { 'default': [],
                                  'description': 'Optional list of Factor handle '
                                                 'strings whose sampled levels are '
                                                 'forwarded as positional arguments to '
                                                 'func on each call. Length must match '
                                                 'the number of arguments func '
                                                 'expects. Omit or pass [] if func '
                                                 'takes no arguments.',
                                  'items': {'type': 'string'},
                                  'type': 'array'},
                  'func': { 'description': 'Handle string pointing to a callable '
                                           '(previously registered in the handle '
                                           'registry) that accepts zero or more float '
                                           'positional arguments (one per dependent '
                                           'factor level) and returns a float sample.',
                            'type': 'string'}},
  'required': ['func'],
  'type': 'object'}
TOOL_NOTES = "1. `func` is a Python callable, not a plain value — it MUST be supplied as a handle string pointing to a live callable in the handle registry; passing a plain string literal will fail at dispatch.\n2. The constructor's `*args[0]` pattern (dependent factors) is flattened into the `dependents` parameter here; the template maps it back to the positional arg before constructing.\n3. In cumulative mode the internal sum is never reset automatically between experiment blocks; call `reset()` on the returned object (via its handle) between blocks to avoid cross-block drift.\n4. `func` must return a numeric float; returning an int is accepted but non-numeric returns raise a TypeError downstream in SweetPea's sampler, not at construction time.\n5. Length of `dependents` must exactly match the arity of `func`; a mismatch raises a RuntimeError at sample time, not at construction."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.CustomDistribution
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
    def create_custom_distribution(args: dict[str, Any] | None = None) -> Any:
        "Call this tool during the SweetPea design phase (step 1) when you need a factor's trial-to-trial sampling to follow a user-defined statistical distribution rather than a built-in one."
        return _impl(args or {})
