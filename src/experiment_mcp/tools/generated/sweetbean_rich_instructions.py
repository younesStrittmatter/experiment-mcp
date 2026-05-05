"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'fb842dd71a97c4b6e77e116de269efa130ff8069d63f832f637fceaebed4a4d7'
__exp_qualname__ = 'sweetbean.stimulus.RichInstructions'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_rich_instructions'
TOOL_DESCRIPTION = 'Call this tool to create a formatted instruction screen that participants read before the main experiment begins. Place it as the first stimulus in a SweetBean Block (step 3 of the pipeline, before or alongside trial stimuli). Returns a RichInstructions stimulus object whose handle can be passed into a Block.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "body_font_px": {\n      "default": 13,\n      "description": "Font size in pixels for body text.",\n      "type": "integer"\n    },\n    "choices": {\n      "description": "Keys that advance the page. Defaults to [\\" \\"] (spacebar) when omitted.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "Key considered correct for scoring purposes. Empty string means no key is marked correct.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Maximum display time in milliseconds before auto-advancing. Omit (null) to require a keypress.",\n      "type": "integer"\n    },\n    "fit_to_viewport": {\n      "description": "If true, shrinks content to fit the screen height. Defaults to false so long pages scroll naturally.",\n      "type": "boolean"\n    },\n    "footer_html": {\n      "description": "Optional raw HTML rendered below inner_html, e.g. a \'Press SPACE to continue\' reminder.",\n      "type": "string"\n    },\n    "inner_html": {\n      "description": "Raw HTML content for the body of the instruction page. Use <p>, <ul>, <b>, etc. for structure. This is the main instruction text shown to participants.",\n      "type": "string"\n    },\n    "max_width_px": {\n      "default": 780,\n      "description": "Maximum content column width in pixels.",\n      "type": "integer"\n    },\n    "section_font_px": {\n      "default": 20,\n      "description": "Font size in pixels for section subheadings.",\n      "type": "integer"\n    },\n    "side_effects": {\n      "description": "Handle string for a SweetBean side-effect object produced by another tool, or omit if none.",\n      "type": "string"\n    },\n    "title": {\n      "default": "Instructions",\n      "description": "Heading displayed at the top of the page.",\n      "type": "string"\n    },\n    "title_font_px": {\n      "default": 32,\n      "description": "Font size in pixels for the title heading.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "inner_html"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `inner_html` is raw HTML, not plain text — use markup tags for formatting.\n- When `choices` is omitted or null the class internally substitutes `[" "]` (spacebar); pass an explicit list only if a different key is needed.\n- `fit_to_viewport` is `False` at the class level, so the page scrolls by default — set to `true` only for short content that must not scroll.\n- `duration` and `side_effects` are independent; both can be omitted for a simple key-gated instruction screen.\n- `side_effects` must be a handle string returned by a prior tool call, not a raw Python object.'
TOOL_PARAMETERS = { 'properties': { 'body_font_px': { 'default': 13,
                                    'description': 'Font size in pixels for body text.',
                                    'type': 'integer'},
                  'choices': { 'description': 'Keys that advance the page. Defaults to '
                                              '[" "] (spacebar) when omitted.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'correct_key': { 'default': '',
                                   'description': 'Key considered correct for scoring '
                                                  'purposes. Empty string means no key '
                                                  'is marked correct.',
                                   'type': 'string'},
                  'duration': { 'description': 'Maximum display time in milliseconds '
                                               'before auto-advancing. Omit (null) to '
                                               'require a keypress.',
                                'type': 'integer'},
                  'fit_to_viewport': { 'description': 'If true, shrinks content to fit '
                                                      'the screen height. Defaults to '
                                                      'false so long pages scroll '
                                                      'naturally.',
                                       'type': 'boolean'},
                  'footer_html': { 'description': 'Optional raw HTML rendered below '
                                                  "inner_html, e.g. a 'Press SPACE to "
                                                  "continue' reminder.",
                                   'type': 'string'},
                  'inner_html': { 'description': 'Raw HTML content for the body of the '
                                                 'instruction page. Use <p>, <ul>, '
                                                 '<b>, etc. for structure. This is the '
                                                 'main instruction text shown to '
                                                 'participants.',
                                  'type': 'string'},
                  'max_width_px': { 'default': 780,
                                    'description': 'Maximum content column width in '
                                                   'pixels.',
                                    'type': 'integer'},
                  'section_font_px': { 'default': 20,
                                       'description': 'Font size in pixels for section '
                                                      'subheadings.',
                                       'type': 'integer'},
                  'side_effects': { 'description': 'Handle string for a SweetBean '
                                                   'side-effect object produced by '
                                                   'another tool, or omit if none.',
                                    'type': 'string'},
                  'title': { 'default': 'Instructions',
                             'description': 'Heading displayed at the top of the page.',
                             'type': 'string'},
                  'title_font_px': { 'default': 32,
                                     'description': 'Font size in pixels for the title '
                                                    'heading.',
                                     'type': 'integer'}},
  'required': ['inner_html'],
  'type': 'object'}
TOOL_NOTES = '- `inner_html` is raw HTML, not plain text — use markup tags for formatting.\n- When `choices` is omitted or null the class internally substitutes `[" "]` (spacebar); pass an explicit list only if a different key is needed.\n- `fit_to_viewport` is `False` at the class level, so the page scrolls by default — set to `true` only for short content that must not scroll.\n- `duration` and `side_effects` are independent; both can be omitted for a simple key-gated instruction screen.\n- `side_effects` must be a handle string returned by a prior tool call, not a raw Python object.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.RichInstructions
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
    def create_rich_instructions(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a formatted instruction screen that participants read before the main experiment begins.'
        return _impl(args or {})
