"""Smoke + structural tests for the experiment-mcp generator pipeline.

These tests do **not** call the LLM. They validate the seam below the
adapter: introspection finds non-empty seed surfaces from sweetpea +
sweetbean, the dry-run orchestrator wires placeholder ToolSpecs through
the template, the resulting modules parse as valid Python and import,
and the rerender path round-trips on-disk metadata back through the
template without loss.

Symmetric in spirit with ``psyneulink-mcp/tests/test_introspection.py``
+ the orchestrator integration tests in that repo, kept lean here
because the generator surface is brand new and we only need the
"pipeline is wired" guarantee for the first commit.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Literal

import pytest

from experiment_mcp.generator import introspection, orchestrator, prompts, template
from experiment_mcp.generator.adapters.base import ToolSpec

# --------------------------------------------------------------------------- #
# introspection                                                               #
# --------------------------------------------------------------------------- #


@pytest.mark.integration
def test_default_seed_directives_yield_real_symbols() -> None:
    """`package: sweetpea` + `package: sweetbean` discover non-empty surfaces.

    Marked integration because it imports the live wrapped libraries —
    a plain `pytest` run skips it; CI / local `pytest -m integration`
    exercises the real surface.
    """
    syms = introspection.discover_seed_symbols(seeds_file=None)
    assert syms, "default seed directives should produce some symbols"
    roots = {s.root_module for s in syms}
    assert roots == {"sweetpea", "sweetbean"}, (
        f"default seeds must cover both wrapped libs; got {roots}"
    )


@pytest.mark.integration
def test_repo_seeds_file_discovers_both_roots() -> None:
    """The committed `generator/seeds.txt` covers sweetpea + sweetbean."""
    repo_root = Path(__file__).resolve().parent.parent
    seeds = repo_root / "generator" / "seeds.txt"
    assert seeds.exists(), f"missing repo seeds file at {seeds}"

    syms = introspection.discover_seed_symbols(seeds)
    assert len(syms) > 50, (
        f"committed seeds.txt should produce many symbols; got {len(syms)}"
    )
    roots = {s.root_module for s in syms}
    assert roots == {"sweetpea", "sweetbean"}
    kinds = {s.kind for s in syms}
    # Methods come from the explicit `method:` directives in the seeds file;
    # if introspection drops them silently, those tools never get generated.
    assert "method" in kinds, f"method-kind seeds should resolve; got {kinds}"


def test_filters_out_exception_subclasses() -> None:
    """`package:` walks must not surface `*Error` classes.

    Hermetic — uses a synthetic module so we don't depend on whatever
    sweetpea / sweetbean call their internal exceptions.
    """

    class FakeError(Exception):
        """Stand-in for any wrapped lib's error class."""

    def fake_function() -> None:
        """Stand-in for a real public function."""

    fake_module_name = "_experiment_mcp_test_fake_module"
    fake_module = type(sys)(fake_module_name)
    fake_module.FakeError = FakeError  # type: ignore[attr-defined]
    fake_module.fake_function = fake_function  # type: ignore[attr-defined]
    sys.modules[fake_module_name] = fake_module
    try:
        directives = [
            introspection.SeedDirective(kind="package", target=fake_module_name)
        ]
        syms = introspection.discover_from_directives(directives)
    finally:
        sys.modules.pop(fake_module_name, None)

    qualnames = {s.qualname for s in syms}
    assert f"{fake_module_name}.fake_function" in qualnames, (
        "non-exception public callables must be discovered"
    )
    assert f"{fake_module_name}.FakeError" not in qualnames, (
        "exception subclasses must be filtered out — agents don't construct them"
    )


# --------------------------------------------------------------------------- #
# template                                                                    #
# --------------------------------------------------------------------------- #


def _make_symbol(
    qualname: str,
    kind: Literal["class", "function", "method"],
    *,
    source: str = "def f(): pass\n",
) -> introspection.SymbolMeta:
    """Hand-build a SymbolMeta (decoupled from any live module)."""
    return introspection.SymbolMeta(
        qualname=qualname,
        kind=kind,
        source=source,
        docstring=None,
        module=qualname.rsplit(".", 1)[0] if "." in qualname else qualname,
        source_sha256="0" * 64,
    )


def _placeholder_spec() -> ToolSpec:
    return {
        "description": "x",
        "parameters": {"type": "object", "properties": {}, "required": []},
        "notes": "",
    }


def test_template_imports_correct_root_per_symbol() -> None:
    """sweetpea-rooted symbols import sweetpea; sweetbean-rooted import sweetbean.

    The cross-collision was the whole reason `_ROOT_ALIAS` exists in the
    template; this guards against a regression where every generated
    module imports the same wrong root.
    """
    sp_body = template.render_module(
        _make_symbol("sweetpea.CrossBlock", "class"),
        _placeholder_spec(),
        generated_by="dry-run",
    )
    sb_body = template.render_module(
        _make_symbol("sweetbean.Experiment", "class"),
        _placeholder_spec(),
        generated_by="dry-run",
    )
    assert "import sweetpea as sp" in sp_body
    assert "sp.CrossBlock" in sp_body
    assert "import sweetbean" not in sp_body

    assert "import sweetbean as sb" in sb_body
    assert "sb.Experiment" in sb_body
    assert "import sweetpea" not in sb_body


