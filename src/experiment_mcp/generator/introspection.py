"""Resolve SweetPea / SweetBean symbols from a seed file.

Symmetric with ``psyneulink_mcp.generator.introspection``. The four
seed directives (``import-walk``, ``symbol``, ``package``, ``method``)
behave identically; the only domain-specific knob is ``root_modules``,
the list of top-level packages that ``import-walk`` recognises as
"the libraries we wrap." For experiment-mcp that defaults to
``["sweetpea", "sweetbean"]``.

Anything matching ``BaseException`` is silently filtered — the
generator should not emit MCP tools for ``*Error`` classes (they're
raised, not constructed).
"""

from __future__ import annotations

import ast
import hashlib
import importlib
import inspect
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

ROOT_MODULES_DEFAULT: tuple[str, ...] = ("sweetpea", "sweetbean")


@dataclass(frozen=True)
class SymbolMeta:
    """One SweetPea / SweetBean symbol slated for tool generation.

    ``source_sha256`` lets the orchestrator skip regenerating a tool
    when the upstream source hasn't changed.

    For ``kind == "method"``, ``qualname`` includes the owning class:
    e.g. ``sweetpea.CrossBlock.crossing``. The class qualname
    is exposed via :attr:`class_qualname`; ``short_name`` is just the
    method name (the last segment).

    The tuple ``root_module`` (``sweetpea`` / ``sweetbean`` / …) is
    inferred from ``qualname.split('.', 1)[0]`` — the template uses
    it to pick the right ``import sweetpea as sp`` / ``import sweetbean
    as sb`` line for each generated module.
    """

    qualname: str
    kind: Literal["class", "function", "method"]
    source: str
    docstring: str | None
    module: str
    source_sha256: str

    @property
    def short_name(self) -> str:
        return self.qualname.rsplit(".", 1)[-1]

    @property
    def root_module(self) -> str:
        """First qualname segment — the top-level package we wrap."""
        return self.qualname.split(".", 1)[0]

    @property
    def class_qualname(self) -> str | None:
        """Qualname of the class that owns this method (method kind only)."""
        if self.kind != "method":
            return None
        parent, _, _ = self.qualname.rpartition(".")
        return parent or None

    @property
    def class_short_name(self) -> str | None:
        """Short name of the owning class (method kind only)."""
        parent = self.class_qualname
        if parent is None:
            return None
        return parent.rsplit(".", 1)[-1]


@dataclass(frozen=True)
class SeedDirective:
    """One non-comment line from ``seeds.txt``."""

    kind: Literal["import-walk", "symbol", "package", "method"]
    target: str


# --------------------------------------------------------------------------- #
# seeds.txt parser                                                            #
# --------------------------------------------------------------------------- #


def parse_seeds_file(path: Path) -> list[SeedDirective]:
    """Read ``seeds.txt``. Blank lines and ``#`` comments are skipped.

    Each non-comment line must match ``<kind>: <target>`` where kind is
    one of ``import-walk``, ``symbol``, ``package``, or ``method``.
    Anything else raises :class:`ValueError` with the offending line
    number.
    """
    if not path.exists():
        return []
    directives: list[SeedDirective] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(
                f"{path}:{lineno}: missing ':' in seed directive {line!r}"
            )
        kind_raw, _, target_raw = line.partition(":")
        kind = kind_raw.strip()
        target = target_raw.strip()
        if kind not in {"import-walk", "symbol", "package", "method"}:
            raise ValueError(
                f"{path}:{lineno}: unknown seed directive kind {kind!r}; "
                "expected one of import-walk, symbol, package, method"
            )
        if not target:
            raise ValueError(f"{path}:{lineno}: empty target in seed directive")
        directives.append(SeedDirective(kind=kind, target=target))  # type: ignore[arg-type]
    return directives


def default_seed_directives() -> list[SeedDirective]:
    """Fallback when no ``seeds.txt`` exists: walk both top-level packages."""
    return [
        SeedDirective(kind="package", target="sweetpea"),
        SeedDirective(kind="package", target="sweetbean"),
    ]


# --------------------------------------------------------------------------- #
# directive dispatch                                                          #
# --------------------------------------------------------------------------- #


