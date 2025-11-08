#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: ./scripts/bootstrap.sh new_project_name"
  exit 1
fi

OLD_PACKAGE="python_boilerplate"
OLD_DIST="python-boilerplate"
NEW_PACKAGE="$1"

if [[ ! "$NEW_PACKAGE" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
  echo "ERROR: new_project_name must be a valid Python identifier (letters, numbers, underscores)."
  exit 1
fi

SRC_DIR="src/$OLD_PACKAGE"
if [ ! -d "$SRC_DIR" ]; then
  echo "ERROR: Expected $SRC_DIR but it does not exist."
  exit 1
fi

NEW_DIST=${NEW_PACKAGE//_/-}

echo "Preparing new project: $NEW_PACKAGE"

mv "$SRC_DIR" "src/$NEW_PACKAGE"

export OLD_PACKAGE NEW_PACKAGE OLD_DIST NEW_DIST
python3 <<'PY'
from __future__ import annotations

import os
from pathlib import Path

root = Path(".").resolve()
skip_dirs = {".git", ".venv", ".uv-cache", "__pycache__"}

old_pkg = os.environ["OLD_PACKAGE"]
new_pkg = os.environ["NEW_PACKAGE"]
old_dist = os.environ["OLD_DIST"]
new_dist = os.environ["NEW_DIST"]

def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return bool(parts & skip_dirs)

for path in root.rglob("*"):
    if not path.is_file():
        continue
    if should_skip(path.relative_to(root)):
        continue
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    updated = content.replace(old_pkg, new_pkg).replace(old_dist, new_dist)
    if updated != content:
        path.write_text(updated, encoding="utf-8")
PY

rm -rf .git
if ! git init -b main >/dev/null 2>&1; then
  git init >/dev/null 2>&1
  git branch -M main >/dev/null 2>&1
fi

echo "Project successfully renamed to $NEW_PACKAGE."
echo "Next steps: uv sync && git add ."
