from __future__ import annotations

import argparse
import ast
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


YEAR_RE = re.compile(r"^_(20\d{2})$")
SKIP_DIRS = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".pytest_cache",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "site-packages",
    "venv",
}


def dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def corpus_group(path: Path, root: Path) -> str:
    for part in path.relative_to(root).parts:
        match = YEAR_RE.match(part)
        if match:
            return match.group(1)
    return "shared"


def iter_python_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.py")
        if not any(part in SKIP_DIRS for part in path.relative_to(root).parts)
    )


def analyze(root: Path) -> dict[str, Any]:
    python_files = iter_python_files(root)
    calls: Counter[str] = Counter()
    bases: Counter[str] = Counter()
    imports: Counter[str] = Counter()
    method_calls: Counter[str] = Counter()
    per_group: dict[str, Counter[str]] = defaultdict(Counter)
    per_file: list[dict[str, object]] = []
    parse_errors: list[dict[str, object]] = []

    total_lines = 0
    total_classes = 0
    construct_classes = 0

    for path in python_files:
        relative = path.relative_to(root).as_posix()
        source = path.read_text(encoding="utf-8", errors="replace")
        line_count = len(source.splitlines())
        total_lines += line_count
        group = corpus_group(path, root)

        try:
            tree = ast.parse(source, filename=relative)
        except SyntaxError as exc:
            parse_errors.append(
                {
                    "file": relative,
                    "line": exc.lineno,
                    "offset": exc.offset,
                    "error": exc.msg,
                }
            )
            per_group[group].update(files=1, lines=line_count, parse_errors=1)
            continue

        file_classes = 0
        file_constructs = 0
        file_plays = 0
        file_waits = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                imports[node.module or ""] += 1
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imports[alias.name] += 1
            elif isinstance(node, ast.ClassDef):
                file_classes += 1
                total_classes += 1
                for base in node.bases:
                    name = dotted_name(base)
                    if name:
                        bases[name] += 1
                if any(
                    isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and item.name == "construct"
                    for item in node.body
                ):
                    file_constructs += 1
                    construct_classes += 1
            elif isinstance(node, ast.Call):
                name = dotted_name(node.func)
                if not name:
                    continue
                calls[name.rsplit(".", 1)[-1]] += 1
                if name.startswith("self."):
                    method_calls[name] += 1
                    if name == "self.play":
                        file_plays += 1
                    elif name == "self.wait":
                        file_waits += 1

        per_group[group].update(
            files=1,
            lines=line_count,
            classes=file_classes,
            construct_classes=file_constructs,
            play_calls=file_plays,
            wait_calls=file_waits,
        )
        per_file.append(
            {
                "file": relative,
                "lines": line_count,
                "classes": file_classes,
                "construct_classes": file_constructs,
                "play_calls": file_plays,
                "wait_calls": file_waits,
            }
        )

    return {
        "root": str(root),
        "method": "Python AST only; target modules were not imported or executed",
        "summary": {
            "python_files": len(python_files),
            "lines": total_lines,
            "classes": total_classes,
            "classes_with_construct": construct_classes,
            "parse_errors": len(parse_errors),
        },
        "imports": imports.most_common(20),
        "direct_bases": bases.most_common(30),
        "self_method_calls": method_calls.most_common(30),
        "common_calls": calls.most_common(80),
        "per_group": {key: dict(value) for key, value in sorted(per_group.items())},
        "top_files_by_play_calls": sorted(
            per_file, key=lambda item: int(item["play_calls"]), reverse=True
        )[:25],
        "top_files_by_construct_classes": sorted(
            per_file, key=lambda item: int(item["construct_classes"]), reverse=True
        )[:25],
        "parse_errors": parse_errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a read-only AST inventory of a Python/Manim repository."
    )
    parser.add_argument("repo_root", type=Path, help="Repository root to inspect")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional JSON output file; stdout is always used when omitted",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.repo_root.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"repository directory not found: {root}")

    rendered = json.dumps(analyze(root), ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = args.output.expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
