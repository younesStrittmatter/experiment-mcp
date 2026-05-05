"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'ef247d5f7bf5a5b3a376aedd76c43c67c315492b2910d03b6435d4917568e234'
__exp_qualname__ = 'sweetbean.Experiment.run_on_language'
__exp_kind__ = 'method'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'run_on_language'
TOOL_DESCRIPTION = 'Call this at step 4 of the SweetPea→SweetBean pipeline, after building an Experiment from SweetBean blocks wired to a SweetPea-sampled timeline, when you want to drive the experiment as a text-based conversation rather than compiling to HTML. Each trial\'s stimuli are serialized into prompts and responses are collected in sequence; the tool returns a tuple `(out_data, prompts)` where `out_data` is a list of per-trial dicts with collected responses and `prompts` is the full accumulated prompt history. Use it for LLM-in-the-loop simulation, headless piloting, or replaying an existing dataset by passing prior trial records via `data`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "data": {\n      "description": "Optional list of prior trial-response dicts to replay. If provided and shorter than the full experiment, remaining trials are simulated live. Omit to run the entire experiment interactively.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "experiment": {\n      "description": "Handle string for the Experiment instance, as returned by the sweetbean_experiment constructor tool.",\n      "type": "string"\n    },\n    "multi_turn": {\n      "default": false,\n      "description": "If false (default), all prior prompts are concatenated into a single context before each trial. If true, each trial is presented as a fresh turn without prior context.",\n      "type": "boolean"\n    },\n    "preamble": {\n      "default": "",\n      "description": "Fixed text prepended to every prompt before the trial content. Use to set persona, instructions, or task framing.",\n      "type": "string"\n    },\n    "response_close_token": {\n      "default": ">>",\n      "description": "Token appended after the model or user response in stored prompt history.",\n      "type": "string"\n    },\n    "response_open_token": {\n      "default": "<<",\n      "description": "Token inserted into prompt templates to mark where the response begins.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "experiment"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `get_input` parameter (a Python callable) cannot be passed through MCP\'s JSON interface and is intentionally omitted from this schema. In a server/headless context the omitted default (`builtins.input`) will block waiting for stdin — this tool is only safe to call with `data` pre-populated for the full experiment (pure replay mode), or when the calling environment can service stdin. For LLM-driven simulation, pre-collect responses and pass them via `data` rather than attempting to wire a live LLM callable. The return value is a two-element tuple `(out_data, prompts)`; the handle registry stores the full tuple, so downstream tools should index into it to retrieve just the trial records or just the prompt log.'
TOOL_PARAMETERS = { 'properties': { 'data': { 'description': 'Optional list of prior trial-response '
                                           'dicts to replay. If provided and shorter '
                                           'than the full experiment, remaining trials '
                                           'are simulated live. Omit to run the entire '
                                           'experiment interactively.',
                            'items': {'type': 'object'},
                            'type': 'array'},
                  'experiment': { 'description': 'Handle string for the Experiment '
                                                 'instance, as returned by the '
                                                 'sweetbean_experiment constructor '
                                                 'tool.',
                                  'type': 'string'},
                  'multi_turn': { 'default': False,
                                  'description': 'If false (default), all prior '
                                                 'prompts are concatenated into a '
                                                 'single context before each trial. If '
                                                 'true, each trial is presented as a '
                                                 'fresh turn without prior context.',
                                  'type': 'boolean'},
                  'preamble': { 'default': '',
                                'description': 'Fixed text prepended to every prompt '
                                               'before the trial content. Use to set '
                                               'persona, instructions, or task '
                                               'framing.',
                                'type': 'string'},
                  'response_close_token': { 'default': '>>',
                                            'description': 'Token appended after the '
                                                           'model or user response in '
                                                           'stored prompt history.',
                                            'type': 'string'},
                  'response_open_token': { 'default': '<<',
                                           'description': 'Token inserted into prompt '
                                                          'templates to mark where the '
                                                          'response begins.',
                                           'type': 'string'}},
  'required': ['experiment'],
  'type': 'object'}
TOOL_NOTES = "The `get_input` parameter (a Python callable) cannot be passed through MCP's JSON interface and is intentionally omitted from this schema. In a server/headless context the omitted default (`builtins.input`) will block waiting for stdin — this tool is only safe to call with `data` pre-populated for the full experiment (pure replay mode), or when the calling environment can service stdin. For LLM-driven simulation, pre-collect responses and pass them via `data` rather than attempting to wire a live LLM callable. The return value is a two-element tuple `(out_data, prompts)`; the handle registry stores the full tuple, so downstream tools should index into it to retrieve just the trial records or just the prompt log."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = sb.Experiment
    resolved = handles.resolve_in(kwargs)
    instance = resolved.pop('experiment', None)
    if instance is None:
        raise TypeError(
            f"{TOOL_NAME} requires kwarg 'experiment' "
            f"(handle returned by create_experiment)."
        )
    if not isinstance(instance, cls):
        raise TypeError(
            f"{TOOL_NAME} got 'experiment'={type(instance).__name__}, "
            f"expected Experiment."
        )
    result = instance.run_on_language(**resolved)
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
    def run_on_language(args: dict[str, Any] | None = None) -> Any:
        'Call this at step 4 of the SweetPea→SweetBean pipeline, after building an Experiment from SweetBean blocks wired to a SweetPea-sampled timeline, when you want to drive the experiment as a text-based conversation rather than compiling to HTML.'
        return _impl(args or {})
