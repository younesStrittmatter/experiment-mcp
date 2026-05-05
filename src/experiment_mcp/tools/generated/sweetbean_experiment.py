"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '027fe8cae60463061dd3695e44466db746a7e0d2e143512b2a7f0b299ac55d2b'
__exp_qualname__ = 'sweetbean.Experiment'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_experiment'
TOOL_DESCRIPTION = 'Call this tool after all SweetBean `Block` handles have been created — it is the final assembly step that bundles an ordered list of blocks into a single `Experiment` handle ready for compilation or export. Pass the returned handle to `sweetbean_experiment_to_html`, `sweetbean_experiment_to_js_string`, `sweetbean_experiment_compile`, or `sweetbean_experiment_run_on_language`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "blocks": {\n      "description": "Ordered list of Block handle strings (each returned by the sweetbean_block tool). Blocks run in the order given; timeline and stimuli are drawn from each block in sequence.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "protections": {\n      "description": "Optional list of Protection handle strings (e.g. BotDetection). Each protection embeds JS into the compiled experiment at well-defined hook points (head assets, runtime init, per-trial on_load/on_finish, summary). Omit if no protections are needed.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "blocks"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe constructor does not compile or export anything — it only assembles the block list. The returned handle must be passed to a downstream tool (`to_html`, `to_js_string`, `compile`, or `run_on_language`) to produce output. Block order is significant: blocks execute left-to-right and shared variables are resolved across blocks in that order. `protections` defaults to an empty list if omitted.'
TOOL_PARAMETERS = { 'properties': { 'blocks': { 'description': 'Ordered list of Block handle strings '
                                             '(each returned by the sweetbean_block '
                                             'tool). Blocks run in the order given; '
                                             'timeline and stimuli are drawn from each '
                                             'block in sequence.',
                              'items': {'type': 'string'},
                              'type': 'array'},
                  'protections': { 'description': 'Optional list of Protection handle '
                                                  'strings (e.g. BotDetection). Each '
                                                  'protection embeds JS into the '
                                                  'compiled experiment at well-defined '
                                                  'hook points (head assets, runtime '
                                                  'init, per-trial on_load/on_finish, '
                                                  'summary). Omit if no protections '
                                                  'are needed.',
                                   'items': {'type': 'string'},
                                   'type': 'array'}},
  'required': ['blocks'],
  'type': 'object'}
TOOL_NOTES = 'The constructor does not compile or export anything — it only assembles the block list. The returned handle must be passed to a downstream tool (`to_html`, `to_js_string`, `compile`, or `run_on_language`) to produce output. Block order is significant: blocks execute left-to-right and shared variables are resolved across blocks in that order. `protections` defaults to an empty list if omitted.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Experiment
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
    def create_experiment(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after all SweetBean `Block` handles have been created — it is the final assembly step that bundles an ordered list of blocks into a single `Experiment` handle ready for compilation or export.'
        return _impl(args or {})
