#!/usr/bin/env bash
set -euo pipefail

# Usage: ./merge_pr.sh <pr-number> [repo] [mode]
# mode: squash (default) or merge
PR_NUMBER=${1:-134}
REPO=${2:-coinbase/coinbase-advanced-py}
MODE=${3:-squash}

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI is required. Install and authenticate first (gh auth login)."
  exit 2
fi

echo "Checking gh auth..."
if ! gh auth status >/dev/null 2>&1; then
  echo "Not authenticated with GitHub CLI. Run: gh auth login" >&2
  exit 3
fi

echo "Merging PR #${PR_NUMBER} on ${REPO} (mode=${MODE})"
if [ "${MODE}" = "squash" ]; then
  gh pr merge "${PR_NUMBER}" --repo "${REPO}" --squash --delete-branch -m "Merge repo summarizer skill: CI, docs, and subagent metadata"
else
  gh pr merge "${PR_NUMBER}" --repo "${REPO}" --merge -m "Merge repo summarizer skill: CI, docs, and subagent metadata"
fi

echo "Done."