def discover_from_directives(
    directives: Iterable[SeedDirective],
    *,
    root_modules: Iterable[str] = ROOT_MODULES_DEFAULT,
) -> list[SymbolMeta]:
    """Run every directive and return a deduped, sorted symbol list.

    ``root_modules`` is the list of top-level packages that ``import-walk``
    treats as "ours" — symbols imported from anything else are ignored.
    """
    roots = tuple(root_modules)
    qualnames: set[str] = set()
    method_qualnames: set[str] = set()
    for d in directives:
        if d.kind == "import-walk":
            qualnames.update(_qualnames_from_import_walk(d.target, roots))
        elif d.kind == "symbol":
            qualnames.add(d.target)
        elif d.kind == "package":
            qualnames.update(_qualnames_from_package(d.target))
        elif d.kind == "method":
            method_qualnames.add(d.target)

    symbols: list[SymbolMeta] = []
    # ``method`` qualnames need a different resolver because the parent
    # of the last segment is a class, not a module — ``importlib`` will
    # refuse to import e.g. ``sweetpea.CrossBlock`` as a module.
    for qualname in sorted(method_qualnames):
        meta = _resolve_method_qualname(qualname)
        if meta is not None:
            symbols.append(meta)
    for qualname in sorted(qualnames):
        meta = _resolve_qualname(qualname)
        if meta is not None:
            symbols.append(meta)
    symbols.sort(key=lambda s: (s.qualname, s.kind))
    return symbols


def discover_seed_symbols(
    seeds_file: Path | None = None,
    *,
    root_modules: Iterable[str] = ROOT_MODULES_DEFAULT,
) -> list[SymbolMeta]:
    """Top-level entry: load ``seeds_file`` or fall back to the default."""
    directives = (
        parse_seeds_file(seeds_file) if seeds_file and seeds_file.exists() else []
    )
    if not directives:
        directives = default_seed_directives()
    return discover_from_directives(directives, root_modules=root_modules)


# --------------------------------------------------------------------------- #
# import-walk                                                                 #
# --------------------------------------------------------------------------- #


def iter_seed_module_files(seed_module_qualname: str) -> list[Path]:
    """Sorted list of ``.py`` files in the package, dunders excluded."""
    pkg = importlib.import_module(seed_module_qualname)
    pkg_file = getattr(pkg, "__file__", None)
    if pkg_file is None:
        return []
    pkg_dir = Path(pkg_file).parent
    if not pkg_dir.is_dir():
        return []
    return sorted(
        p
        for p in pkg_dir.iterdir()
        if p.suffix == ".py" and not p.name.startswith("__")
    )


def _module_root(module_name: str, roots: tuple[str, ...]) -> str | None:
    """Return the matching root from ``roots`` if ``module_name`` is under it."""
    for root in roots:
        if module_name == root or module_name.startswith(root + "."):
            return root
    return None


def _qualnames_from_import_walk(
    seed_module_qualname: str,
    roots: tuple[str, ...],
) -> set[str]:
    """Symbols used by any .py file in ``seed_module_qualname``'s package.

    Catches the same three idioms as the sibling: ``from <root> import X``,
    ``from <root>.sub import X``, and ``import <root> [as alias]`` followed
    by ``alias.X`` attribute access.
    """
    qualnames: set[str] = set()
    for py_file in iter_seed_module_files(seed_module_qualname):
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"), filename=str(py_file))
        except (OSError, SyntaxError):
            continue

        # Per-root: name binding (`import sweetpea as sp` → {"sp"}).
        bindings_by_root: dict[str, set[str]] = {root: set() for root in roots}

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if not node.module:
                    continue
                root = _module_root(node.module, roots)
                if root is None:
                    continue
                for alias in node.names:
                    if alias.name == "*" or alias.name.startswith("_"):
                        continue
                    qualnames.add(f"{root}.{alias.name}")
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    root = _module_root(alias.name, roots)
                    if root is None:
                        continue
                    bindings_by_root[root].add(
                        alias.asname or alias.name.split(".", 1)[0]
                    )

        flat_bindings = {b: root for root, bs in bindings_by_root.items() for b in bs}
        if flat_bindings:
            for node in ast.walk(tree):
                if not isinstance(node, ast.Attribute):
                    continue
                base = node.value
                if not isinstance(base, ast.Name):
                    continue
                root = flat_bindings.get(base.id)
                if root is None:
                    continue
                if node.attr.startswith("_"):
                    continue
                qualnames.add(f"{root}.{node.attr}")
    return qualnames


