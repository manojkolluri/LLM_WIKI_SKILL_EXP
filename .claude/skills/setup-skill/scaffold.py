"""
scaffold.py — copies the skill's template tree into a target directory, substituting
placeholders (PROJECT_NAME, PROJECT_SUMMARY) along the way.

Usage:
    python scaffold.py <target-dir> --project-name "..." --project-summary "..."

This script is deliberately small — single file, standard library only. It exists so
the skill doesn't have to fan out N create_file calls for every template; one
subprocess invocation handles all of them.

Files with `{{PROJECT_NAME}}` or `{{PROJECT_SUMMARY}}` in their content get
substituted. Other files (.gitkeep, .gitignore, the README's static parts) pass through
untouched.

The script refuses to write to a non-empty target directory unless --force is given.
Better to fail loudly than to silently overwrite an existing project.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path


PLACEHOLDERS = ("{{PROJECT_NAME}}", "{{PROJECT_SUMMARY}}")


def substitute(text: str, project_name: str, project_summary: str) -> str:
    """Replace placeholders in a text blob."""
    return text.replace("{{PROJECT_NAME}}", project_name).replace(
        "{{PROJECT_SUMMARY}}", project_summary
    )


def copy_and_substitute(src_root: Path, dst_root: Path, project_name: str, project_summary: str) -> list[str]:
    """Walk the template tree, copy each file to dst, substituting placeholders in text content."""
    created: list[str] = []

    for src_path in src_root.rglob("*"):
        rel = src_path.relative_to(src_root)
        dst_path = dst_root / rel

        if src_path.is_dir():
            dst_path.mkdir(parents=True, exist_ok=True)
            continue

        dst_path.parent.mkdir(parents=True, exist_ok=True)

        # Read as text and substitute if any placeholder is present; otherwise pass through bytes.
        try:
            raw = src_path.read_text(encoding="utf-8")
            if any(p in raw for p in PLACEHOLDERS):
                dst_path.write_text(
                    substitute(raw, project_name, project_summary), encoding="utf-8"
                )
            else:
                shutil.copyfile(src_path, dst_path)
        except UnicodeDecodeError:
            # Binary file — copy as bytes.
            shutil.copyfile(src_path, dst_path)

        created.append(str(rel))

    return created


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold a new project from the setup skill's template tree."
    )
    parser.add_argument(
        "target",
        help="Directory to scaffold into. Created if missing. Refuses to write to a non-empty dir without --force.",
    )
    parser.add_argument(
        "--project-name",
        required=True,
        help="Name of the project (used in README, CLAUDE.md, Wiki headers).",
    )
    parser.add_argument(
        "--project-summary",
        required=True,
        help="One-sentence summary of the product (used in README, system-overview.md).",
    )
    parser.add_argument(
        "--templates",
        default=None,
        help="Path to the templates folder. Defaults to <script-dir>/templates.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Allow scaffolding into a non-empty target directory (overwrites overlapping files).",
    )

    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    src_root = Path(args.templates) if args.templates else script_dir / "templates"

    if not src_root.is_dir():
        print(f"ERROR: templates folder not found at {src_root}", file=sys.stderr)
        return 2

    dst_root = Path(args.target).resolve()
    if dst_root.exists() and any(dst_root.iterdir()) and not args.force:
        print(
            f"ERROR: target {dst_root} is not empty. Re-run with --force to overwrite.",
            file=sys.stderr,
        )
        return 3

    dst_root.mkdir(parents=True, exist_ok=True)
    created = copy_and_substitute(src_root, dst_root, args.project_name, args.project_summary)

    print(f"Scaffolded {len(created)} files into {dst_root}")
    for path in sorted(created):
        print(f"  + {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
