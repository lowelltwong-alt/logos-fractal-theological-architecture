#!/usr/bin/env bash
set -uo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_TS="$(date -u +"%Y%m%dT%H%M%SZ")"
LOG_DIR="${ROOT_DIR}/logs/overnight"
CHECKPOINT_DIR="${LOG_DIR}/checkpoints"
REPORT_DIR="${ROOT_DIR}/reports"
LOG_FILE="${LOG_DIR}/overnight_maintenance_${RUN_TS}.log"
SUMMARY_FILE="${REPORT_DIR}/overnight_maintenance_summary_${RUN_TS}.md"
DRY_RUN=0
STRICT_MODE=0
FORCE_RERUN=0

STAGES=(
  "metadata_lint_and_normalization"
  "cross_reference_validation"
  "link_validation"
  "report_generation"
)

usage() {
  cat <<USAGE
Usage: scripts/overnight_maintenance.sh [options]

Runs staged maintenance with resumable checkpoints.

Options:
  --dry-run                 Preview normalization without writing files.
  --strict                  Fail run on warnings.
  --force                   Re-run stages even if checkpoint exists.
  --checkpoint-dir <path>   Override checkpoint directory.
  --log-dir <path>          Override log output directory.
  --report-dir <path>       Override report output directory.
  -h, --help                Show this help message.
USAGE
}

while (($# > 0)); do
  case "$1" in
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --strict)
      STRICT_MODE=1
      shift
      ;;
    --force)
      FORCE_RERUN=1
      shift
      ;;
    --checkpoint-dir)
      CHECKPOINT_DIR="$2"
      shift 2
      ;;
    --log-dir)
      LOG_DIR="$2"
      shift 2
      ;;
    --report-dir)
      REPORT_DIR="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      usage
      exit 2
      ;;
  esac
done

mkdir -p "$LOG_DIR" "$CHECKPOINT_DIR" "$REPORT_DIR"
LOG_FILE="${LOG_DIR}/overnight_maintenance_${RUN_TS}.log"
SUMMARY_FILE="${REPORT_DIR}/overnight_maintenance_summary_${RUN_TS}.md"

WARNINGS=0
ERRORS=0
COMPLETED_STAGES=()
SKIPPED_STAGES=()

log() {
  local level="$1"
  shift
  local msg="$*"
  local ts
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  printf '[%s] [%s] %s\n' "$ts" "$level" "$msg" | tee -a "$LOG_FILE"
}

checkpoint_file() {
  local stage="$1"
  printf '%s/%s.done' "$CHECKPOINT_DIR" "$stage"
}

mark_stage_done() {
  local stage="$1"
  local file
  file="$(checkpoint_file "$stage")"
  cat > "$file" <<MARK
stage: $stage
completed_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
run_timestamp: $RUN_TS
strict_mode: $STRICT_MODE
dry_run: $DRY_RUN
MARK
}

run_cmd() {
  local desc="$1"
  shift
  log INFO "Running: ${desc}"
  if "$@" >>"$LOG_FILE" 2>&1; then
    log INFO "Completed: ${desc}"
    return 0
  fi
  log ERROR "Failed: ${desc}"
  return 1
}

handle_check_failure() {
  local message="$1"
  if [[ $STRICT_MODE -eq 1 ]]; then
    log ERROR "${message}"
    ERRORS=$((ERRORS + 1))
    return 1
  fi
  log WARN "${message} (continuing because strict mode is off)"
  WARNINGS=$((WARNINGS + 1))
  return 0
}

run_stage() {
  local stage="$1"
  shift
  local ckpt
  ckpt="$(checkpoint_file "$stage")"

  if [[ $FORCE_RERUN -eq 0 && -f "$ckpt" ]]; then
    log INFO "Skipping ${stage}; checkpoint present at ${ckpt}"
    SKIPPED_STAGES+=("$stage")
    return 0
  fi

  log INFO "Starting stage: ${stage}"
  if "$@"; then
    mark_stage_done "$stage"
    COMPLETED_STAGES+=("$stage")
    log INFO "Stage completed: ${stage}"
    return 0
  fi

  log ERROR "Stage failed: ${stage}"
  return 1
}

