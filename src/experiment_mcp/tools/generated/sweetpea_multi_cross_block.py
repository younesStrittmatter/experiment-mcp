"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'a957fadb2b7e5f798a3c53b633ad0dc5bd5617e8776553bc48505c68f7f82d10'
__exp_qualname__ = 'sweetpea.MultiCrossBlock'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_multi_cross_block'
TOOL_DESCRIPTION = 'Call this tool when the experiment design requires **multiple independent crossings** — i.e., when you need every combination of factors A×B to appear AND every combination of factors C×D to appear, but not necessarily A×B×C×D. Use it in place of `sweetpea_fully_cross_block` whenever you have more than one crossing group. Returns a Block handle to pass to `sweetpea_gen`, `sweetpea_iterate_gen`, or any tool that accepts a Block.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "alignment": {\n      "default": "EQUAL_PREAMBLE",\n      "description": "Controls preamble alignment across repeats. EQUAL_PREAMBLE (default) gives all repeats the same preamble length; FRONT_PREAMBLE places preamble only at the front.",\n      "enum": [\n        "EQUAL_PREAMBLE",\n        "FRONT_PREAMBLE"\n      ],\n      "type": "string"\n    },\n    "constraints": {\n      "description": "Handle strings for Constraint objects (e.g. Exclude, AtMostKInARow) that restrict the generated sequences. Pass an empty array if there are no constraints.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "crossings": {\n      "description": "List of crossing groups, each a list of Factor handle strings. Every combination within each group appears at least once. Trial count is determined by the largest product of level counts across all groups.",\n      "items": {\n        "items": {\n          "type": "string"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "design": {\n      "description": "Handle strings for every Factor in the design (one level from each factor appears in every trial).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "mode": {\n      "default": "EQUAL",\n      "description": "Controls how repeat blocks are sized relative to the base block. EQUAL (default) pads each repeat to the same length; MINIMAL uses the smallest valid size.",\n      "enum": [\n        "EQUAL",\n        "MINIMAL"\n      ],\n      "type": "string"\n    },\n    "require_complete_crossing": {\n      "default": true,\n      "description": "When true (default), every combination in each crossing must appear in every block. Set to false when some combinations are intentionally excluded via an Exclude constraint.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "design",\n    "crossings",\n    "constraints"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `crossings` list may reference the same Factor handle in more than one group — shared factors create constraints across crossings, not a Cartesian explosion. The number of trials per run equals the maximum product of level counts among all crossing groups, not the product of all crossing groups combined. Pass `require_complete_crossing: false` whenever any crossing combination is excluded via an `Exclude` constraint; failing to do so will cause synthesis to be unsatisfiable. `mode` and `alignment` are advanced parameters; omit them to get the defaults for typical designs.'
TOOL_PARAMETERS = { 'properties': { 'alignment': { 'default': 'EQUAL_PREAMBLE',
                                 'description': 'Controls preamble alignment across '
                                                'repeats. EQUAL_PREAMBLE (default) '
                                                'gives all repeats the same preamble '
                                                'length; FRONT_PREAMBLE places '
                                                'preamble only at the front.',
                                 'enum': ['EQUAL_PREAMBLE', 'FRONT_PREAMBLE'],
                                 'type': 'string'},
                  'constraints': { 'description': 'Handle strings for Constraint '
                                                  'objects (e.g. Exclude, '
                                                  'AtMostKInARow) that restrict the '
                                                  'generated sequences. Pass an empty '
                                                  'array if there are no constraints.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'crossings': { 'description': 'List of crossing groups, each a list '
                                                'of Factor handle strings. Every '
                                                'combination within each group appears '
                                                'at least once. Trial count is '
                                                'determined by the largest product of '
                                                'level counts across all groups.',
                                 'items': { 'items': {'type': 'string'},
                                            'type': 'array'},
                                 'type': 'array'},
                  'design': { 'description': 'Handle strings for every Factor in the '
                                             'design (one level from each factor '
                                             'appears in every trial).',
                              'items': {'type': 'string'},
                              'type': 'array'},
                  'mode': { 'default': 'EQUAL',
                            'description': 'Controls how repeat blocks are sized '
                                           'relative to the base block. EQUAL '
                                           '(default) pads each repeat to the same '
                                           'length; MINIMAL uses the smallest valid '
                                           'size.',
                            'enum': ['EQUAL', 'MINIMAL'],
                            'type': 'string'},
                  'require_complete_crossing': { 'default': True,
                                                 'description': 'When true (default), '
                                                                'every combination in '
                                                                'each crossing must '
                                                                'appear in every '
                                                                'block. Set to false '
                                                                'when some '
                                                                'combinations are '
                                                                'intentionally '
                                                                'excluded via an '
                                                                'Exclude constraint.',
                                                 'type': 'boolean'}},
  'required': ['design', 'crossings', 'constraints'],
  'type': 'object'}
TOOL_NOTES = 'The `crossings` list may reference the same Factor handle in more than one group — shared factors create constraints across crossings, not a Cartesian explosion. The number of trials per run equals the maximum product of level counts among all crossing groups, not the product of all crossing groups combined. Pass `require_complete_crossing: false` whenever any crossing combination is excluded via an `Exclude` constraint; failing to do so will cause synthesis to be unsatisfiable. `mode` and `alignment` are advanced parameters; omit them to get the defaults for typical designs.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.MultiCrossBlock
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
    def create_multi_cross_block(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when the experiment design requires **multiple independent crossings** — i.e., when you need every combination of factors A×B to appear AND every combination of factors C×D to appear, but not necessarily A×B×C×D.'
        return _impl(args or {})
