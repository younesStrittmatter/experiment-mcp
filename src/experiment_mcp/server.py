"""Entry point for the experiment-mcp server.

Phase 2 (t6e) scaffold. Boots a real MCP server on stdio (or SSE) with
**no tools registered yet** — the tool surface lands in a follow-up
once `psyneulink-psyche` Phase 1 t6 ships and we know what
`compile_task` / `run_task` / `validate_dataset` need to look like.

The shape mirrors `psyneulink_mcp.server` so that filling in tools
later is mechanical: drop modules under `tools/curated/` (hand-
authored) and `tools/generated/` (auto-generated from SweetPea /
SweetBean introspection), then call their `register(mcp)` here.
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("experiment-mcp")

# TODO(t6e): register tools from `tools/curated/` and `tools/generated/`.
# Mirror psyneulink_mcp.server:
#
#     from .tools.curated import compile as curated_compile
#     from .tools.curated import run as curated_run
#     from .tools.generated import register_all as register_generated
#
#     curated_compile.register(mcp)
#     curated_run.register(mcp)
#     register_generated(mcp)
#
# Keep all sweetpea / sweetbean imports inside the registered tool
# bodies behind try/except so the server still boots when the
# `experiments` extra is not installed.


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="experiment-mcp",
        description=(
            "experiment-mcp server. Defaults to stdio for in-process MCP "
            "clients; pass --transport sse to expose the same MCP over "
            "HTTP+SSE on a localhost port."
        ),
    )
    p.add_argument(
        "--transport",
        choices=("stdio", "sse"),
        default=os.environ.get("EXPERIMENT_MCP_TRANSPORT", "stdio"),
        help=(
            "Transport. stdio (default) for in-process MCP clients; "
            "sse for HTTP/SSE on --host:--port."
        ),
    )
    p.add_argument(
        "--host",
        default=os.environ.get("EXPERIMENT_MCP_HOST", "127.0.0.1"),
        help="(SSE only) bind host. Default 127.0.0.1.",
    )
    p.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("EXPERIMENT_MCP_PORT", "8766")),
        help="(SSE only) bind port. Default 8766.",
    )
    return p


def main(argv: list[str] | None = None) -> None:
    ns = _build_parser().parse_args(argv)
    if ns.transport == "stdio":
        mcp.run()
        return

    mcp.settings.host = ns.host
    mcp.settings.port = ns.port
    sse_path = getattr(mcp.settings, "sse_path", "/sse")
    print(
        f"experiment-mcp: serving sse on http://{ns.host}:{ns.port}{sse_path}",
        file=sys.stderr,
        flush=True,
    )
    asyncio.run(mcp.run_sse_async())


if __name__ == "__main__":
    main()
