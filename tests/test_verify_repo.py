# ABOUTME: Pytest wrapper that fails when the repo verification script reports any failure.
# ABOUTME: CI runs this; the script in scripts/verify_repo.py is the source of truth.

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "verify_repo.py"


def test_repo_verification_passes():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    assert result.returncode == 0, (
        f"verify_repo.py exited {result.returncode}\n"
        f"--- stdout ---\n{result.stdout}\n"
        f"--- stderr ---\n{result.stderr}"
    )