stage_metadata_lint_and_normalization() {
  local changed_count

  if ! run_cmd "Validate node frontmatter" python3 "$ROOT_DIR/scripts/validate_node_frontmatter.py"; then
    if ! handle_check_failure "Node frontmatter validation failed"; then
      return 1
    fi
  fi

  if ! run_cmd "Validate claim files" python3 "$ROOT_DIR/scripts/validate_claim_files.py"; then
    if ! handle_check_failure "Claim file validation failed"; then
      return 1
    fi
  fi

  log INFO "Normalizing trailing whitespace and EOF newlines for tracked markdown/yaml/json files"
  changed_count="$({
    python3 - "$ROOT_DIR" "$DRY_RUN" <<'PY'
from __future__ import annotations
import pathlib
import subprocess
import sys

root = pathlib.Path(sys.argv[1])
dry_run = sys.argv[2] == "1"

proc = subprocess.run(
    ["git", "-C", str(root), "ls-files", "*.md", "*.yaml", "*.yml", "*.json"],
    check=True,
    capture_output=True,
    text=True,
)

changed = []
for rel in proc.stdout.splitlines():
    if not rel:
        continue
    path = root / rel
    text = path.read_text(encoding="utf-8")
    normalized = "\n".join(line.rstrip() for line in text.splitlines())
    if text.endswith("\n"):
        normalized += "\n"
    elif normalized:
        normalized += "\n"
    if normalized != text:
        changed.append(rel)
        if not dry_run:
            path.write_text(normalized, encoding="utf-8")

for rel in changed:
    print(rel)
print(f"__CHANGED_COUNT__={len(changed)}")
PY
  } | tee -a "$LOG_FILE" | awk -F= '/__CHANGED_COUNT__=/{print $2}' | tail -n 1)"

  changed_count="${changed_count:-0}"
  if [[ "$changed_count" -gt 0 ]]; then
    if [[ $DRY_RUN -eq 1 ]]; then
      log WARN "Dry-run: ${changed_count} files would be normalized"
    else
      log WARN "Normalized ${changed_count} files"
    fi
    WARNINGS=$((WARNINGS + 1))
  else
    log INFO "No normalization changes needed"
  fi

  return 0
}

stage_cross_reference_validation() {
  if ! run_cmd "Validate cross references" python3 "$ROOT_DIR/scripts/validate_cross_references.py"; then
    handle_check_failure "Cross-reference validation failed"
    return $?
  fi
  return 0
}

stage_link_validation() {
  local broken_count

  broken_count="$({
    python3 - "$ROOT_DIR" <<'PY'
from __future__ import annotations
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])
link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

skip_prefixes = ("http://", "https://", "mailto:", "#")
broken = []

for path in root.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for match in link_pattern.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(skip_prefixes):
            continue
        target_path = target.split("#", 1)[0]
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(root)
        except ValueError:
            broken.append((path.relative_to(root).as_posix(), target))
            continue
        if not resolved.exists():
            broken.append((path.relative_to(root).as_posix(), target))

for rel, target in broken:
    print(f"BROKEN {rel}: {target}")
print(f"__BROKEN_COUNT__={len(broken)}")
PY
  } | tee -a "$LOG_FILE" | awk -F= '/__BROKEN_COUNT__=/{print $2}' | tail -n 1)"

  broken_count="${broken_count:-0}"
  if [[ "$broken_count" -gt 0 ]]; then
    if ! handle_check_failure "Found ${broken_count} broken markdown links"; then
      return 1
    fi
    return 0
  fi

  log INFO "No broken markdown links found"
  return 0
}

stage_report_generation() {
  log INFO "Generating summary report at ${SUMMARY_FILE}"
  {
    echo "# Overnight Maintenance Summary"
    echo
    echo "- Run timestamp (UTC): ${RUN_TS}"
    echo "- Dry-run mode: ${DRY_RUN}"
    echo "- Strict mode: ${STRICT_MODE}"
    echo "- Log file: ${LOG_FILE}"
    echo "- Checkpoint directory: ${CHECKPOINT_DIR}"
    echo
    echo "## Stage status"
    for stage in "${STAGES[@]}"; do
      local status="pending"
      if [[ " ${COMPLETED_STAGES[*]} " == *" ${stage} "* ]]; then
        status="completed"
      elif [[ " ${SKIPPED_STAGES[*]} " == *" ${stage} "* ]]; then
        status="skipped (checkpoint)"
      fi
      echo "- ${stage}: ${status}"
    done
    echo
    echo "## Warnings"
    echo "- Total warnings: ${WARNINGS}"
    echo
    echo "## Errors"
    echo "- Total errors: ${ERRORS}"
  } > "$SUMMARY_FILE"

  return 0
}

log INFO "Overnight maintenance run started"
log INFO "Root: ${ROOT_DIR}"
log INFO "Log file: ${LOG_FILE}"
log INFO "Checkpoint dir: ${CHECKPOINT_DIR}"
log INFO "Report file: ${SUMMARY_FILE}"
log INFO "Modes: dry_run=${DRY_RUN}, strict=${STRICT_MODE}, force=${FORCE_RERUN}"

if ! run_stage "metadata_lint_and_normalization" stage_metadata_lint_and_normalization; then
  exit 1
fi
if ! run_stage "cross_reference_validation" stage_cross_reference_validation; then
  exit 1
fi
if ! run_stage "link_validation" stage_link_validation; then
  exit 1
fi
if ! run_stage "report_generation" stage_report_generation; then
  exit 1
fi

if [[ $STRICT_MODE -eq 1 && $WARNINGS -gt 0 ]]; then
  log ERROR "Strict mode enabled and warnings detected (${WARNINGS})"
  exit 1
fi

if [[ $ERRORS -gt 0 ]]; then
  log ERROR "Run completed with ${ERRORS} errors"
  exit 1
fi

log INFO "Overnight maintenance run completed successfully"
exit 0
