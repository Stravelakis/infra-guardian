#!/usr/bin/env python3
"""infra-guardian: doctor — checks the skill's own health.

Verifies: config present + readable, scripts present + executable,
backup dir writable, timer status, Telegram (optional).
Prints a plain-English pass/fix report. Changes nothing.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG = REPO / "guardian.config.yaml"
SCRIPTS = ["backup.py", "setup.py", "infra-status-check.py", "doctor.py"]

OK = "PASS"
WARN = "WARN"
BAD = "FIX "


def line(status, what, detail=""):
    print(f"[{status}] {what}" + (f" — {detail}" if detail else ""))


def check_config():
    if not CONFIG.exists():
        line(BAD, "Config file", "guardian.config.yaml missing. Run setup.py.")
        return
    try:
        text = CONFIG.read_text()
        if "mode" in text:
            line(OK, "Config file", "found and readable")
        else:
            line(WARN, "Config file", "found but has no 'mode' — re-run setup.py")
    except Exception as e:
        line(BAD, "Config file", f"unreadable ({e})")


def check_scripts():
    for name in SCRIPTS:
        p = REPO / "scripts" / name
        if not p.exists():
            line(WARN, f"Script {name}", "not created yet")
        elif os.access(p, os.X_OK):
            line(OK, f"Script {name}", "present and executable")
        else:
            line(WARN, f"Script {name}",
                 f"present but not executable — run: chmod +x scripts/{name}")


def check_backup_dir():
    d = REPO / "backups"
    try:
        d.mkdir(exist_ok=True)
        test = d / ".write-test"
        test.write_text("ok")
        test.unlink()
        line(OK, "Backups folder", "exists and is writable")
    except Exception as e:
        line(BAD, "Backups folder", f"cannot write ({e})")


def check_timer():
    if not shutil.which("systemctl"):
        line(WARN, "Self-check timer", "systemctl not found (fine off-Ubuntu)")
        return
    try:
        r = subprocess.run(
            ["systemctl", "--user", "is-enabled", "infra-status-check.timer"],
            capture_output=True, text=True, timeout=10)
        state = r.stdout.strip() or r.stderr.strip()
        if state == "enabled":
            line(OK, "Self-check timer", "enabled")
        else:
            line(WARN, "Self-check timer", f"{state} — enable it to get self-checks")
    except Exception as e:
        line(WARN, "Self-check timer", f"could not check ({e})")


def check_telegram():
    dotenv = REPO / ".env"
    token = ""
    if dotenv.exists():
        for l in dotenv.read_text().splitlines():
            if l.startswith("TELEGRAM_BOT_TOKEN="):
                token = l.split("=", 1)[1].strip()
    if token and "12345678" not in token:
        line(OK, "Telegram (optional)", "configured")
    else:
        line(WARN, "Telegram (optional)", "not set up — self-checks print/save instead")


def main():
    print("infra-guardian doctor")
    print("In plain English: I'm checking that the guardian itself is healthy.\n")
    check_config()
    check_scripts()
    check_backup_dir()
    check_timer()
    check_telegram()
    print("\nDone. [FIX] = needs action. [WARN] = optional/not blocking. "
          "[PASS] = good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
