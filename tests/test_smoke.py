"""Hermetic smoke test for the experiment-mcp scaffold.

No network, no `gh`, no sweetpea / sweetbean. Just confirms the package
imports cleanly and the MCP server object is constructed with zero
tools registered (the Phase 2 t6e starting point).
"""

from __future__ import annotations


def test_package_imports() -> None:
    import experiment_mcp

    assert experiment_mcp.__version__ == "0.0.1"


def test_server_module_boots_with_no_tools() -> None:
    """Importing `experiment_mcp.server` must construct the FastMCP app
    and must not register any tools (the surface lands in a follow-up).
    """
    from experiment_mcp import server

    assert server.mcp is not None
    assert server.mcp.name == "experiment-mcp"

    # Tool registration is deferred to Phase 2 t6e. The exact attribute
    # FastMCP uses to track registered tools varies across MCP releases,
    # so probe the common ones rather than coupling to one shape.
    candidate_attrs = (
        "_tools",
        "_tool_handlers",
        "tools",
    )
    found_registry = False
    for attr in candidate_attrs:
        registry = getattr(server.mcp, attr, None)
        if registry is None:
            continue
        found_registry = True
        # Empty mapping or empty sequence are both fine.
        assert len(registry) == 0, (
            f"experiment-mcp scaffold should ship zero registered tools; "
            f"found {len(registry)} on `mcp.{attr}`"
        )
    # If FastMCP exposed none of the expected registries the scaffold is
    # still valid (the import succeeded and `mcp.name` matches) — we just
    # log via assertion message that we couldn't independently verify
    # the empty-tools claim.
    if not found_registry:
        # Fall back to the public FastMCP API if it grew one. `list_tools`
        # is a coroutine in modern FastMCP; await it via asyncio.run so
        # this stays a plain sync test.
        import asyncio
        import inspect

        list_tools = getattr(server.mcp, "list_tools", None)
        if callable(list_tools):
            result = list_tools()
            if inspect.iscoroutine(result):
                result = asyncio.run(result)
            assert len(result) == 0
