#!/usr/bin/env python3
"""Summarize repository structure as JSON.

Usage: python tools/skills/summarize_repo.py --workspace-root . --depth 2
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys

try:
    import tomllib as toml
except Exception:
    toml = None


def read_pyproject(path: str) -> dict | None:
    if not toml:
        return None
    try:
        with open(path, "rb") as f:
            return toml.load(f)
    except Exception:
        return None


def read_setup_name(path: str) -> str | None:
    try:
        text = open(path, "r", encoding="utf-8").read()
    except Exception:
        return None
    # Try quick regex for name='pkg'
    m = re.search(r"name\s*=\s*['\"]([^'\"]+)['\"]", text)
    if m:
        return m.group(1)
    # Try to AST-parse and find setup(...) call with keyword 'name'
    try:
        tree = ast.parse(text)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'setup':
                for kw in node.keywords:
                    if kw.arg == 'name' and isinstance(kw.value, ast.Constant):
                        return kw.value.value
    except Exception:
        pass
    return None


def list_packages(root: str, depth: int) -> list:
    out = []
    for entry in sorted(os.listdir(root)):
        p = os.path.join(root, entry)
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "__init__.py")):
            pkg = {"name": entry, "subpackages": []}
            if depth > 1:
                try:
                    for sub in sorted(os.listdir(p)):
                        sp = os.path.join(p, sub)
                        if os.path.isdir(sp) and os.path.exists(os.path.join(sp, "__init__.py")):
                            pkg["subpackages"].append(sub)
                except Exception:
                    pass
            out.append(pkg)
    return out


def top_level_modules(root: str) -> list:
    mods = []
    for f in sorted(os.listdir(root)):
        if f.endswith('.py') and f != '__init__.py':
            mods.append(f)
    return mods


def collect_tests(root: str) -> list:
    tests_dir = os.path.join(root, 'tests')
    if not os.path.isdir(tests_dir):
        tests_dir = os.path.join(root, 'test')
        if not os.path.isdir(tests_dir):
            return []
    files = []
    for dirpath, dirnames, filenames in os.walk(tests_dir):
        for fn in filenames:
            if fn.endswith('.py'):
                rel = os.path.relpath(os.path.join(dirpath, fn), root)
                files.append(rel)
    return sorted(files)


def notable_files(root: str) -> list:
    candidates = ['README.md', 'README.rst', 'LICENSE', 'LICENSE.md', 'setup.py', 'pyproject.toml']
    return [c for c in candidates if os.path.exists(os.path.join(root, c))]


def summarize(root: str, depth: int) -> dict:
    root = os.path.abspath(root)
    pkg_name = None
    pyproject = os.path.join(root, 'pyproject.toml')
    if os.path.exists(pyproject):
        data = read_pyproject(pyproject)
        if data:
            # Try common locations for project name
            name = data.get('project', {}).get('name') if isinstance(data.get('project'), dict) else None
            if not name:
                name = data.get('tool', {}).get('poetry', {}).get('name') if isinstance(data.get('tool'), dict) else None
            pkg_name = name
    setup_py = os.path.join(root, 'setup.py')
    if not pkg_name and os.path.exists(setup_py):
        pkg_name = read_setup_name(setup_py)

    packages = list_packages(root, depth)
    modules = top_level_modules(root)
    tests = collect_tests(root)
    notes = notable_files(root)

    summary = f"Repository at {os.path.basename(root)}: {len(packages)} package(s), {len(modules)} top-level module(s), {len(tests)} test file(s)."

    return {
        'summary': summary,
        'package_name': pkg_name,
        'packages': packages,
        'top_level_modules': modules,
        'tests': tests[:20],
        'notable_files': notes,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description='Summarize repository structure')
    ap.add_argument('--workspace-root', '-w', default='.', help='Repository root')
    ap.add_argument('--depth', '-d', type=int, default=2, help='Directory depth for package discovery')
    ap.add_argument('--pretty', action='store_true', help='Pretty-print JSON')
    args = ap.parse_args(argv)

    out = summarize(args.workspace_root, args.depth)
    if args.pretty:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