# --------------------------------------------------------------------------- #
# package walk                                                                #
# --------------------------------------------------------------------------- #


def _qualnames_from_package(package_qualname: str) -> set[str]:
    """Every public class/function on the live module object.

    Filters silently:

    * Names starting with ``_`` (private-by-convention).
    * Exception / Warning subclasses — these are raised by the library,
      not constructed by an agent. Surfacing them as MCP tools wastes
      LLM regen budget and produces nonsensical "create FooError"
      descriptions.
    """
    try:
        module = importlib.import_module(package_qualname)
    except ImportError:
        return set()
    qualnames: set[str] = set()
    for name in dir(module):
        if name.startswith("_"):
            continue
        try:
            obj = getattr(module, name)
        except AttributeError:
            continue
        if inspect.isclass(obj):
            if issubclass(obj, BaseException):
                continue
            qualnames.add(f"{package_qualname}.{name}")
        elif inspect.isfunction(obj):
            qualnames.add(f"{package_qualname}.{name}")
    return qualnames


# --------------------------------------------------------------------------- #
# resolution                                                                  #
# --------------------------------------------------------------------------- #


def _resolve_qualname(qualname: str) -> SymbolMeta | None:
    """Resolve ``pkg.attr`` to a :class:`SymbolMeta`; return None on failure.

    "Failure" includes: import error on the package, missing attribute,
    non-class / non-function object, exception subclass, or
    :func:`inspect.getsource` raising (which it does for C-implemented
    callables).
    """
    if "." not in qualname:
        return None
    package_qualname, _, attr = qualname.rpartition(".")
    try:
        package = importlib.import_module(package_qualname)
    except ImportError:
        return None
    try:
        obj = getattr(package, attr)
    except AttributeError:
        return None

    if inspect.isclass(obj):
        if issubclass(obj, BaseException):
            return None
        kind: Literal["class", "function"] = "class"
    elif inspect.isfunction(obj) or inspect.isbuiltin(obj):
        kind = "function"
    else:
        return None

    try:
        source = inspect.getsource(obj)
    except (OSError, TypeError):
        return None

    return SymbolMeta(
        qualname=qualname,
        kind=kind,
        source=source,
        docstring=inspect.getdoc(obj),
        module=getattr(obj, "__module__", package_qualname),
        source_sha256=hashlib.sha256(source.encode("utf-8")).hexdigest(),
    )


def _resolve_method_qualname(qualname: str) -> SymbolMeta | None:
    """Resolve ``pkg.ClassName.method_name`` to a method-kind :class:`SymbolMeta`.

    Returns ``None`` when:
    * the parent qualname doesn't resolve to a class,
    * the named attribute is missing or isn't a function/descriptor,
    * the source can't be read (C-implemented descriptors etc.).
    """
    class_qualname, _, method_name = qualname.rpartition(".")
    if not class_qualname or not method_name:
        return None
    class_meta = _resolve_qualname(class_qualname)
    if class_meta is None or class_meta.kind != "class":
        return None
    try:
        package = importlib.import_module(
            class_qualname.rpartition(".")[0]
        )
        cls = getattr(package, class_meta.short_name)
    except (ImportError, AttributeError):
        return None
    method = inspect.getattr_static(cls, method_name, None)
    if method is None:
        return None
    if isinstance(method, (classmethod, staticmethod)):
        method = method.__func__
    if not (inspect.isfunction(method) or inspect.ismethod(method)):
        return None
    try:
        source = inspect.getsource(method)
    except (OSError, TypeError):
        return None
    return SymbolMeta(
        qualname=qualname,
        kind="method",
        source=source,
        docstring=inspect.getdoc(method),
        module=getattr(method, "__module__", class_meta.module),
        source_sha256=hashlib.sha256(source.encode("utf-8")).hexdigest(),
    )
