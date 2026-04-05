#!/usr/bin/env python3
"""Check whether a newer version of this skill is available on GitHub."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import urllib.error
import urllib.request


DEFAULT_TIMEOUT = 15.0


def parse_args() -> argparse.Namespace:
    default_manifest = Path(__file__).resolve().parent.parent / "skill-manifest.json"
    parser = argparse.ArgumentParser(
        description="Check whether a newer skill version exists on GitHub."
    )
    parser.add_argument(
        "--manifest",
        default=str(default_manifest),
        help="Path to local skill-manifest.json",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help="HTTP timeout in seconds",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def emit(key: str, value: str) -> None:
    print(f"{key}={value}")


def normalize_version(version: str) -> tuple[int, int, int] | None:
    parts = version.strip().split(".")
    if not parts:
        return None
    values: list[int] = []
    for part in parts:
        if not part.isdigit():
            return None
        values.append(int(part))
    while len(values) < 3:
        values.append(0)
    return tuple(values[:3])


def resolve_remote_manifest_url(manifest: dict) -> str | None:
    source = manifest.get("source", {})
    raw_manifest_url = str(source.get("raw_manifest_url", "")).strip()
    if raw_manifest_url:
        return raw_manifest_url

    repo = str(source.get("repo", "")).strip()
    if not repo:
        return None

    ref = str(source.get("ref", "")).strip() or "main"
    manifest_path = str(source.get("manifest_path", "")).strip()
    if not manifest_path:
        base_path = str(source.get("path", "")).strip().strip("/")
        manifest_path = (
            f"{base_path}/skill-manifest.json" if base_path else "skill-manifest.json"
        )

    manifest_path = manifest_path.lstrip("/")
    return f"https://raw.githubusercontent.com/{repo}/{ref}/{manifest_path}"


def fetch_json(url: str, timeout: float) -> dict:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "codex-skill-update-checker"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = response.read().decode("utf-8")
    return json.loads(payload)


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest).expanduser().resolve()

    try:
        local_manifest = load_json(manifest_path)
    except FileNotFoundError:
        emit("STATUS", "invalid-manifest")
        emit("REASON", f"missing-file:{manifest_path}")
        return 1
    except json.JSONDecodeError as exc:
        emit("STATUS", "invalid-manifest")
        emit("REASON", f"json-error:{exc.msg}")
        return 1

    local_version = str(local_manifest.get("version", "")).strip()
    if not local_version:
        emit("STATUS", "invalid-manifest")
        emit("REASON", "missing-version")
        return 1

    remote_url = resolve_remote_manifest_url(local_manifest)
    if not remote_url:
        emit("STATUS", "skipped")
        emit("REASON", "missing-source-repo")
        emit("LOCAL_VERSION", local_version)
        return 0

    emit("LOCAL_VERSION", local_version)
    emit("REMOTE_MANIFEST_URL", remote_url)

    try:
        remote_manifest = fetch_json(remote_url, args.timeout)
    except urllib.error.HTTPError as exc:
        emit("STATUS", "check-failed")
        emit("REASON", f"http-{exc.code}")
        return 0
    except urllib.error.URLError as exc:
        emit("STATUS", "check-failed")
        emit("REASON", f"url-error:{exc.reason}")
        return 0
    except TimeoutError:
        emit("STATUS", "check-failed")
        emit("REASON", "timeout")
        return 0
    except json.JSONDecodeError:
        emit("STATUS", "check-failed")
        emit("REASON", "remote-json-invalid")
        return 0

    remote_version = str(remote_manifest.get("version", "")).strip()
    if not remote_version:
        emit("STATUS", "check-failed")
        emit("REASON", "remote-version-missing")
        return 0

    emit("REMOTE_VERSION", remote_version)

    repo = str(local_manifest.get("source", {}).get("repo", "")).strip()
    if repo:
        emit("REPO", repo)

    update_hint = str(local_manifest.get("update", {}).get("install_command", "")).strip()
    if update_hint:
        emit("UPDATE_HINT", update_hint)

    notes_url = str(local_manifest.get("update", {}).get("notes_url", "")).strip()
    if notes_url:
        emit("NOTES_URL", notes_url)

    local_norm = normalize_version(local_version)
    remote_norm = normalize_version(remote_version)

    if local_norm and remote_norm:
        if remote_norm > local_norm:
            emit("STATUS", "update-available")
            return 0
        if remote_norm == local_norm:
            emit("STATUS", "up-to-date")
            return 0
        emit("STATUS", "local-ahead")
        return 0

    if remote_version == local_version:
        emit("STATUS", "up-to-date")
        return 0

    emit("STATUS", "version-diff")
    return 0


if __name__ == "__main__":
    sys.exit(main())
