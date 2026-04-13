#!/usr/bin/env python3
"""Validate local markdown internal links and backtick path references.

Default scope is README.md so local validation, CI validation, and semantic
merge all measure the same bounded baseline in Wave B. Pass --all-markdown to
run the broader manual audit that will be normalized in Wave C.
"""
from __future__ import annotations

import argparse
import pathlib
import re

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BACKTICK_RE = re.compile(r"`([^`]+)`")

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "#")
VALID_BACKTICK_SUFFIXES = (".md", ".yaml", ".yml", ".json", ".py", ".sh", "/")


def looks_like_local_path(text: str) -> bool:
    candidate = text.strip().strip('"').strip("'")
    if not candidate or " " in candidate or '<' in candidate or '>' in candidate:
        return False
    if candidate.startswith(SKIP_PREFIXES):
        return False
    if candidate.startswith("<") and candidate.endswith(">"):
        candidate = candidate[1:-1].strip()
    if candidate.startswith(("./", "../")):
        return True
    if "/" not in candidate:
        return False
    return candidate.endswith(VALID_BACKTICK_SUFFIXES)


def normalize_target(raw: str) -> str:
    target = raw.strip().strip('"').strip("'")
    if target.startswith('<') and target.endswith('>'):
        target = target[1:-1].strip()
    if '#' in target:
        target = target.split('#', 1)[0]
    if '?' in target:
        target = target.split('?', 1)[0]
    return target.strip()


def iter_targets(text: str):
    yield from MARKDOWN_LINK_RE.findall(text)
    for ref in BACKTICK_RE.findall(text):
        if looks_like_local_path(ref):
            yield ref


def path_exists(base_file: pathlib.Path, raw_target: str, root: pathlib.Path) -> bool:
    target = normalize_target(raw_target)
    if not target or target.startswith(SKIP_PREFIXES):
        return True

    candidates = []
    if target.startswith('/'):
        candidates.append(root / target.lstrip('/'))
    else:
        candidates.append(base_file.parent / target)
        candidates.append(root / target)
    return any(c.exists() for c in candidates)


def check_markdown_files(root: pathlib.Path, files: list[pathlib.Path]) -> list[str]:
    failures: list[str] = []
    for md in files:
        text = md.read_text(encoding='utf-8')
        for target in iter_targets(text):
            if not path_exists(md, target, root):
                failures.append(f"{md.relative_to(root).as_posix()}: missing local target '{target}'")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='*', help='Optional markdown files to validate.')
    parser.add_argument(
        '--all-markdown',
        action='store_true',
        help='Validate all markdown files in repository (broader manual audit scope).',
    )
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parents[1]

    if args.paths:
        files = [root / p for p in args.paths]
    elif args.all_markdown:
        files = sorted(root.rglob('*.md'))
    else:
        files = [root / 'README.md']

    markdown_files = [p for p in files if p.suffix == '.md' and p.exists()]
    failures = check_markdown_files(root, markdown_files)

    if failures:
        for failure in failures:
            print('FAIL', failure)
        return 1

    print(f'Internal link validation passed ({len(markdown_files)} markdown files).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
