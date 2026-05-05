"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'bc6bd23e4642409bc232bba4c9c92759dfd7270047516a65d16b708ed2ca1faf'
__exp_qualname__ = 'sweetpea.save_experiments_csv'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'save_experiments_csv'
TOOL_DESCRIPTION = 'Call this tool after generating a trial sequence (via gen, iterate_gen, or similar sampling tools) when you want to persist the experiment data to disk as CSV files — for example, before handing the sequence off to a human experimenter or archiving results. It writes one CSV file per experiment in the list, using only the non-hidden factors from the block\'s design as columns. Each output file is named `<file_prefix>_<index>.csv`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the SweetPea Block (e.g. from cross_block or multi_cross_block) whose design defines which factors appear as CSV columns.",\n      "type": "string"\n    },\n    "experiments": {\n      "description": "List of experiment dicts as returned by gen, iterate_gen, or similar sampling tools. Each dict maps factor names to lists of level values.",\n      "items": {\n        "additionalProperties": {\n          "type": "array"\n        },\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "file_prefix": {\n      "default": "experiment",\n      "description": "Prefix for output CSV filenames. Files are written as <file_prefix>_0.csv, <file_prefix>_1.csv, etc. Defaults to \'experiment\'.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "block",\n    "experiments"\n  ],\n  "type": "object"\n}\n\nNotes:\nHidden factors (internal SweetPea bookkeeping columns) are silently excluded from the CSV output — only agent-visible factors from the block\'s design appear as columns. Files are written relative to the server process\'s current working directory; there is no way to specify an absolute path through this tool. If `experiments` contains multiple dicts (e.g. from iterate_gen), each produces a separate numbered file. The return value is the result of the internal `_experiments_to_csv` helper and is not a handle — do not pass it to downstream tools.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the SweetPea Block '
                                            '(e.g. from cross_block or '
                                            'multi_cross_block) whose design defines '
                                            'which factors appear as CSV columns.',
                             'type': 'string'},
                  'experiments': { 'description': 'List of experiment dicts as '
                                                  'returned by gen, iterate_gen, or '
                                                  'similar sampling tools. Each dict '
                                                  'maps factor names to lists of level '
                                                  'values.',
                                   'items': { 'additionalProperties': {'type': 'array'},
                                              'type': 'object'},
                                   'type': 'array'},
                  'file_prefix': { 'default': 'experiment',
                                   'description': 'Prefix for output CSV filenames. '
                                                  'Files are written as '
                                                  '<file_prefix>_0.csv, '
                                                  '<file_prefix>_1.csv, etc. Defaults '
                                                  "to 'experiment'.",
                                   'type': 'string'}},
  'required': ['block', 'experiments'],
  'type': 'object'}
TOOL_NOTES = "Hidden factors (internal SweetPea bookkeeping columns) are silently excluded from the CSV output — only agent-visible factors from the block's design appear as columns. Files are written relative to the server process's current working directory; there is no way to specify an absolute path through this tool. If `experiments` contains multiple dicts (e.g. from iterate_gen), each produces a separate numbered file. The return value is the result of the internal `_experiments_to_csv` helper and is not a handle — do not pass it to downstream tools."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.save_experiments_csv
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
    def save_experiments_csv(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after generating a trial sequence (via gen, iterate_gen, or similar sampling tools) when you want to persist the experiment data to disk as CSV files — for example, before handing the sequence off to a human experimenter or archiving results.'
        return _impl(args or {})
