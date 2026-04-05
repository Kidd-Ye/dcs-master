#!/usr/bin/env python3
"""Check whether an installed dcs-master package is complete and optionally repair it."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "AGENTS.md",
    "skill-manifest.json",
    "scripts/install-portable-skill.py",
    "scripts/check-skill-update.py",
    "scripts/upgrade-from-github.py",
    "references/intent-routing.md",
    "references/rich-answering.md",
    "references/getting-started.md",
    "references/milestone-checklists.md",
    "references/response-templates.md",
    "references/release-and-quality.md",
    "references/troubleshooting.md",
    "references/knowledge-map.md",
    "references/conversation-examples.md",
    "references/platform-basics.md",
    "references/doc-index.md",
    "references/coach-playbooks.md",
]

REQUIRED_DIRS = [
    "references/docs/zh",
    "references/docs/en",
    "state",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check whether an installed dcs-master package is complete."
    )
    parser.add_argument(
        "--repair",
        action="store_true",
        help="If the installation is incomplete and the layout is recognized, run the upgrade script automatically.",
    )
    return parser.parse_args()


def manifest_version() -> str:
    path = ROOT / "skill-manifest.json"
    if not path.exists():
        return "unknown"
    for line in path.read_text(encoding="utf-8").splitlines():
        if '"version"' in line:
            return line.split(":", 1)[1].strip().strip('",')
    return "unknown"


def detect_layout() -> tuple[str | None, str | None, str | None]:
    root_str = str(ROOT)

    if root_str.endswith("/.codex/skills/dcs-master"):
        return ("codex", str(ROOT.parent), None)

    if root_str.endswith("/.qoderwork/skills/dcs-master"):
        return ("qoderwork", str(ROOT.parent), None)

    if "/.opencode/skills/dcs-master" in root_str:
        return ("opencode", str(ROOT.parents[2]), "project")

    if ROOT.name == ".dcs-master":
        return ("universal", str(ROOT.parent), None)

    return (None, None, None)


def find_missing() -> list[str]:
    missing: list[str] = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            missing.append(rel)

    for rel in REQUIRED_DIRS:
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        if rel.endswith("/zh") or rel.endswith("/en"):
            count = len(list(path.glob("*.md")))
            if count < 10:
                missing.append(f"{rel} (too few docs: {count})")

    return missing


def build_repair_command(vendor: str | None, dest: str | None, scope: str | None) -> list[str] | None:
    if not vendor or not dest:
        return None

    script = ROOT / "scripts" / "upgrade-from-github.py"
    cmd = [sys.executable, str(script), vendor, "--to", dest]
    if vendor == "opencode" and scope:
        cmd.extend(["--scope", scope])
    return cmd


def main() -> int:
    args = parse_args()
    version = manifest_version()
    vendor, dest, scope = detect_layout()
    missing = find_missing()

    print(f"ROOT={ROOT}")
    print(f"VERSION={version}")
    print(f"LAYOUT={vendor or 'unknown'}")

    if not missing:
        print("STATUS=healthy")
        return 0

    print("STATUS=incomplete")
    print("MISSING:")
    for item in missing:
        print(f"- {item}")

    repair_cmd = build_repair_command(vendor, dest, scope)
    if repair_cmd:
        print("REPAIR_COMMAND=" + " ".join(repair_cmd))
    else:
        print("REPAIR_COMMAND=unavailable")

    if args.repair and repair_cmd:
        print("ACTION=repair")
        return subprocess.run(repair_cmd).returncode

    if args.repair and not repair_cmd:
        print("ACTION=repair-unavailable")
        return 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
