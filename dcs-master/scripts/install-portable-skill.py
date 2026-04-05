#!/usr/bin/env python3
"""Install dcs-master into other AI coding tools."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


SKILL_NAME = "dcs-master"
PROJECT_PACK_DIR = ".dcs-master"
ROOT = Path(__file__).resolve().parent.parent
IGNORE_NAMES = {
    ".DS_Store",
    ".git",
    "__pycache__",
    ".pytest_cache",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install dcs-master into Codex, OpenCode, Claude, Cursor, Copilot, Gemini, or a universal project layout."
    )
    parser.add_argument(
        "vendor",
        choices=[
            "codex",
            "opencode",
            "claude",
            "cursor",
            "copilot",
            "gemini",
            "universal",
        ],
        help="Target tool or project layout.",
    )
    parser.add_argument(
        "--to",
        required=True,
        help="Destination path. For Codex, pass the skill home. For project-scoped vendors, pass the project root.",
    )
    parser.add_argument(
        "--scope",
        choices=["project", "global"],
        default="project",
        help="Used by OpenCode only. 'project' installs into .opencode/skills, 'global' installs into <dest>/skills.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing targets if they already exist.",
    )
    return parser.parse_args()


def fail(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str, force: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        fail(f"Target already exists: {path}")
    path.write_text(content, encoding="utf-8")


def ignore_filter(_src: str, names: list[str]) -> set[str]:
    ignored = set()
    for name in names:
        if name in IGNORE_NAMES:
            ignored.add(name)
    return ignored


def copy_tree(src: Path, dest: Path, force: bool) -> None:
    if dest.exists():
        if not force:
            fail(f"Target already exists: {dest}")
        if dest.is_dir():
            shutil.rmtree(dest)
        else:
            dest.unlink()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src, dest, ignore=ignore_filter)


def adapt_agents_for_project(pack_dir: str) -> str:
    content = read_text(ROOT / "AGENTS.md")
    replacements = {
        "`references/": f"`{pack_dir}/references/",
        "`scripts/": f"`{pack_dir}/scripts/",
        "`state/": f"`{pack_dir}/state/",
    }
    for source, target in replacements.items():
        content = content.replace(source, target)
    return content


def install_codex(dest_root: Path, force: bool) -> list[Path]:
    target = dest_root / SKILL_NAME
    copy_tree(ROOT, target, force)
    return [target]


def install_opencode(dest_root: Path, scope: str, force: bool) -> list[Path]:
    if scope == "project":
        target = dest_root / ".opencode" / "skills" / SKILL_NAME
    else:
        target = dest_root / "skills" / SKILL_NAME
    copy_tree(ROOT, target, force)
    return [target]


def install_project_vendor(vendor: str, project_root: Path, force: bool) -> list[Path]:
    changed: list[Path] = []
    pack_root = project_root / PROJECT_PACK_DIR
    copy_tree(ROOT, pack_root, force)
    changed.append(pack_root)

    agents_content = adapt_agents_for_project(PROJECT_PACK_DIR)
    agents_path = project_root / "AGENTS.md"
    write_text(agents_path, agents_content, force)
    changed.append(agents_path)

    if vendor in {"claude", "universal"}:
        path = project_root / "CLAUDE.md"
        write_text(path, read_text(ROOT / "CLAUDE.md"), force)
        changed.append(path)

    if vendor in {"gemini", "universal"}:
        path = project_root / "GEMINI.md"
        write_text(path, read_text(ROOT / "GEMINI.md"), force)
        changed.append(path)

    if vendor in {"copilot", "universal"}:
        path = project_root / ".github" / "copilot-instructions.md"
        write_text(path, read_text(ROOT / ".github" / "copilot-instructions.md"), force)
        changed.append(path)

    if vendor in {"cursor", "universal"}:
        path = project_root / ".cursor" / "rules" / "dcs-master.mdc"
        write_text(path, read_text(ROOT / ".cursor" / "rules" / "dcs-master.mdc"), force)
        changed.append(path)

    return changed


def main() -> int:
    args = parse_args()
    dest_root = Path(args.to).expanduser().resolve()

    if args.vendor == "codex":
        changed = install_codex(dest_root, args.force)
    elif args.vendor == "opencode":
        changed = install_opencode(dest_root, args.scope, args.force)
    else:
        changed = install_project_vendor(args.vendor, dest_root, args.force)

    print("Installed dcs-master to:")
    for path in changed:
        print(f"- {path}")

    if args.vendor in {"codex", "opencode"}:
        print("Restart the tool to pick up the new skill if needed.")
    else:
        print("Open the target project in the corresponding tool to start using the installed instructions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
