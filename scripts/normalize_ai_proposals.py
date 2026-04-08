#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROPOSALS_DIR = ROOT / "data/ai-output/quarantine/proposals"
NORMALIZED_DIR = ROOT / "data/ai-output/quarantine/normalized"


def main() -> int:
    NORMALIZED_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in sorted(PROPOSALS_DIR.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload.setdefault("promotion_status", "quarantined")
        payload.setdefault("reviewer_required", True)
        payload.setdefault("auto_promotion_allowed", False)
        out_path = NORMALIZED_DIR / path.name
        out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        count += 1

    print(f"normalized_proposals={count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
