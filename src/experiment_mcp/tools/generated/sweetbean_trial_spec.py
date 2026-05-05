"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'faca46d7b4b53a1cb7e7cd1725eaad8ab77e184b9a3032f3b866533e8445361a'
__exp_qualname__ = 'sweetbean.TrialSpec'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_trial_spec'
TOOL_DESCRIPTION = 'Call this tool after creating one or more stimulus specs (e.g. sweetbean_text_stimulus_spec, sweetbean_symbol_stimulus_spec) and optional response specs to assemble them into a single rendered trial frame. Use it when building a SweetBean Block — each element in a Block\'s trial list should be a TrialSpec handle. The result is a handle string pointing to a TrialSpec object ready to be passed to sweetbean_block.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "background_color": {\n      "default": "black",\n      "description": "CSS background color for the trial frame (e.g. \'black\', \'#ffffff\', \'rgb(200,200,200)\'). Defaults to black.",\n      "type": "string"\n    },\n    "responses": {\n      "default": [],\n      "description": "Optional list of response handler handle strings (from sweetbean_keyboard_press_response_spec, sweetbean_mouse_click_response_spec, etc.) active during this trial frame. Pass an empty array or omit for stimulus-only (no-response) trials.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "stimuli": {\n      "description": "Ordered list of stimulus handle strings (from sweetbean_text_stimulus_spec, sweetbean_symbol_stimulus_spec, sweetbean_asset_stimulus_spec, etc.). Rendered as overlapping layers; z-index is assigned by list position if not set on each stimulus.",\n      "items": {\n        "type": "string"\n      },\n      "minItems": 1,\n      "type": "array"\n    },\n    "trial_duration_ms": {\n      "description": "Hard cap on total trial duration in milliseconds. If omitted the trial waits for a response (or runs indefinitely if no response handlers are attached).",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "stimuli"\n  ],\n  "type": "object"\n}\n\nNotes:\nstimuli is required and must contain at least one handle. The model validator auto-fills missing per-stimulus defaults (z_index from list order, rect=RectangleSpec(), opacity=1.0, and type-specific defaults like font_size_px=32 for text), so you rarely need to set those on the stimuli themselves. All stimulus ids within a trial must be unique if provided — the validator raises if duplicates are detected. trial_duration_ms and background_color carry _PROMPT_SILENT in their schema_extra, meaning they are intentionally de-emphasized in the prompt surface; only pass them when the experiment design explicitly requires them.'
TOOL_PARAMETERS = { 'properties': { 'background_color': { 'default': 'black',
                                        'description': 'CSS background color for the '
                                                       "trial frame (e.g. 'black', "
                                                       "'#ffffff', "
                                                       "'rgb(200,200,200)'). Defaults "
                                                       'to black.',
                                        'type': 'string'},
                  'responses': { 'default': [],
                                 'description': 'Optional list of response handler '
                                                'handle strings (from '
                                                'sweetbean_keyboard_press_response_spec, '
                                                'sweetbean_mouse_click_response_spec, '
                                                'etc.) active during this trial frame. '
                                                'Pass an empty array or omit for '
                                                'stimulus-only (no-response) trials.',
                                 'items': {'type': 'string'},
                                 'type': 'array'},
                  'stimuli': { 'description': 'Ordered list of stimulus handle strings '
                                              '(from sweetbean_text_stimulus_spec, '
                                              'sweetbean_symbol_stimulus_spec, '
                                              'sweetbean_asset_stimulus_spec, etc.). '
                                              'Rendered as overlapping layers; z-index '
                                              'is assigned by list position if not set '
                                              'on each stimulus.',
                               'items': {'type': 'string'},
                               'minItems': 1,
                               'type': 'array'},
                  'trial_duration_ms': { 'description': 'Hard cap on total trial '
                                                        'duration in milliseconds. If '
                                                        'omitted the trial waits for a '
                                                        'response (or runs '
                                                        'indefinitely if no response '
                                                        'handlers are attached).',
                                         'minimum': 1,
                                         'type': 'integer'}},
  'required': ['stimuli'],
  'type': 'object'}
TOOL_NOTES = 'stimuli is required and must contain at least one handle. The model validator auto-fills missing per-stimulus defaults (z_index from list order, rect=RectangleSpec(), opacity=1.0, and type-specific defaults like font_size_px=32 for text), so you rarely need to set those on the stimuli themselves. All stimulus ids within a trial must be unique if provided — the validator raises if duplicates are detected. trial_duration_ms and background_color carry _PROMPT_SILENT in their schema_extra, meaning they are intentionally de-emphasized in the prompt surface; only pass them when the experiment design explicitly requires them.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.TrialSpec
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
    def create_trial_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after creating one or more stimulus specs (e.g.'
        return _impl(args or {})
