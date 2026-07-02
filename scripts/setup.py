#!/usr/bin/env python3
"""
infra-guardian :: setup.py

A friendly, plain-English wizard that writes guardian.config.yaml.

You do NOT need to be a developer to run this. It asks a few simple
questions, explains each one, and offers safe defaults you can just
press Enter to accept. Nothing is changed on your system except the
creation of one settings file (guardian.config.yaml) in the project root.

Run it with:
    python3 scripts/setup.py

Re-run it any time you want to change your choices.
"""

import os
import sys
from datetime import datetime, timezone

# ---------------------------------------------------------------------------
# Where the config file lives: project root (one level up from /scripts).
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, os.pardir))
CONFIG_PATH = os.path.join(PROJECT_ROOT, "guardian.config.yaml")


# ---------------------------------------------------------------------------
# Small helpers for a gentle, plain-English conversation.
# ---------------------------------------------------------------------------
def say(text=""):
    print(text)


def ask_choice(question, options, default_key):
    """
    Ask an A/B/C style question. `options` is a list of (key, label) tuples.
    Returns the chosen key. Pressing Enter accepts the default.
    """
    say(question)
    for key, label in options:
        marker = " (default)" if key == default_key else ""
        say(f"   {key}) {label}{marker}")
    valid = {key.lower() for key, _ in options}
    while True:
        raw = input(f"Choose [{default_key}]: ").strip().lower()
        if raw == "":
            return default_key
        if raw in valid:
            return raw
        say("   Sorry, I didn't recognise that. Please type one of the letters shown.")


def ask_yes_no(question, default_yes=True):
    suffix = "[Y/n]" if default_yes else "[y/N]"
    while True:
        raw = input(f"{question} {suffix}: ").strip().lower()
        if raw == "":
            return default_yes
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        say("   Please answer y (yes) or n (no).")


def ask_text(question, default=""):
    hint = f" [{default}]" if default else ""
    raw = input(f"{question}{hint}: ").strip()
    return raw if raw else default


def ask_int(question, default):
    while True:
        raw = input(f"{question} [{default}]: ").strip()
        if raw == "":
            return default
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        say("   Please enter a whole number greater than zero.")


# ---------------------------------------------------------------------------
# Tiny YAML writer — hand-rolled so we need NO external libraries.
# Our config is simple and flat, so this stays safe and predictable.
# ---------------------------------------------------------------------------
def yaml_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    if v is None or v == "":
        return '""'
    # Quote strings to be safe (paths, tokens, words like "yes").
    return f'"{v}"'


