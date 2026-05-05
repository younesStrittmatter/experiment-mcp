"""Build-time generator for the auto layer of experiment-mcp tools.

Symmetric with ``psyneulink_mcp.generator``. This subpackage walks
SweetPea + SweetBean's public API surface, asks an LLM for a
:class:`ToolSpec` per symbol, and writes one MCP tool module per symbol
into ``src/experiment_mcp/tools/generated/``.

Never imported by the runtime server. Entry point is the
``experiment-mcp-generate`` console script (or
``scripts/generate_tools.py``).
"""
