"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '614c86d1810738ffc6256fe61b479455252335665c837c6d6b302400a061095b'
__exp_qualname__ = 'sweetbean.build_prompt_schema_markdown'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'build_prompt_schema_markdown'
TOOL_DESCRIPTION = 'Call this tool before constructing SweetBean trials or stimuli to get the authoritative schema for TrialSpec, StimulusSpecUnion, and ResponseSpecUnion. Returns a markdown reference document — including a placeholder guide explaining how {{column_name}} tokens from a SweetPea-sampled timeline are interpolated into stimulus fields. Use it at step 3 of the pipeline (wiring SweetPea sequences into SweetBean trials) whenever you are unsure which fields a stimulus or response spec accepts.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "verbosity": {\n      "default": 1,\n      "description": "Controls schema detail level. 1 (default) shows core fields; higher values (e.g. 2) expose optional fields gated by prompt_verbosity_min. Increase when you need less-common stimulus or response properties.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nWhen the `auto_prompt` package is absent, the function falls back to raw JSON Schema dumps wrapped in a code block — still parseable but without the timeline-placeholder guide or narrative descriptions. The returned string is purely informational and produces no SweetBean object or handle; it is a read-only reference call with no side effects.'
TOOL_PARAMETERS = { 'properties': { 'verbosity': { 'default': 1,
                                 'description': 'Controls schema detail level. 1 '
                                                '(default) shows core fields; higher '
                                                'values (e.g. 2) expose optional '
                                                'fields gated by prompt_verbosity_min. '
                                                'Increase when you need less-common '
                                                'stimulus or response properties.',
                                 'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'When the `auto_prompt` package is absent, the function falls back to raw JSON Schema dumps wrapped in a code block — still parseable but without the timeline-placeholder guide or narrative descriptions. The returned string is purely informational and produces no SweetBean object or handle; it is a read-only reference call with no side effects.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.build_prompt_schema_markdown
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
    def build_prompt_schema_markdown(args: dict[str, Any] | None = None) -> Any:
        'Call this tool before constructing SweetBean trials or stimuli to get the authoritative schema for TrialSpec, StimulusSpecUnion, and ResponseSpecUnion.'
        return _impl(args or {})
