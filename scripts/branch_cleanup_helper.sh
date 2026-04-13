#!/usr/bin/env bash
set -euo pipefail

# Safe helper for branch cleanup.
# Default behavior is DRY RUN.
# Requires: git
# Optional: gh (for pull request inventory)
# Usage:
#   ./logos_branch_cleanup_helper.sh
#   MODE=apply DELETE_FILE=branches-to-delete.txt ./logos_branch_cleanup_helper.sh
#
# branches-to-delete.txt format:
#   one branch name per line
#   blank lines and lines starting with # are ignored

REMOTE="${REMOTE:-origin}"
MAIN_BRANCH="${MAIN_BRANCH:-main}"
MODE="${MODE:-dry-run}"
DELETE_FILE="${DELETE_FILE:-branches-to-delete.txt}"

printf '\n==> Fetching latest refs from %s\n' "$REMOTE"
git fetch "$REMOTE" --prune --tags

printf '\n==> Safety snapshot reminder\n'
echo "Create a tag before deleting anything:"
echo "  STAMP=\$(date -u +%Y%m%dT%H%M%SZ)"
echo "  git tag -a pre-cleanup-\$STAMP -m 'Snapshot before branch cleanup'"
echo "  git push $REMOTE pre-cleanup-\$STAMP"

printf '\n==> Open pull requests (requires gh)\n'
if command -v gh >/dev/null 2>&1; then
  gh pr list --state open --limit 100 \
    --json number,title,headRefName,baseRefName,isDraft,url \
    --jq '.[] | "#\(.number) | \(.headRefName) -> \(.baseRefName) | draft=\(.isDraft) | \(.title) | \(.url)"'
else
  echo "gh not installed; skipping PR inventory"
fi

printf '\n==> Remote branches merged into %s/%s\n' "$REMOTE" "$MAIN_BRANCH"
git branch -r --merged "$REMOTE/$MAIN_BRANCH" \
  | sed 's#^[* ]*##' \
  | grep "^$REMOTE/" \
  | sed "s#^$REMOTE/##" \
  | grep -v "^$MAIN_BRANCH$" \
  | sort -u || true

printf '\n==> Remote branches NOT merged into %s/%s\n' "$REMOTE" "$MAIN_BRANCH"
git branch -r --no-merged "$REMOTE/$MAIN_BRANCH" \
  | sed 's#^[* ]*##' \
  | grep "^$REMOTE/" \
  | sed "s#^$REMOTE/##" \
  | grep -v "^$MAIN_BRANCH$" \
  | sort -u || true

if [[ ! -f "$DELETE_FILE" ]]; then
  printf '\n==> No %s file found. Create one when you are ready to delete branches.\n' "$DELETE_FILE"
  exit 0
fi

printf '\n==> Planned deletions from %s\n' "$DELETE_FILE"
while IFS= read -r branch; do
  [[ -z "$branch" ]] && continue
  [[ "$branch" =~ ^# ]] && continue
  if [[ "$MODE" == "apply" ]]; then
    echo "Deleting remote branch: $branch"
    git push "$REMOTE" --delete "$branch"
  else
    echo "[dry-run] git push $REMOTE --delete $branch"
  fi
done < "$DELETE_FILE"

printf '\n==> Done\n'
if [[ "$MODE" != "apply" ]]; then
  echo "No branches were deleted. Re-run with MODE=apply when you are sure."
fi
