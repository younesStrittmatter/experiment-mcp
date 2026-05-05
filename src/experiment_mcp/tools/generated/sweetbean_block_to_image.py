"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'ac22cc4a2b01cfdc301418dea62d1a0cbe141a39a3a0d1c9a3937ab0f0142e30'
__exp_qualname__ = 'sweetbean.Block.to_image'
__exp_kind__ = 'method'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'to_image'
TOOL_DESCRIPTION = 'Call this tool after building a SweetBean Block (step 3–4 of the pipeline) to render a visual snapshot of the stimulus sequence as a PNG image. Use it to inspect or document an experimental design before compiling to HTML or running headless — the image shows the exact stimuli the block would display, sampled from the trial timeline. Returns a saved file when a path is provided, or raw PIL image data when called without a path.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string returned by the Block constructor tool identifying the SweetBean Block whose stimuli should be rendered.",\n      "type": "string"\n    },\n    "data": {\n      "description": "Trial-level data required by stimuli that depend on previous responses, such as feedback stimuli that need a \'correct\' key. Pass an empty array or omit if the block contains no response-conditional stimuli.",\n      "items": {\n        "additionalProperties": true,\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "path": {\n      "description": "Filesystem path at which to save the output. In sequence mode (sequence=true) this is a single PNG file path; in non-sequence mode it is a directory and files are written as stimulus_0.png, stimulus_1.png, \\u2026 Pass an empty string to skip saving and receive the PIL image object as a handle instead.",\n      "type": "string"\n    },\n    "sequence": {\n      "default": true,\n      "description": "If true (default), all stimulus frames are composited into a single side-by-side sequence image. If false, each stimulus is saved as a separate file and path must be a directory.",\n      "type": "boolean"\n    },\n    "timeline_idx": {\n      "default": "random",\n      "description": "Controls which trial from the block\'s timeline is rendered. \'random\' (default) picks one trial at random; an integer picks by zero-based index; null renders the full timeline (one image strip per trial).",\n      "oneOf": [\n        {\n          "enum": [\n            "random"\n          ],\n          "type": "string"\n        },\n        {\n          "minimum": 0,\n          "type": "integer"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "zoom_factor": {\n      "default": 3,\n      "description": "Pixel zoom multiplier applied to rendered stimuli. Pass a single number to apply uniformly, or a list with one entry per stimulus to zoom each frame independently.",\n      "oneOf": [\n        {\n          "minimum": 0,\n          "type": "number"\n        },\n        {\n          "items": {\n            "minimum": 0,\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "block",\n    "path",\n    "data"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `data` has no Python default; pass `[]` when the block has no feedback stimuli — do not omit it entirely or the call will fail.\n- Stimuli with `duration=0` are skipped during rendering; the image may show fewer frames than the block\'s stimulus list if any have zero duration.\n- When `sequence=false` and `path` is set, the return value is None (files written to directory); when `path` is empty and `sequence=false`, returns a tuple `(images, durations)` not a single image — handle accordingly.\n- `timeline_idx=null` renders every timeline entry, which can produce a very wide composite image for long trial lists.\n- The method calls `asyncio.run(render_html_to_image(...))` internally via Playwright/Chromium; ensure a display or virtual framebuffer is available in headless server environments.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string returned by the Block '
                                            'constructor tool identifying the '
                                            'SweetBean Block whose stimuli should be '
                                            'rendered.',
                             'type': 'string'},
                  'data': { 'description': 'Trial-level data required by stimuli that '
                                           'depend on previous responses, such as '
                                           "feedback stimuli that need a 'correct' "
                                           'key. Pass an empty array or omit if the '
                                           'block contains no response-conditional '
                                           'stimuli.',
                            'items': {'additionalProperties': True, 'type': 'object'},
                            'type': 'array'},
                  'path': { 'description': 'Filesystem path at which to save the '
                                           'output. In sequence mode (sequence=true) '
                                           'this is a single PNG file path; in '
                                           'non-sequence mode it is a directory and '
                                           'files are written as stimulus_0.png, '
                                           'stimulus_1.png, … Pass an empty string to '
                                           'skip saving and receive the PIL image '
                                           'object as a handle instead.',
                            'type': 'string'},
                  'sequence': { 'default': True,
                                'description': 'If true (default), all stimulus frames '
                                               'are composited into a single '
                                               'side-by-side sequence image. If false, '
                                               'each stimulus is saved as a separate '
                                               'file and path must be a directory.',
                                'type': 'boolean'},
                  'timeline_idx': { 'default': 'random',
                                    'description': 'Controls which trial from the '
                                                   "block's timeline is rendered. "
                                                   "'random' (default) picks one trial "
                                                   'at random; an integer picks by '
                                                   'zero-based index; null renders the '
                                                   'full timeline (one image strip per '
                                                   'trial).',
                                    'oneOf': [ {'enum': ['random'], 'type': 'string'},
                                               {'minimum': 0, 'type': 'integer'},
                                               {'type': 'null'}]},
                  'zoom_factor': { 'default': 3,
                                   'description': 'Pixel zoom multiplier applied to '
                                                  'rendered stimuli. Pass a single '
                                                  'number to apply uniformly, or a '
                                                  'list with one entry per stimulus to '
                                                  'zoom each frame independently.',
                                   'oneOf': [ {'minimum': 0, 'type': 'number'},
                                              { 'items': { 'minimum': 0,
                                                           'type': 'number'},
                                                'type': 'array'}]}},
  'required': ['block', 'path', 'data'],
  'type': 'object'}
TOOL_NOTES = "- `data` has no Python default; pass `[]` when the block has no feedback stimuli — do not omit it entirely or the call will fail.\n- Stimuli with `duration=0` are skipped during rendering; the image may show fewer frames than the block's stimulus list if any have zero duration.\n- When `sequence=false` and `path` is set, the return value is None (files written to directory); when `path` is empty and `sequence=false`, returns a tuple `(images, durations)` not a single image — handle accordingly.\n- `timeline_idx=null` renders every timeline entry, which can produce a very wide composite image for long trial lists.\n- The method calls `asyncio.run(render_html_to_image(...))` internally via Playwright/Chromium; ensure a display or virtual framebuffer is available in headless server environments."


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = sb.Block
    resolved = handles.resolve_in(kwargs)
    instance = resolved.pop('block', None)
    if instance is None:
        raise TypeError(
            f"{TOOL_NAME} requires kwarg 'block' "
            f"(handle returned by create_block)."
        )
    if not isinstance(instance, cls):
        raise TypeError(
            f"{TOOL_NAME} got 'block'={type(instance).__name__}, "
            f"expected Block."
        )
    result = instance.to_image(**resolved)
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
    def to_image(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after building a SweetBean Block (step 3–4 of the pipeline) to render a visual snapshot of the stimulus sequence as a PNG image.'
        return _impl(args or {})