def test_module_stem_namespaces_by_root() -> None:
    """`Block` exists in BOTH wrapped libs — stems must not collide."""
    sp_block = _make_symbol("sweetpea.Block", "class")
    sb_block = _make_symbol("sweetbean.Block", "class")
    assert template.module_stem_for(sp_block) == "sweetpea_block"
    assert template.module_stem_for(sb_block) == "sweetbean_block"
    assert template.module_stem_for(sp_block) != template.module_stem_for(sb_block)


def test_method_template_carries_class_in_stem() -> None:
    """Method modules namespace by class so same-named methods don't collide."""
    a = _make_symbol("sweetbean.Experiment.to_html", "method")
    b = _make_symbol("sweetbean.Block.to_image", "method")
    assert template.module_stem_for(a) == "sweetbean_experiment_to_html"
    assert template.module_stem_for(b) == "sweetbean_block_to_image"


# --------------------------------------------------------------------------- #
# prompts                                                                     #
# --------------------------------------------------------------------------- #


def test_prompt_mentions_root_for_classes() -> None:
    """The prompt names the wrapped lib so the LLM grounds its output."""
    sym = _make_symbol("sweetpea.CrossBlock", "class")
    p = prompts.render_prompt(sym, feedback=None)
    assert "sweetpea" in p
    assert "sweetpea.CrossBlock" in p
    assert "PsyNeuLink" not in p, (
        "prompt text must not leak from the sibling repo"
    )


def test_prompt_method_addendum_is_generic() -> None:
    """No method should hit a sibling-leaked per-method override.

    If experiment-mcp ever grows hand-tuned method addenda, this test
    will start failing for those — that's the right time to update it.
    """
    sym = _make_symbol("sweetbean.Experiment.to_html", "method")
    p = prompts.render_prompt(sym, feedback=None)
    assert "Method-kind contract" in p
    assert "Composition" not in p, (
        "PsyNeuLink-specific method hints must not be reachable from "
        "experiment-mcp's prompts"
    )


# --------------------------------------------------------------------------- #
# orchestrator (dry-run)                                                      #
# --------------------------------------------------------------------------- #


@pytest.mark.integration
def test_dry_run_writes_parseable_module(tmp_path, monkeypatch) -> None:
    """`--dry-run --limit 1` writes one Python file that parses + imports.

    Integration-marked because it imports sweetpea / sweetbean to walk
    them. The test redirects GENERATED_DIR to a tmp dir so it doesn't
    pollute the repo.
    """
    import ast

    monkeypatch.setattr(orchestrator, "GENERATED_DIR", tmp_path)
    rc = orchestrator.main(["--dry-run", "--limit", "1"])
    assert rc == 0

    py_files = sorted(p for p in tmp_path.iterdir() if p.suffix == ".py")
    py_files = [p for p in py_files if not p.name.startswith("__")]
    assert len(py_files) == 1, f"expected 1 generated module, got {py_files}"

    body = py_files[0].read_text(encoding="utf-8")
    ast.parse(body, filename=str(py_files[0]))
    assert "TODO: regen with adapter" in body
    assert "__exp_root__" in body


# --------------------------------------------------------------------------- #
# rerender                                                                    #
# --------------------------------------------------------------------------- #


def test_rerender_round_trips_metadata(tmp_path) -> None:
    """A module written by the template re-renders to the same metadata.

    Hermetic — synthesises a module on disk, calls the rerender path,
    then checks the constants survived.
    """
    from experiment_mcp.generator.rerender import rerender_path

    sym = _make_symbol("sweetbean.Experiment", "class")
    body = template.render_module(sym, _placeholder_spec(), generated_by="dry-run")
    p = tmp_path / "sweetbean_experiment.py"
    p.write_text(body, encoding="utf-8")

    rerender_path(p)

    rendered = p.read_text(encoding="utf-8")
    assert "__exp_qualname__ = 'sweetbean.Experiment'" in rendered
    assert "__exp_kind__ = 'class'" in rendered
    assert "__exp_root__ = 'sweetbean'" in rendered
    assert "import sweetbean as sb" in rendered


def test_rerender_rejects_modules_missing_metadata(tmp_path) -> None:
    """A stray .py without the required constants is reported, not crashed on."""
    from experiment_mcp.generator.rerender import RerenderError, rerender_path

    p = tmp_path / "stray.py"
    p.write_text("# not a generated module\n", encoding="utf-8")
    with pytest.raises(RerenderError):
        rerender_path(p)


# --------------------------------------------------------------------------- #
# orchestrator helpers                                                        #
# --------------------------------------------------------------------------- #


def test_augment_with_historical_failures_appends_block() -> None:
    """The historical-failures block is appended to the description verbatim."""
    spec: ToolSpec = {"description": "create a thing", "parameters": {}, "notes": ""}
    failures = [
        {"number": 17, "title": "broken kwarg", "body": "agent passed missing arg"},
        {"number": 18, "title": "wrong default", "body": ""},
    ]
    out = orchestrator._augment_with_historical_failures(spec, failures)
    assert out is not spec, "must return a new dict"
    assert "## HISTORICAL FAILURES" in out["description"]
    assert "#17 — broken kwarg" in out["description"]
    assert "#18 — wrong default" in out["description"]


def test_augment_with_historical_failures_no_op_when_empty() -> None:
    spec: ToolSpec = {"description": "x", "parameters": {}, "notes": ""}
    out = orchestrator._augment_with_historical_failures(spec, [])
    assert out is spec
