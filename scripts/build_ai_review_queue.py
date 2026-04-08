#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
NORMALIZED_DIR = ROOT / "data/ai-output/quarantine/normalized"
SUGGESTIONS_DIR = ROOT / "data/ai-output/quarantine/suggestions"
REPORT_DIR = ROOT / "reports/ai-review-queue"

REVIEW_FIELDS = [
    "reviewer_id",
    "reviewed_at_utc",
    "review_decision",
    "review_rationale",
    "promotion_target_trust_zone",
]


def main() -> int:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_path = REPORT_DIR / f"review_queue_{timestamp}.md"

    lines = [
        "# AI Review Queue",
        "",
        f"- Generated at (UTC): {timestamp}",
        "- Auto-promotion: disabled",
        "",
        "## Mandatory reviewer fields",
    ]
    lines.extend([f"- `{field}`" for field in REVIEW_FIELDS])
    lines.append("")
    lines.append("## Queue items")

    count = 0
    for proposal_path in sorted(NORMALIZED_DIR.glob("*.json")):
        proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
        suggestion_path = SUGGESTIONS_DIR / proposal_path.name
        suggestion_count = 0
        if suggestion_path.exists():
            suggestion = json.loads(suggestion_path.read_text(encoding="utf-8"))
            suggestion_count = len(suggestion.get("suggestions", []))

        lines.append(f"### {proposal_path.name}")
        lines.append(f"- Candidate label: {proposal.get('candidate_label', 'n/a')}")
        lines.append(f"- Draft anchor: {proposal.get('draft_anchor', proposal.get('anchor', 'n/a'))}")
        lines.append(f"- Link suggestions: {suggestion_count}")
        lines.append("- Reviewer fields:")
        for field in REVIEW_FIELDS:
            lines.append(f"  - {field}: <required>")
        lines.append("")
        count += 1

    lines.append(f"Total queued items: {count}")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(str(report_path.relative_to(ROOT)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
