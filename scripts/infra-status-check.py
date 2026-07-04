#!/usr/bin/env python3
"""
infra-status-check.py — infra-guardian scheduled self-check.
Reads status.md, detects drift, proposes A/B/C next steps.
Telegram is OPTIONAL: used only if configured, else logs locally.
Run by systemd --user timer. Never acts automatically.
"""

import os
import sys
import datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not installed. Run: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "guardian.config.yaml"
STATUS_PATH = REPO_ROOT / "status.md"
LOG_PATH = REPO_ROOT / "self-check.log"


def load_config():
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f) or {}


def load_env():
    """Minimal .env reader (no external dependency)."""
    env = {}
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip()
    return env


def read_status():
    if not STATUS_PATH.exists():
        return None
    return STATUS_PATH.read_text()


def diagnose(status_text):
    """
    Very light drift check. Returns (summary, options[]).
    Extend the checks here as the ecosystem grows.
    """
    issues = []

    if status_text is None:
        issues.append("No status.md found — the project has no living record yet.")
    else:
        if "TODO" in status_text or "OPEN" in status_text.upper():
            issues.append("Open items still present in status.md.")
        if "Verified?" not in status_text:
            issues.append("Backups table may be missing its 'Verified?' column.")

    if issues:
        summary = "Self-check found things needing attention:\n- " + "\n- ".join(issues)
        options = [
            "A) Review the open items in status.md now.",
            "B) Run a fresh verified backup, then review.",
            "C) Snooze until the next scheduled check (no change).",
        ]
    else:
        summary = "Self-check passed. No drift detected."
        options = [
            "A) Continue as-is (recommended).",
            "B) Run an extra verified backup for peace of mind.",
            "C) Open status.md to review recent history.",
        ]
    return summary, options


def send_telegram(config, env, message):
    """Returns True if sent, False if not configured / failed."""
    tg = config.get("telegram", {}) or {}
    if not tg.get("enabled"):
        return False
    token = env.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = env.get("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id or token.startswith("12345678"):
        return False
    try:
        import urllib.request
        import urllib.parse
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = urllib.parse.urlencode({"chat_id": chat_id, "text": message}).encode()
        urllib.request.urlopen(url, data=data, timeout=10)
        return True
    except Exception as e:
        log(f"Telegram send failed: {e}")
        return False


def log(text):
    stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    with open(LOG_PATH, "a") as f:
        f.write(f"\n[{stamp}]\n{text}\n")


def main():
    config = load_config()
    env = load_env()
    status_text = read_status()

    summary, options = diagnose(status_text)
    message = "infra-guardian self-check\n\n" + summary + "\n\n" + "\n".join(options)

    log(message)

    if send_telegram(config, env, message):
        print("Self-check complete. Proposal sent via Telegram.")
    else:
        print("Self-check complete. Telegram not configured — logged locally.")
        print(message)


if __name__ == "__main__":
    main()
