#!/usr/bin/env python3
"""Run offline structural checks for the Copenhagen student handbook.

This script deliberately does not fetch URLs. A passing result means the source
register is structurally consistent, not that external facts are still current.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path


ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", re.MULTILINE)
URL_RE = re.compile(r"https?://[^\s<>]+")
INPUT_RE = re.compile(r"\\input\{([^}]+)\}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", help="handbook repository root")
    parser.add_argument("--max-age-days", type=int, default=370, help="warn when a claim is older than this")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.repo).resolve()
    problems: list[str] = []
    warnings: list[str] = []

    required = [
        "main.tex",
        "SOURCE_REGISTER.md",
        "SOCIAL_CONTENT_POLICY.md",
        "COPYRIGHT.md",
        "CONTRIBUTING.md",
    ]
    for relative in required:
        if not (root / relative).is_file():
            problems.append(f"missing required file: {relative}")

    if problems:
        return report(root, problems, warnings, 0)

    main_tex = (root / "main.tex").read_text(encoding="utf-8")
    for include in INPUT_RE.findall(main_tex):
        relative = include if Path(include).suffix else include + ".tex"
        if not (root / relative).is_file():
            problems.append(f"main.tex includes missing file: {relative}")

    register = (root / "SOURCE_REGISTER.md").read_text(encoding="utf-8")
    rows = ROW_RE.findall(register)
    if not rows:
        problems.append("SOURCE_REGISTER.md contains no parseable claim rows")

    seen: set[str] = set()
    today = dt.date.today()
    for claim_id, _topic, source_file, source, verified_text in rows:
        claim_id = claim_id.strip()
        if claim_id in seen:
            problems.append(f"duplicate Claim ID: {claim_id}")
        seen.add(claim_id)

        source_path = Path(source_file.strip())
        candidates = [root / source_path, root / "chapters" / source_path]
        if not any(path.is_file() for path in candidates):
            problems.append(f"{claim_id}: referenced source file not found: {source_file}")

        if "同上" not in source and not URL_RE.search(source):
            problems.append(f"{claim_id}: no URL or explicit same-as-above marker")

        verified = dt.date.fromisoformat(verified_text)
        age = (today - verified).days
        if age < 0:
            warnings.append(f"{claim_id}: verification date is in the future ({verified})")
        elif age > args.max_age_days:
            warnings.append(f"{claim_id}: last verified {age} days ago ({verified})")

    return report(root, problems, warnings, len(rows))


def report(root: Path, problems: list[str], warnings: list[str], claims: int) -> int:
    print(f"Handbook root: {root}")
    print(f"Claims parsed: {claims}")
    for item in warnings:
        print(f"WARNING: {item}")
    for item in problems:
        print(f"ERROR: {item}")
    if problems:
        print(f"FAILED: {len(problems)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASSED: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
