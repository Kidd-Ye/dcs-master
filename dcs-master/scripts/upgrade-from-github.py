#!/usr/bin/env python3
"""Download the latest dcs-master from GitHub and upgrade an existing installation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import urllib.request
import zipfile


DEFAULT_MANIFEST = {
    "source": {
        "repo": "Kidd-Ye/dcs-master",
        "ref": "main",
        "path": "dcs-master",
    }
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upgrade an installed dcs-master package from GitHub."
    )
    parser.add_argument(
        "vendor",
        choices=["codex", "qoderwork", "skilldir", "opencode", "claude", "cursor", "copilot", "gemini", "universal"],
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
        help="Used by OpenCode only. 'project' upgrades .opencode/skills, 'global' upgrades <dest>/skills.",
    )
    parser.add_argument(
        "--manifest",
        default=str(Path(__file__).resolve().parent.parent / "skill-manifest.json"),
        help="Path to local skill-manifest.json",
    )
    return parser.parse_args()


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return DEFAULT_MANIFEST
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_zip_url(manifest: dict) -> tuple[str, str]:
    source = manifest.get("source", {})
    repo = str(source.get("repo", "")).strip()
    ref = str(source.get("ref", "")).strip() or "main"
    if not repo:
        raise SystemExit("Manifest missing source.repo")
    return (f"https://codeload.github.com/{repo}/zip/{ref}", ref)


def safe_extract(zip_path: Path, dest_dir: Path) -> Path:
    with zipfile.ZipFile(zip_path, "r") as archive:
        top_levels = {name.split("/")[0] for name in archive.namelist() if name}
        archive.extractall(dest_dir)
    if len(top_levels) != 1:
        raise SystemExit("Unexpected GitHub archive layout.")
    return dest_dir / next(iter(top_levels))


def run_install(installer: Path, vendor: str, to: str, scope: str) -> int:
    cmd = [sys.executable, str(installer), vendor, "--to", to, "--force"]
    if vendor == "opencode":
        cmd.extend(["--scope", scope])
    result = subprocess.run(cmd)
    return result.returncode


def main() -> int:
    args = parse_args()
    manifest = load_manifest(Path(args.manifest).expanduser().resolve())
    zip_url, ref = resolve_zip_url(manifest)
    skill_path = str(manifest.get("source", {}).get("path", "")).strip().strip("/")
    if not skill_path:
        raise SystemExit("Manifest missing source.path")

    with tempfile.TemporaryDirectory(prefix="dcs-master-upgrade-") as tmp:
        tmp_path = Path(tmp)
        zip_path = tmp_path / f"{ref}.zip"
        urllib.request.urlretrieve(zip_url, zip_path)
        repo_root = safe_extract(zip_path, tmp_path)
        install_script = repo_root / skill_path / "scripts" / "install-portable-skill.py"
        if not install_script.exists():
            raise SystemExit("install-portable-skill.py not found in downloaded package.")
        return run_install(install_script, args.vendor, args.to, args.scope)


if __name__ == "__main__":
    raise SystemExit(main())
