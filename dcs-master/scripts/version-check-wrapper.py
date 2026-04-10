#!/usr/bin/env python3
"""Version check wrapper for dcs-master skill.

This script checks for updates and returns a formatted message if an update is available.
It is designed to be called at the start of each skill session.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def check_version() -> str | None:
    """Check if a newer version is available and return update message."""
    script_dir = Path(__file__).resolve().parent
    check_script = script_dir / "check-skill-update.py"
    
    if not check_script.exists():
        return None
    
    try:
        result = subprocess.run(
            [sys.executable, str(check_script)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        output = result.stdout.strip()
        
        # Parse the output
        status = None
        local_version = None
        remote_version = None
        
        for line in output.split("\n"):
            if "=" in line:
                key, value = line.split("=", 1)
                if key == "STATUS":
                    status = value
                elif key == "LOCAL_VERSION":
                    local_version = value
                elif key == "REMOTE_VERSION":
                    remote_version = value
        
        if status == "update-available" and local_version and remote_version:
            return (
                f"📦 **发现新版本**: dcs-master {local_version} → {remote_version}\n"
                f"   升级命令: `python3 {script_dir}/upgrade-from-github.py qoderwork --to ~/.qoderwork/skills`"
            )
        
    except (subprocess.TimeoutExpired, Exception):
        pass
    
    return None


if __name__ == "__main__":
    message = check_version()
    if message:
        print(message)
