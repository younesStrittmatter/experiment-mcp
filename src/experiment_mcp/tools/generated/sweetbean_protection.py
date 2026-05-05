"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'd46c70dee031bf5a19f0bbd66ce08922710ce50f81de3287935e5298e52cdb30'
__exp_qualname__ = 'sweetbean.Protection'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_protection'
TOOL_DESCRIPTION = 'Call this tool to instantiate a no-op `sweetbean.Protection` placeholder — useful as a structural slot in a SweetBean Experiment when you need a protection object but don\'t yet have a concrete subclass (e.g. BotDetection). In the pipeline this sits just before `Experiment.to_html` or `Experiment.compile`: pass the returned handle as the `protection` argument to those tools. The result is a handle string referencing the live Protection instance.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "name": {\n      "default": "protection",\n      "description": "Identifier for this protection instance, embedded in generated JS. Defaults to \'protection\'. Override when multiple protection layers coexist in one experiment.",\n      "type": "string"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThis is the abstract base class — all hook methods (head_assets, runtime_js, init_js, summary_js, on_load_for_stimulus, on_finish_for_stimulus) return empty strings, so instantiating it directly adds no actual protection behavior. If you want real bot-detection or attention-check logic, use a concrete subclass (e.g. sweetbean.BotDetection) instead. Only instantiate this base class when you explicitly need a structural no-op placeholder.'
TOOL_PARAMETERS = { 'properties': { 'name': { 'default': 'protection',
                            'description': 'Identifier for this protection instance, '
                                           'embedded in generated JS. Defaults to '
                                           "'protection'. Override when multiple "
                                           'protection layers coexist in one '
                                           'experiment.',
                            'type': 'string'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'This is the abstract base class — all hook methods (head_assets, runtime_js, init_js, summary_js, on_load_for_stimulus, on_finish_for_stimulus) return empty strings, so instantiating it directly adds no actual protection behavior. If you want real bot-detection or attention-check logic, use a concrete subclass (e.g. sweetbean.BotDetection) instead. Only instantiate this base class when you explicitly need a structural no-op placeholder.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Protection
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
    def create_protection(args: dict[str, Any] | None = None) -> Any:
        "Call this tool to instantiate a no-op `sweetbean.Protection` placeholder — useful as a structural slot in a SweetBean Experiment when you need a protection object but don't yet have a concrete subclass (e.g."
        return _impl(args or {})
