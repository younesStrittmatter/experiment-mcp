"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '44368c48a033544861eaa29a6f6b7f2417195fdd1a85d13f3e2408d8d0fe5374'
__exp_qualname__ = 'sweetpea.UniGen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_uni_gen'
TOOL_DESCRIPTION = 'Call this tool at step 2 of the SweetPea pipeline — after a Block (e.g. CrossBlock) has been declared with its factors and crossing — to sample one or more trial sequences with approximately uniform probability over the valid solution space. The result is a SamplingResult handle containing a list of trial-sequence dicts that can be passed to SweetBean stimulus/trial wiring in subsequent steps.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the SweetPea Block (e.g. CrossBlock) produced by a prior block-construction tool call.",\n      "type": "string"\n    },\n    "min_search": {\n      "default": false,\n      "description": "Enable minimum-search mode. Rarely needed; leave false unless you have a specific reason.",\n      "type": "boolean"\n    },\n    "sample_count": {\n      "description": "Number of trial sequences to sample. Each sequence is one independent run of the full design.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "use_cmsgen": {\n      "default": false,\n      "description": "Use CMSGen instead of the default UniGen SAT sampler. CMSGen can be faster on some designs but is less rigorously uniform.",\n      "type": "boolean"\n    }\n  },\n  "required": [\n    "block",\n    "sample_count"\n  ],\n  "type": "object"\n}\n\nNotes:\nUniGen guarantees approximately uniform sampling over satisfying assignments, which is stronger than the pseudo-random sampling of non-uniform generators. If the block has constraint errors (e.g. over-constrained crossing), `sample` returns an empty SamplingResult silently rather than raising — check that the returned sequence list is non-empty before proceeding. `min_search` is underdocumented upstream (marked TODO); avoid it unless you know what you need. Docker is never used (`use_docker=False` is hardcoded); the SAT solver runs in-process.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the SweetPea Block '
                                            '(e.g. CrossBlock) produced by a prior '
                                            'block-construction tool call.',
                             'type': 'string'},
                  'min_search': { 'default': False,
                                  'description': 'Enable minimum-search mode. Rarely '
                                                 'needed; leave false unless you have '
                                                 'a specific reason.',
                                  'type': 'boolean'},
                  'sample_count': { 'description': 'Number of trial sequences to '
                                                   'sample. Each sequence is one '
                                                   'independent run of the full '
                                                   'design.',
                                    'minimum': 1,
                                    'type': 'integer'},
                  'use_cmsgen': { 'default': False,
                                  'description': 'Use CMSGen instead of the default '
                                                 'UniGen SAT sampler. CMSGen can be '
                                                 'faster on some designs but is less '
                                                 'rigorously uniform.',
                                  'type': 'boolean'}},
  'required': ['block', 'sample_count'],
  'type': 'object'}
TOOL_NOTES = 'UniGen guarantees approximately uniform sampling over satisfying assignments, which is stronger than the pseudo-random sampling of non-uniform generators. If the block has constraint errors (e.g. over-constrained crossing), `sample` returns an empty SamplingResult silently rather than raising — check that the returned sequence list is non-empty before proceeding. `min_search` is underdocumented upstream (marked TODO); avoid it unless you know what you need. Docker is never used (`use_docker=False` is hardcoded); the SAT solver runs in-process.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.UniGen
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
    def create_uni_gen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at step 2 of the SweetPea pipeline — after a Block (e.g.'
        return _impl(args or {})