def write_config(cfg):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = []
    lines.append("# guardian.config.yaml")
    lines.append("# Written by scripts/setup.py — safe to edit by hand later.")
    lines.append(f"# Last written: {stamp}")
    lines.append("")
    lines.append("backup:")
    lines.append(f"  mode: {yaml_value(cfg['backup']['mode'])}"
                 "        # every_change | interval | first_plus_interval")
    lines.append(f"  interval: {yaml_value(cfg['backup']['interval'])}"
                 "           # only used by interval / first_plus_interval")
    lines.append(f"  scope: {yaml_value(cfg['backup']['scope'])}"
                 "       # changed_only | full")
    lines.append(f"  retention: {yaml_value(cfg['backup']['retention'])}"
                 "      # session | keep")
    lines.append(f"  prompt_cleanup: {yaml_value(cfg['backup']['prompt_cleanup'])}"
                 "    # ask before deleting a past session's backups")
    lines.append("")
    lines.append("paths:")
    lines.append(f"  backup_dir: {yaml_value(cfg['paths']['backup_dir'])}"
                 "   # where backups are stored")
    lines.append(f"  mirror_dir: {yaml_value(cfg['paths']['mirror_dir'])}"
                 "   # optional 2nd copy (3-2-1 rule); leave empty to skip")
    lines.append("")
    lines.append("notifications:")
    lines.append(f"  channel: {yaml_value(cfg['notifications']['channel'])}"
                 "     # telegram | none")
    lines.append(f"  telegram_bot_token: {yaml_value(cfg['notifications']['telegram_bot_token'])}")
    lines.append(f"  telegram_chat_id: {yaml_value(cfg['notifications']['telegram_chat_id'])}")
    lines.append("")

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# The wizard.
# ---------------------------------------------------------------------------
def main():
    say("=" * 64)
    say(" Infra Guardian — Setup Wizard")
    say("=" * 64)
    say("I'll ask a few short questions. Press Enter to accept any")
    say("default. You can re-run this any time to change your answers.")
    say("")

    # If a config already exists, protect it (rule 3: never lose good state).
    if os.path.exists(CONFIG_PATH):
        say("Heads-up: a guardian.config.yaml already exists.")
        if not ask_yes_no("Do you want to overwrite it with new answers?", default_yes=False):
            say("No changes made. Your existing settings are untouched. Bye!")
            return

    cfg = {
        "backup": {},
        "paths": {},
        "notifications": {},
    }

    # --- Backup mode ---------------------------------------------------------
    say("\n--- 1. How often should I make a safety backup? ---")
    say("In plain English: a backup is a copy of a file taken BEFORE I change")
    say("it, so we can always undo. The safest choice is 'before every change'.")
    say("")
    mode = ask_choice(
        "Pick your backup style:",
        [
            ("a", "Before EVERY change — safest, recommended"),
            ("b", "Every few changes — smaller, slightly riskier"),
            ("c", "First change, then every few after that"),
        ],
        default_key="a",
    )
    mode_map = {"a": "every_change", "b": "interval", "c": "first_plus_interval"}
    cfg["backup"]["mode"] = mode_map[mode]

    if cfg["backup"]["mode"] == "every_change":
        cfg["backup"]["interval"] = 5  # stored but unused; kept for easy switching
    else:
        say("")
        cfg["backup"]["interval"] = ask_int(
            "How many changes between backups? (e.g. 5 means every 5th change)", 5
        )

    # --- Scope ---------------------------------------------------------------
    say("\n--- 2. What should each backup include? ---")
    say("In plain English: 'only changed files' keeps backups small and fast.")
    scope = ask_choice(
        "Backup scope:",
        [
            ("a", "Only the files I'm about to change — recommended, small"),
            ("b", "The whole folder each time — bigger, thorough"),
        ],
        default_key="a",
    )
    cfg["backup"]["scope"] = "changed_only" if scope == "a" else "full"

    # --- Retention -----------------------------------------------------------
    say("\n--- 3. How long should I keep backups? ---")
    say("In plain English: a 'session' is one work sitting. 'Keep everything'")
    say("never auto-deletes, but uses more disk over time.")
    retention = ask_choice(
        "Keep backups for:",
        [
            ("a", "This session, then offer to tidy up — recommended"),
            ("b", "Keep everything, forever"),
        ],
        default_key="a",
    )
    cfg["backup"]["retention"] = "session" if retention == "a" else "keep"

    # --- Cleanup prompt ------------------------------------------------------
    say("\n--- 4. Tidy-up safety check ---")
    say("In plain English: next time I start, if last session went perfectly,")
    say("should I ASK you before deleting its old backups? (I never delete")
    say("silently.)")
    cfg["backup"]["prompt_cleanup"] = ask_yes_no(
        "Ask before deleting old backups?", default_yes=True
    )

    # --- Paths ---------------------------------------------------------------
    say("\n--- 5. Where should backups be stored? ---")
    default_backup = os.path.join(PROJECT_ROOT, "backups")
    cfg["paths"]["backup_dir"] = ask_text(
        "Backup folder (full path)", default=default_backup
    )
    say("")
    say("Optional: a SECOND copy on a different disk/drive (the '3-2-1' rule —")
    say("a backup that dies with the original isn't really a backup).")
    if ask_yes_no("Set up a second mirror copy now?", default_yes=False):
        cfg["paths"]["mirror_dir"] = ask_text("Mirror folder (full path)", default="")
    else:
        cfg["paths"]["mirror_dir"] = ""

    # --- Notifications -------------------------------------------------------
    say("\n--- 6. How should the scheduled check reach you? ---")
    say("In plain English: a timer occasionally checks status and can message")
    say("you with A/B/C suggestions. Telegram works from any of your setups —")
    say("it isn't tied to one machine or to Hermes.")
    channel = ask_choice(
        "Notification channel:",
        [
            ("a", "Telegram bot — recommended, works everywhere"),
            ("b", "None for now — I'll set it up later"),
        ],
        default_key="a",
    )
    if channel == "a":
        cfg["notifications"]["channel"] = "telegram"
        say("")
        say("You'll need two things from Telegram (I'll guide you if unsure):")
        say("  • a bot token (from @BotFather)")
        say("  • your chat id (from @userinfobot)")
        say("You can leave these blank now and paste them into the config later.")
        cfg["notifications"]["telegram_bot_token"] = ask_text(
            "Telegram bot token", default=""
        )
        cfg["notifications"]["telegram_chat_id"] = ask_text(
            "Telegram chat id", default=""
        )
    else:
        cfg["notifications"]["channel"] = "none"
        cfg["notifications"]["telegram_bot_token"] = ""
        cfg["notifications"]["telegram_chat_id"] = ""

    # --- Write it out --------------------------------------------------------
    write_config(cfg)

    say("\n" + "=" * 64)
    say(" All set! I saved your choices to:")
    say(f"   {CONFIG_PATH}")
    say("=" * 64)
    say("In plain English, here's what you chose:")
    say(f"  • Backups: {cfg['backup']['mode'].replace('_', ' ')}")
    say(f"  • Includes: {cfg['backup']['scope'].replace('_', ' ')}")
    say(f"  • Kept: {cfg['backup']['retention']}")
    say(f"  • Stored in: {cfg['paths']['backup_dir']}")
    if cfg["paths"]["mirror_dir"]:
        say(f"  • Mirror copy: {cfg['paths']['mirror_dir']}")
    say(f"  • Alerts via: {cfg['notifications']['channel']}")
    say("")
    say("You can re-run this wizard any time, or edit the file by hand.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        say("\n\nCancelled. No settings file was written. Nothing changed.")
        sys.exit(1)
