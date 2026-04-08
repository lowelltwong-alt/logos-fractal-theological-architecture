#!/usr/bin/env bash
set -euo pipefail

python3 scripts/validate_node_frontmatter.py
python3 scripts/validate_cross_references.py
python3 scripts/validate_claim_files.py
python3 scripts/validate_internal_links.py
python3 scripts/semantic_merge_pipeline.py
