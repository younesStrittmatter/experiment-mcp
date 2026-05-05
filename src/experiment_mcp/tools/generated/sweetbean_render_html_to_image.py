"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '726729d272c482d0c3443d6a3a1449795202cbfdbfa326438e1d629d8d4b6393'
__exp_qualname__ = 'sweetbean.block.render_html_to_image'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'render_html_to_image'
TOOL_DESCRIPTION = 'Call this tool after producing jsPsych HTML (via sweetbean_block_to_image, sweetbean_experiment_to_html, or similar) when you need a rendered visual preview of an experiment block. It spins up a headless browser, executes the JavaScript, and returns a screenshot — use it to verify stimulus layout, timing overlays, or jsPsych plugin rendering before deploying to participants.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "html_content": {\n      "description": "A complete HTML document string (including jsPsych boilerplate and experiment JavaScript) to render. Typically the output of sweetbean_experiment_to_html or sweetbean_block_to_js wrapped in a full HTML page.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "html_content"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe function sleeps for 5 seconds after loading the page to allow jsPsych JavaScript to execute — each call has at least a 5-second latency. The screenshot is taken at 1920×1080 viewport and is NOT full-page (only the visible area is captured). The return value is a PIL Image object stored as a handle; pass that handle to downstream image-handling tools. Requires pyppeteer and Pillow to be installed; if either is missing the call will raise an ImportError at runtime. Chromium is downloaded on first pyppeteer use if not already cached.'
TOOL_PARAMETERS = { 'properties': { 'html_content': { 'description': 'A complete HTML document string '
                                                   '(including jsPsych boilerplate and '
                                                   'experiment JavaScript) to render. '
                                                   'Typically the output of '
                                                   'sweetbean_experiment_to_html or '
                                                   'sweetbean_block_to_js wrapped in a '
                                                   'full HTML page.',
                                    'type': 'string'}},
  'required': ['html_content'],
  'type': 'object'}
TOOL_NOTES = 'The function sleeps for 5 seconds after loading the page to allow jsPsych JavaScript to execute — each call has at least a 5-second latency. The screenshot is taken at 1920×1080 viewport and is NOT full-page (only the visible area is captured). The return value is a PIL Image object stored as a handle; pass that handle to downstream image-handling tools. Requires pyppeteer and Pillow to be installed; if either is missing the call will raise an ImportError at runtime. Chromium is downloaded on first pyppeteer use if not already cached.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.render_html_to_image
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
    def render_html_to_image(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after producing jsPsych HTML (via sweetbean_block_to_image, sweetbean_experiment_to_html, or similar) when you need a rendered visual preview of an experiment block.'
        return _impl(args or {})
