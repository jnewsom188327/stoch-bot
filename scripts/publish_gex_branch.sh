#!/usr/bin/env bash
# Commit one GEX snapshot onto the gex-data branch and push that branch.
# Never checks out a push of main. A rejected push is retried against the
# latest gex-data tip so two overlapping runs do not drop each other's rows.
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: publish_gex_branch.sh LAST_RUN_JSON" >&2
  exit 2
fi
JSON=$1
if [ ! -s "$JSON" ]; then
  echo "snapshot file missing: $JSON" >&2
  exit 2
fi

LOGGER=${GEX_LOGGER_PY:-/tmp/gex_logger.py}
PY=${GEX_PYTHON:-python3}
SLEEP_SECS=${GEX_PUSH_RETRY_SLEEP-}
export GIT_TERMINAL_PROMPT=0

cd "$(git rev-parse --show-toplevel)"
START_SHA=$(git rev-parse HEAD)
git config user.name "gex-logger"
git config user.email "gex-logger@users.noreply.github.com"

publish_once() {
  local base
  # The leading + updates only this remote-tracking ref. A shallow fetch
  # cannot always prove a fast-forward, and the push below is never forced.
  if git fetch --depth=1 origin "+gex-data:refs/remotes/origin/gex-data"; then
    base=refs/remotes/origin/gex-data
  else
    base=$START_SHA
  fi
  # Reset only the gex-data branch. START_SHA is the workflow commit (main).
  git checkout -f -B gex-data "$base"
  local branch
  branch=$(git rev-parse --abbrev-ref HEAD)
  if [ "$branch" != "gex-data" ]; then
    echo "refusing to commit on ${branch}" >&2
    return 1
  fi
  "$PY" "$LOGGER" --publish "$JSON" --out results/gex
  git add -- results/gex/gex_levels.csv results/gex/GEX_LATEST.md results/gex/GEX_PINE_SNIPPET.txt
  shopt -s nullglob
  local gz=(results/gex/gex_strikes_*.csv.gz)
  if [ ${#gz[@]} -gt 0 ]; then
    git add -- "${gz[@]}"
  fi
  shopt -u nullglob
  if git diff --cached --quiet; then
    echo "GEX files already contain this snapshot."
    return 0
  fi
  git commit -m "gex snapshot $(date -u +%Y-%m-%dT%H:%MZ)"
  git push origin gex-data
}

attempt=1
while [ "$attempt" -le 5 ]; do
  if publish_once; then
    exit 0
  fi
  echo "publish attempt ${attempt} failed; retrying" >&2
  if [ -n "${SLEEP_SECS}" ]; then
    sleep "$SLEEP_SECS"
  else
    sleep $((attempt * 3))
  fi
  attempt=$((attempt + 1))
done
echo "could not push gex-data" >&2
exit 1
