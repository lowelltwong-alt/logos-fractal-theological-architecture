#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
NORMALIZED_DIR = ROOT / "data/ai-output/quarantine/normalized"
SUGGESTIONS_DIR = ROOT / "data/ai-output/quarantine/suggestions"


def tokenize(value: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", value.lower()) if len(t) > 2}


def load_candidate_targets() -> list[str]:
    concepts = []
    for p in sorted((ROOT / "data/graph/concepts").glob("concept.*.json")):
        stem = p.stem
        concepts.append(stem.replace("concept.", "concept."))
    return concepts


def main() -> int:
    SUGGESTIONS_DIR.mkdir(parents=True, exist_ok=True)
    targets = load_candidate_targets()
    target_tokens = {t: tokenize(t) for t in targets}

    files = 0
    for path in sorted(NORMALIZED_DIR.glob("*.json")):
        proposal = json.loads(path.read_text(encoding="utf-8"))
        anchor = str(proposal.get("draft_anchor") or proposal.get("anchor") or proposal.get("candidate_label") or "")
        anchor_tokens = tokenize(anchor)
        scored = []
        for target, tokens in target_tokens.items():
            overlap = len(anchor_tokens & tokens)
            if overlap > 0:
                scored.append((overlap, target))

        scored.sort(key=lambda x: (-x[0], x[1]))
        suggestions = [
            {
                "target": target,
                "relationship": "related_to",
                "confidence_band": "low" if score == 1 else "medium",
                "overlap_score": score,
            }
            for score, target in scored[:5]
        ]

        out = {
            "proposal_file": path.name,
            "suggestions": suggestions,
            "reviewer_required": True,
            "auto_promotion_allowed": False,
        }
        out_path = SUGGESTIONS_DIR / path.name
        out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        files += 1

    print(f"suggestion_files={files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
