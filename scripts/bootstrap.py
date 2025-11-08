#!/usr/bin/env python3
"""Project bootstrapper that renames the template package and resets git history."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path

OLD_PACKAGE = "python_boilerplate"
OLD_DIST = "patch-inspector"
SKIP_DIRS = {".git", ".venv", ".uv-cache", "__pycache__"}
IDENTIFIER_RE = re.compile(r"^[A-Za-z_]\w*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rename the template package and reset repository history."
    )
    parser.add_argument(
        "new_project_name",
        help="New package name (must be a valid Python identifier).",
    )
    return parser.parse_args()


def validate_new_name(new_name: str) -> None:
    if not IDENTIFIER_RE.match(new_name):
        raise SystemExit(
            "ERROR: new_project_name must be a valid Python identifier "
            "(letters, numbers, underscores)."
        )
    if new_name == OLD_PACKAGE:
        raise SystemExit(
            f"ERROR: new_project_name must be different from the template package ({OLD_PACKAGE})."
        )


def rename_package(root: Path, new_package: str) -> None:
    src_dir = root / "src" / OLD_PACKAGE
    if not src_dir.is_dir():
        raise SystemExit(f"ERROR: Expected {src_dir} but it does not exist.")

    dest_dir = root / "src" / new_package
    if dest_dir.exists():
        raise SystemExit(
            f"ERROR: Destination {dest_dir} already exists. Choose a different project name."
        )

    src_dir.rename(dest_dir)


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def replace_identifiers(root: Path, new_package: str) -> None:
    new_dist = new_package.replace("_", "-")
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if should_skip(relative):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = content.replace(OLD_PACKAGE, new_package).replace(OLD_DIST, new_dist)
        if updated != content:
            path.write_text(updated, encoding="utf-8")


def reset_git_repo(root: Path) -> None:
    git_dir = root / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)

    try:
        subprocess.run(
            ["git", "init", "-b", "main"],
            cwd=root,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        subprocess.run(
            ["git", "init"],
            cwd=root,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        subprocess.run(
            ["git", "branch", "-M", "main"],
            cwd=root,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def main() -> int:
    args = parse_args()
    new_package = args.new_project_name
    validate_new_name(new_package)

    root = Path(__file__).resolve().parent.parent
    print(f"Preparing new project: {new_package}")

    rename_package(root, new_package)
    replace_identifiers(root, new_package)
    reset_git_repo(root)

    print(f"Project successfully renamed to {new_package}.")
    print("Next steps: uv sync && git add .")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
