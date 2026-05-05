"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'd3b67eaa38964658c26b43485dc031942a365b35e552714f681f240959d37821'
__exp_qualname__ = 'sweetbean.AssetStimulusSpec'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_asset_stimulus_spec'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the pipeline to define an image or animated-GIF stimulus for a jsPsych trial. Use it when a SweetPea trial sequence includes a factor whose levels correspond to visual assets (images, GIFs); the resulting AssetStimulusSpec is then passed into a SweetBean Trial or Block to render the asset on screen. Returns an AssetStimulusSpec object (handle string) ready for composition into a SweetBean experiment.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "asset_ref": {\n      "description": "URL or file path of the image/GIF to display, or a jsPsych timeline variable placeholder such as `{{column_name}}` that will be resolved from the current CSV/trial-sequence row at runtime. Use the placeholder form when different trials should show different images drawn from a SweetPea factor.",\n      "type": "string"\n    },\n    "object_fit": {\n      "description": "Optional CSS object-fit value controlling how the asset is scaled inside its container. Omit to accept the default (contain).",\n      "enum": [\n        "contain",\n        "cover",\n        "fill",\n        "none",\n        "scale-down"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "asset_ref"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `object_fit` field is tagged `_PROMPT_SILENT` in the source, meaning jsPsych\'s own UI will not surface it; it is still respected at render time. When omitted it behaves as CSS `contain`. The `kind` field is always `"asset"` and must not be passed — it is set automatically by the class.'
TOOL_PARAMETERS = { 'properties': { 'asset_ref': { 'description': 'URL or file path of the image/GIF to '
                                                'display, or a jsPsych timeline '
                                                'variable placeholder such as '
                                                '`{{column_name}}` that will be '
                                                'resolved from the current '
                                                'CSV/trial-sequence row at runtime. '
                                                'Use the placeholder form when '
                                                'different trials should show '
                                                'different images drawn from a '
                                                'SweetPea factor.',
                                 'type': 'string'},
                  'object_fit': { 'description': 'Optional CSS object-fit value '
                                                 'controlling how the asset is scaled '
                                                 'inside its container. Omit to accept '
                                                 'the default (contain).',
                                  'enum': [ 'contain',
                                            'cover',
                                            'fill',
                                            'none',
                                            'scale-down'],
                                  'type': 'string'}},
  'required': ['asset_ref'],
  'type': 'object'}
TOOL_NOTES = 'The `object_fit` field is tagged `_PROMPT_SILENT` in the source, meaning jsPsych\'s own UI will not surface it; it is still respected at render time. When omitted it behaves as CSS `contain`. The `kind` field is always `"asset"` and must not be passed — it is set automatically by the class.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.AssetStimulusSpec
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
    def create_asset_stimulus_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the pipeline to define an image or animated-GIF stimulus for a jsPsych trial.'
        return _impl(args or {})
