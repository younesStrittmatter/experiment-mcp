"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'b237d0d404a575eed6b7fb78c45047fc27ddb06a3557a38ace24a8abfe790f49'
__exp_qualname__ = 'sweetbean.Block'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_block'
TOOL_DESCRIPTION = 'Call this tool at step 3 of the pipeline, after creating SweetBean stimulus objects and (optionally) sampling a SweetPea trial sequence. It groups one or more stimuli into an ordered block (e.g. instructions, training, or test phase) and returns a handle that must be passed to the Experiment tool to compile or run the full experiment. The result is an opaque handle string referencing a live Block object.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "stimuli": {\n      "description": "Ordered list of handle strings for SweetBean stimulus objects (e.g. returned by TextStimulus, ImageStimulus, or similar tools). Each handle is resolved to a live stimulus before dispatch.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "timeline": {\n      "default": [],\n      "description": "List of trial-row dicts mapping timeline variable names to their values for this block. Pass the trial sequence sampled from SweetPea here (one dict per trial). Omit or pass [] for blocks with no timeline variables (e.g. static instruction screens).",\n      "items": {\n        "additionalProperties": true,\n        "type": "object"\n      },\n      "type": "array"\n    }\n  },\n  "required": [\n    "stimuli"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `stimuli` must be non-empty; passing an empty list will produce a Block with no trials.\n- `timeline` dicts must use the exact variable names declared in your SweetBean stimulus arguments — mismatched keys are silently ignored at render time, which causes blank or broken trials.\n- The Block does not validate that every stimulus\'s timeline-variable references are satisfied by `timeline`; mismatches surface only when `to_js` or `to_image` is called on the parent Experiment.\n- If `timeline` contains a `CodeVariable` handle rather than a plain list, use that handle as the sole element; mixing `CodeVariable` handles with `template_timeline_token` (set by `Experiment.compile`) raises a `ValueError`.\n- Block objects are stateful: calling `to_js` mutates internal JS state. Let the Experiment tool drive compilation rather than calling JS-render methods directly.'
TOOL_PARAMETERS = { 'properties': { 'stimuli': { 'description': 'Ordered list of handle strings for '
                                              'SweetBean stimulus objects (e.g. '
                                              'returned by TextStimulus, '
                                              'ImageStimulus, or similar tools). Each '
                                              'handle is resolved to a live stimulus '
                                              'before dispatch.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'timeline': { 'default': [],
                                'description': 'List of trial-row dicts mapping '
                                               'timeline variable names to their '
                                               'values for this block. Pass the trial '
                                               'sequence sampled from SweetPea here '
                                               '(one dict per trial). Omit or pass [] '
                                               'for blocks with no timeline variables '
                                               '(e.g. static instruction screens).',
                                'items': { 'additionalProperties': True,
                                           'type': 'object'},
                                'type': 'array'}},
  'required': ['stimuli'],
  'type': 'object'}
TOOL_NOTES = "- `stimuli` must be non-empty; passing an empty list will produce a Block with no trials.\n- `timeline` dicts must use the exact variable names declared in your SweetBean stimulus arguments — mismatched keys are silently ignored at render time, which causes blank or broken trials.\n- The Block does not validate that every stimulus's timeline-variable references are satisfied by `timeline`; mismatches surface only when `to_js` or `to_image` is called on the parent Experiment.\n- If `timeline` contains a `CodeVariable` handle rather than a plain list, use that handle as the sole element; mixing `CodeVariable` handles with `template_timeline_token` (set by `Experiment.compile`) raises a `ValueError`.\n- Block objects are stateful: calling `to_js` mutates internal JS state. Let the Experiment tool drive compilation rather than calling JS-render methods directly."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Block
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
    def create_block(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at step 3 of the pipeline, after creating SweetBean stimulus objects and (optionally) sampling a SweetPea trial sequence.'
        return _impl(args or {})
