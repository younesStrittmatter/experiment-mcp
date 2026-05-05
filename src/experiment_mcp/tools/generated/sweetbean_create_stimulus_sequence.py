"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '8f9eac38f4a17a9c9db1197defd992e032b2ab72f8dd695831ff09251fc9a6ac'
__exp_qualname__ = 'sweetbean.block.create_stimulus_sequence'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_stimulus_sequence'
TOOL_DESCRIPTION = 'Call this tool to produce a visual timeline diagram of a SweetBean stimulus sequence: it composites a list of PIL Image frames onto a shared canvas, arranged diagonally with configurable overlap, draws a connecting arrow, and annotates each frame with its duration in milliseconds (or "Until response" for null timings). Use it after you have a set of rendered stimulus images and a timing schedule — typically as a debugging or documentation step before wiring the frames into a SweetBean Block and compiling to HTML. The return value is a handle to a PIL Image (the composite canvas).\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "arrow_color": {\n      "default": [\n        0,\n        0,\n        0\n      ],\n      "description": "RGB color of the timeline arrow drawn below the frames, e.g. [0, 0, 0] for black.",\n      "items": {\n        "maximum": 255,\n        "minimum": 0,\n        "type": "integer"\n      },\n      "maxItems": 3,\n      "minItems": 3,\n      "type": "array"\n    },\n    "font_path": {\n      "description": "Absolute path to a TrueType (.ttf) font file for timing labels. If omitted, PIL\'s built-in default font is used.",\n      "type": "string"\n    },\n    "images": {\n      "description": "Ordered list of handle strings, each pointing to a PIL Image object produced by a prior tool call. All images must be the same pixel dimensions.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "overlap_x": {\n      "default": 0.05,\n      "description": "Horizontal overlap between successive frames as a fraction of image width (0\\u20131). Smaller values spread frames further apart horizontally.",\n      "type": "number"\n    },\n    "overlap_y": {\n      "default": 0.5,\n      "description": "Vertical overlap between successive frames as a fraction of image height (0\\u20131). Larger values stack frames more tightly.",\n      "type": "number"\n    },\n    "timings": {\n      "description": "Duration for each image in milliseconds. Use null for a frame that stays until the participant responds (rendered as \'Until response\'). Must be the same length as images.",\n      "items": {\n        "type": [\n          "number",\n          "null"\n        ]\n      },\n      "type": "array"\n    },\n    "zoom_factor": {\n      "default": 2.5,\n      "description": "Zoom (crop-in) factor applied to each image before pasting. A scalar applies the same zoom to all frames; pass an array of the same length as images for per-frame control. Higher values zoom in more.",\n      "oneOf": [\n        {\n          "type": "number"\n        },\n        {\n          "items": {\n            "type": "number"\n          },\n          "type": "array"\n        }\n      ]\n    }\n  },\n  "required": [\n    "images",\n    "timings"\n  ],\n  "type": "object"\n}\n\nNotes:\n• All images must be the same pixel size; canvas layout is computed from `images[0].size` — mismatched sizes produce misaligned output without an explicit error.\n• `images` and `timings` must have identical lengths; a mismatch raises `ValueError`.\n• The returned PIL Image canvas includes ~25 % padding on each side for the arrow and text, so the output is larger than the sum of the individual frames.\n• Requires Pillow; if PIL is not installed the function raises `ImportError` at call time (lazy import via `_lazy_pil()`).\n• `zoom_factor` as a scalar is broadcast to a list internally — pass a list only when you need per-frame zoom.\n• The arrow is drawn from the bottom-left corner of the first frame to the bottom-left corner of the last frame; for a single image (`len(images) == 1`) the arrow degenerates to a point and timing fraction is fixed at 0.'
TOOL_PARAMETERS = { 'properties': { 'arrow_color': { 'default': [0, 0, 0],
                                   'description': 'RGB color of the timeline arrow '
                                                  'drawn below the frames, e.g. [0, 0, '
                                                  '0] for black.',
                                   'items': { 'maximum': 255,
                                              'minimum': 0,
                                              'type': 'integer'},
                                   'maxItems': 3,
                                   'minItems': 3,
                                   'type': 'array'},
                  'font_path': { 'description': 'Absolute path to a TrueType (.ttf) '
                                                'font file for timing labels. If '
                                                "omitted, PIL's built-in default font "
                                                'is used.',
                                 'type': 'string'},
                  'images': { 'description': 'Ordered list of handle strings, each '
                                             'pointing to a PIL Image object produced '
                                             'by a prior tool call. All images must be '
                                             'the same pixel dimensions.',
                              'items': {'type': 'string'},
                              'type': 'array'},
                  'overlap_x': { 'default': 0.05,
                                 'description': 'Horizontal overlap between successive '
                                                'frames as a fraction of image width '
                                                '(0–1). Smaller values spread frames '
                                                'further apart horizontally.',
                                 'type': 'number'},
                  'overlap_y': { 'default': 0.5,
                                 'description': 'Vertical overlap between successive '
                                                'frames as a fraction of image height '
                                                '(0–1). Larger values stack frames '
                                                'more tightly.',
                                 'type': 'number'},
                  'timings': { 'description': 'Duration for each image in '
                                              'milliseconds. Use null for a frame that '
                                              'stays until the participant responds '
                                              "(rendered as 'Until response'). Must be "
                                              'the same length as images.',
                               'items': {'type': ['number', 'null']},
                               'type': 'array'},
                  'zoom_factor': { 'default': 2.5,
                                   'description': 'Zoom (crop-in) factor applied to '
                                                  'each image before pasting. A scalar '
                                                  'applies the same zoom to all '
                                                  'frames; pass an array of the same '
                                                  'length as images for per-frame '
                                                  'control. Higher values zoom in '
                                                  'more.',
                                   'oneOf': [ {'type': 'number'},
                                              { 'items': {'type': 'number'},
                                                'type': 'array'}]}},
  'required': ['images', 'timings'],
  'type': 'object'}
TOOL_NOTES = '• All images must be the same pixel size; canvas layout is computed from `images[0].size` — mismatched sizes produce misaligned output without an explicit error.\n• `images` and `timings` must have identical lengths; a mismatch raises `ValueError`.\n• The returned PIL Image canvas includes ~25 % padding on each side for the arrow and text, so the output is larger than the sum of the individual frames.\n• Requires Pillow; if PIL is not installed the function raises `ImportError` at call time (lazy import via `_lazy_pil()`).\n• `zoom_factor` as a scalar is broadcast to a list internally — pass a list only when you need per-frame zoom.\n• The arrow is drawn from the bottom-left corner of the first frame to the bottom-left corner of the last frame; for a single image (`len(images) == 1`) the arrow degenerates to a point and timing fraction is fixed at 0.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.create_stimulus_sequence
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
    def create_stimulus_sequence(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to produce a visual timeline diagram of a SweetBean stimulus sequence: it composites a list of PIL Image frames onto a shared canvas, arranged diagonally with configurable overlap, draws a connecting arrow, and annotates each frame with its duration in milliseconds (or "Until response" for null timings).'
        return _impl(args or {})
