"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '1cf48dcf0d276984fbbfe7c491b1e696c63de6719b44795f47a0c08c80266ad0'
__exp_qualname__ = 'sweetbean.stimulus.Image'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_image'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the pipeline — after SweetPea has generated a trial sequence — to define a stimulus trial that displays an image and waits for a keyboard response. Returns a handle string to a SweetBean `Image` stimulus object that can be passed to `sweetbean_block` to assemble a trial block.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "choices": {\n      "description": "List of keyboard keys that will be recorded if pressed during the trial (e.g. [\'f\', \'j\']). If omitted, any key is accepted.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "correct_key": {\n      "description": "The key that constitutes a correct response. Used for accuracy scoring. Defaults to empty string (no correct key defined).",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Time in milliseconds the stimulus is presented. If omitted, the trial waits indefinitely for a key press.",\n      "type": "integer"\n    },\n    "side_effects": {\n      "description": "Optional list of SideEffect definition objects to update global data (e.g. score counter) on each trial response.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "stimulus": {\n      "description": "File path to the image to display (e.g. \'images/cat.png\'). Must be a key in \'image_prompts.json\' if the experiment will be run on a language model.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "stimulus"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `stimulus` path is relative to the experiment\'s working directory, not the Python script. When running the experiment on a language model via `experiment_run_on_language`, a file named `image_prompts.json` must exist in the same directory as the experiment script; it maps each image path to a text prompt describing the image — missing or invalid JSON in that file raises at runtime. `duration=None` means the trial is response-terminated (no timeout). `choices=None` means any key is accepted.'
TOOL_PARAMETERS = { 'properties': { 'choices': { 'description': 'List of keyboard keys that will be '
                                              'recorded if pressed during the trial '
                                              "(e.g. ['f', 'j']). If omitted, any key "
                                              'is accepted.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'correct_key': { 'description': 'The key that constitutes a correct '
                                                  'response. Used for accuracy '
                                                  'scoring. Defaults to empty string '
                                                  '(no correct key defined).',
                                   'type': 'string'},
                  'duration': { 'description': 'Time in milliseconds the stimulus is '
                                               'presented. If omitted, the trial waits '
                                               'indefinitely for a key press.',
                                'type': 'integer'},
                  'side_effects': { 'description': 'Optional list of SideEffect '
                                                   'definition objects to update '
                                                   'global data (e.g. score counter) '
                                                   'on each trial response.',
                                    'items': {'type': 'object'},
                                    'type': 'array'},
                  'stimulus': { 'description': 'File path to the image to display '
                                               "(e.g. 'images/cat.png'). Must be a key "
                                               "in 'image_prompts.json' if the "
                                               'experiment will be run on a language '
                                               'model.',
                                'type': 'string'}},
  'required': ['stimulus'],
  'type': 'object'}
TOOL_NOTES = "The `stimulus` path is relative to the experiment's working directory, not the Python script. When running the experiment on a language model via `experiment_run_on_language`, a file named `image_prompts.json` must exist in the same directory as the experiment script; it maps each image path to a text prompt describing the image — missing or invalid JSON in that file raises at runtime. `duration=None` means the trial is response-terminated (no timeout). `choices=None` means any key is accepted."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Image
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
    def create_image(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the pipeline — after SweetPea has generated a trial sequence — to define a stimulus trial that displays an image and waits for a keyboard response.'
        return _impl(args or {})
