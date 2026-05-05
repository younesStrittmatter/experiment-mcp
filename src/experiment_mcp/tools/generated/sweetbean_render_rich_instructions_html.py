"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'd824109630b9728a7abf16f67f2bc27478a982a0aa9fee7dd4e90003a07696f1'
__exp_qualname__ = 'sweetbean.stimulus.render_rich_instructions_html'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'render_rich_instructions_html'
TOOL_DESCRIPTION = 'Call this tool when you need to generate a styled instructions HTML string outside the SweetBean stimulus pipeline — for example, to embed instructions in a custom HTML template, preview panel, or any non-stimulus context. It returns a self-contained `<style>` block plus a styled wrapper div as a plain string; pass that string wherever raw HTML is accepted. Use `RichInstructions` stimulus instead if you want the instructions rendered as a jsPsych trial inside a SweetBean experiment.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "body_font_px": {\n      "default": 13,\n      "description": "Font size in pixels for body text. Default 13.",\n      "type": "integer"\n    },\n    "footer_html": {\n      "description": "HTML appended after inner_html. Omit or pass null to use the default \'Press SPACE to continue\' footer paragraph.",\n      "type": "string"\n    },\n    "inner_html": {\n      "description": "The main body HTML to render inside the instructions wrapper. May contain `<p>`, `<ul>`, `<section>`, etc. Not escaped \\u2014 pass safe HTML.",\n      "type": "string"\n    },\n    "max_width_px": {\n      "default": 780,\n      "description": "Maximum width of the instructions panel in pixels. Default 780.",\n      "type": "integer"\n    },\n    "section_font_px": {\n      "default": 20,\n      "description": "Font size in pixels for section subheadings. Default 20.",\n      "type": "integer"\n    },\n    "title": {\n      "default": "Instructions",\n      "description": "Heading text displayed at the top of the instructions panel. Plain text only; automatically HTML-escaped. Defaults to \'Instructions\'.",\n      "type": "string"\n    },\n    "title_font_px": {\n      "default": 32,\n      "description": "Font size in pixels for the title heading. Default 32.",\n      "type": "integer"\n    }\n  },\n  "required": [\n    "inner_html"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `inner_html` is the only required parameter; all others have defaults.\n- `footer_html` being absent (not passed) and being `null` both trigger the default "Press SPACE to continue" footer — to suppress the footer entirely, pass an empty string `""`.\n- `title` is HTML-escaped before rendering, so plain text is always safe; do NOT pre-escape it or you will see double-escaping.\n- All `*_px` parameters are cast to `int` internally; pass integers, not floats.\n- This function returns a raw HTML string, not a handle — it cannot be passed as a SweetBean object to other tools.'
TOOL_PARAMETERS = { 'properties': { 'body_font_px': { 'default': 13,
                                    'description': 'Font size in pixels for body text. '
                                                   'Default 13.',
                                    'type': 'integer'},
                  'footer_html': { 'description': 'HTML appended after inner_html. '
                                                  'Omit or pass null to use the '
                                                  "default 'Press SPACE to continue' "
                                                  'footer paragraph.',
                                   'type': 'string'},
                  'inner_html': { 'description': 'The main body HTML to render inside '
                                                 'the instructions wrapper. May '
                                                 'contain `<p>`, `<ul>`, `<section>`, '
                                                 'etc. Not escaped — pass safe HTML.',
                                  'type': 'string'},
                  'max_width_px': { 'default': 780,
                                    'description': 'Maximum width of the instructions '
                                                   'panel in pixels. Default 780.',
                                    'type': 'integer'},
                  'section_font_px': { 'default': 20,
                                       'description': 'Font size in pixels for section '
                                                      'subheadings. Default 20.',
                                       'type': 'integer'},
                  'title': { 'default': 'Instructions',
                             'description': 'Heading text displayed at the top of the '
                                            'instructions panel. Plain text only; '
                                            'automatically HTML-escaped. Defaults to '
                                            "'Instructions'.",
                             'type': 'string'},
                  'title_font_px': { 'default': 32,
                                     'description': 'Font size in pixels for the title '
                                                    'heading. Default 32.',
                                     'type': 'integer'}},
  'required': ['inner_html'],
  'type': 'object'}
TOOL_NOTES = '- `inner_html` is the only required parameter; all others have defaults.\n- `footer_html` being absent (not passed) and being `null` both trigger the default "Press SPACE to continue" footer — to suppress the footer entirely, pass an empty string `""`.\n- `title` is HTML-escaped before rendering, so plain text is always safe; do NOT pre-escape it or you will see double-escaping.\n- All `*_px` parameters are cast to `int` internally; pass integers, not floats.\n- This function returns a raw HTML string, not a handle — it cannot be passed as a SweetBean object to other tools.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.render_rich_instructions_html
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
    def render_rich_instructions_html(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when you need to generate a styled instructions HTML string outside the SweetBean stimulus pipeline — for example, to embed instructions in a custom HTML template, preview panel, or any non-stimulus context.'
        return _impl(args or {})
