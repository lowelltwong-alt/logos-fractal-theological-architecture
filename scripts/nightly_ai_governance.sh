#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

echo "[nightly-ai] step 1/4: lint"
bash scripts/run_validations.sh

echo "[nightly-ai] step 2/4: normalize proposals"
python3 scripts/normalize_ai_proposals.py

echo "[nightly-ai] step 3/4: suggest links"
python3 scripts/suggest_ai_links.py

echo "[nightly-ai] step 4/4: produce review queue"
python3 scripts/build_ai_review_queue.py

echo "[nightly-ai] completed with no auto-promotion"
