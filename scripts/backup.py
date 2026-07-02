#!/usr/bin/env python3
"""
Infra Guardian — backup.py

In plain English: this is the "undo button" for your config work. Before any
change touches a file, this script saves a copy somewhere safe, checks the copy
is a perfect match (not corrupted), and remembers where it put it. If a change
goes wrong, --restore-last puts things back exactly as they were.

Design contract (see HANDOFF.md §7 and SKILL.md rule 3):
  - Never report success on an unverified backup.
  - A backup that dies with the original isn't a backup -> optional mirror path.
  - Restore is reversible: the live file is snapshotted before it's overwritten.

Commands:
  backup.py --file PATH [--reason TEXT] [--force] [--dry-run]
  backup.py --list [--all]
  backup.py --restore <id>
  backup.py --restore-last
  backup.py --new-session [--name NAME]

Config: guardian.config.yaml (see setup.py). Falls back to safe defaults.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import sys
import uuid
from pathlib import Path

# ---------------------------------------------------------------------------
# YAML is the only external dependency. Fail with a plain-English message
# instead of a stack trace if it's missing.
# ---------------------------------------------------------------------------
try:
    import yaml
except ImportError:  # pragma: no cover
    print(
        "This tool needs the 'PyYAML' package to read your settings file.\n"
        "In plain English: run this once, then try again:\n"
        "    python3 -m pip install --user pyyaml",
        file=sys.stderr,
    )
    sys.exit(2)


# ---------------------------------------------------------------------------
# Small talk helpers (plain-English output — SKILL.md "Plain-English mode")
# ---------------------------------------------------------------------------
def say(msg: str) -> None:
    print(msg)


def plain(msg: str) -> None:
    """Print a 'so, in normal words...' gloss."""
    print(f"  In plain English: {msg}")


def die(msg: str, code: int = 1) -> None:
    print(f"STOPPED: {msg}", file=sys.stderr)
    sys.exit(code)


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def session_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def short_id() -> str:
    return uuid.uuid4().hex[:8]


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
DEFAULT_CONFIG = {
    "backup": {
        "mode": "every_change",      # every_change | interval | first_plus_interval
        "interval": 5,               # used by interval / first_plus_interval
        "scope": "changed_only",     # changed_only | full
        "retention": "session",      # session | keep
        "prompt_cleanup": True,
        "root": "~/.infra-guardian/backups",
        "mirror": None,              # optional second location (3-2-1 principle)
    }
}


def find_config(explicit: str | None) -> Path | None:
    """Look for guardian.config.yaml: --config, then CWD, then home dir."""
    candidates = []
    if explicit:
        candidates.append(Path(explicit).expanduser())
    candidates.append(Path.cwd() / "guardian.config.yaml")
    candidates.append(Path.home() / ".infra-guardian" / "guardian.config.yaml")
    for c in candidates:
        if c.is_file():
            return c
    return None


def load_config(explicit: str | None) -> dict:
    path = find_config(explicit)
    cfg = {"backup": dict(DEFAULT_CONFIG["backup"])}
    if path:
        with open(path, "r", encoding="utf-8") as fh:
            loaded = yaml.safe_load(fh) or {}
        cfg["backup"].update((loaded.get("backup") or {}))
        say(f"Using settings from: {path}")
    else:
        say("No guardian.config.yaml found — using safe defaults "
            "(backup every change). Run setup.py to customise.")
    return cfg


# ---------------------------------------------------------------------------
# Storage layout + state
# ---------------------------------------------------------------------------
def backup_root(cfg: dict) -> Path:
    root = Path(cfg["backup"]["root"]).expanduser()
    root.mkdir(parents=True, exist_ok=True)
    return root


def state_path(cfg: dict) -> Path:
    return backup_root(cfg) / "state.json"


def load_state(cfg: dict) -> dict:
    p = state_path(cfg)
    if p.is_file():
        with open(p, "r", encoding="utf-8") as fh:
            return json.load(fh)
    return {"current_session": None, "change_count": 0, "entries": []}


def save_state(cfg: dict, state: dict) -> None:
    p = state_path(cfg)
    tmp = p.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2)
    tmp.replace(p)  # atomic write so a crash can't corrupt the record


def get_or_create_session(cfg: dict, state: dict, name: str | None = None) -> str:
    if state.get("current_session"):
        return state["current_session"]
    sid = f"{session_stamp()}"
    if name:
        safe = "".join(c if c.isalnum() or c in "-_" else "-" for c in name)
        sid = f"{sid}_{safe}"
    (backup_root(cfg) / sid).mkdir(parents=True, exist_ok=True)
    state["current_session"] = sid
    state["change_count"] = 0
    save_state(cfg, state)
    say(f"Started a new backup session: {sid}")
    return sid


# ---------------------------------------------------------------------------
# Checksums + verification
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def last_entry_for(state: dict, source: Path) -> dict | None:
    src = str(source.resolve())
    for entry in reversed(state["entries"]):
        if entry["source"] == src:
            return entry
    return None


# ---------------------------------------------------------------------------
# Policy: should we actually snapshot right now?
# ---------------------------------------------------------------------------
def should_back_up(cfg: dict, state: dict, source: Path, force: bool) -> tuple[bool, str]:
    if force:
        return True, "forced (--force)"

    mode = cfg["backup"]["mode"]
    scope = cfg["backup"]["scope"]

    # changed_only: skip if the file is byte-for-byte identical to its last backup.
    if scope == "changed_only":
        prev = last_entry_for(state, source)
        if prev and source.is_file() and sha256_of(source) == prev["sha256"]:
            return False, "file unchanged since last backup"

    if mode == "every_change":
        return True, "policy: every change"

    count = state.get("change_count", 0)
    interval = max(1, int(cfg["backup"]["interval"]))

    if mode == "first_plus_interval" and count == 0:
        return True, "policy: first change of the session"

    # interval / first_plus_interval: back up on the Nth change.
    if (count % interval) == 0:
        return True, f"policy: every {interval}th change (this is #{count + 1})"
    return False, f"policy: only every {interval}th change (this is #{count + 1})"


# ---------------------------------------------------------------------------
# Core actions
# ---------------------------------------------------------------------------
def do_backup(cfg: dict, state: dict, source: Path, reason: str,
              force: bool, dry_run: bool) -> None:
    source = source.expanduser()
    if not source.exists():
        die(f"Can't find the file to back up: {source}")
    if not source.is_file():
        die(f"That path isn't a single file (folders not supported yet): {source}")

    proceed, why = should_back_up(cfg, state, source, force)

    if dry_run:
        say(f"[DRY RUN] Would {'BACK UP' if proceed else 'SKIP'} {source}")
        plain(why)
        return

    # We still count this as a "change" for interval bookkeeping.
    state["change_count"] = state.get("change_count", 0) + 1

    if not proceed:
        save_state(cfg, state)
        say(f"Skipped backup of {source}.")
        plain(why)
        return

    sid = get_or_create_session(cfg, state)
    stamp = session_stamp()
    sid_short = short_id()
    safe_name = source.name
    stored_name = f"{safe_name}.{stamp}.{sid_short}"
    dest = backup_root(cfg) / sid / stored_name

    shutil.copy2(source, dest)  # copy2 preserves timestamps/permissions

    # VERIFY — this is the whole point. Compare checksums; refuse to claim success otherwise.
    src_sum = sha256_of(source)
    dst_sum = sha256_of(dest)
    if src_sum != dst_sum:
        dest.unlink(missing_ok=True)
        die("Backup copy did NOT match the original (checksum mismatch). "
            "Nothing was changed. Try again or check disk space.")

    entry = {
        "id": sid_short,
        "session": sid,
        "source": str(source.resolve()),
        "stored": str(dest),
        "mirror": None,
        "sha256": src_sum,
        "size": dest.stat().st_size,
        "reason": reason,
        "timestamp": now_iso(),
        "verified": "yes — sha256 match",
    }

    # Optional mirror (3-2-1). A backup that dies with the primary isn't a backup.
    mirror_root = cfg["backup"].get("mirror")
    if mirror_root:
        mdir = Path(mirror_root).expanduser() / sid
        mdir.mkdir(parents=True, exist_ok=True)
        mdest = mdir / stored_name
        shutil.copy2(dest, mdest)
        if sha256_of(mdest) != src_sum:
            say("WARNING: mirror copy failed verification. Primary backup is fine; "
                "mirror is NOT trustworthy.")
        else:
            entry["mirror"] = str(mdest)

    state["entries"].append(entry)
    save_state(cfg, state)

    say(f"Backed up  ->  {dest}")
    plain(f"A verified safe copy of '{source.name}' now exists. Reason: {reason}. "
          f"Restore it any time with:  backup.py --restore {sid_short}")
    if entry["mirror"]:
        plain(f"A second copy also lives at: {entry['mirror']}")


def cmd_list(cfg: dict, state: dict, show_all: bool) -> None:
    current = state.get("current_session")
    entries = state["entries"]
    if not show_all:
        entries = [e for e in entries if e["session"] == current]
    if not entries:
        say("No backups recorded yet.")
        return
    say(f"{'ID':<10} {'WHEN (UTC)':<22} {'FILE':<28} REASON")
    say("-" * 80)
    for e in entries:
        say(f"{e['id']:<10} {e['timestamp']:<22} {Path(e['source']).name:<28} {e['reason']}")
    plain("Use the ID in the first column with --restore <id>.")


def _find_entry(state: dict, entry_id: str) -> dict | None:
    for e in state["entries"]:
        if e["id"] == entry_id:
            return e
    return None


def do_restore(cfg: dict, state: dict, entry: dict) -> None:
    stored = Path(entry["stored"])
    original = Path(entry["source"])

    if not stored.is_file():
        # Fall back to the mirror if the primary copy is gone.
        if entry.get("mirror") and Path(entry["mirror"]).is_file():
            stored = Path(entry["mirror"])
            say("Primary backup missing — restoring from the mirror copy instead.")
        else:
            die(f"The backup file is missing: {entry['stored']}")

    # Confirm the backup itself is still intact before we trust it.
    if sha256_of(stored) != entry["sha256"]:
        die("The backup file is corrupted (checksum no longer matches). "
            "NOT restoring — this would make things worse.")

    # Make restore reversible: snapshot the CURRENT live file first.
    if original.is_file():
        pre = original.with_suffix(original.suffix + f".pre-restore.{session_stamp()}")
        shutil.copy2(original, pre)
        say(f"Saved the current version first (in case you want it back): {pre}")

    original.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(stored, original)

    if sha256_of(original) != entry["sha256"]:
        die("Restore finished but the result doesn't match the backup. "
            "Something is wrong with the disk — do not trust this file.")

    say(f"Restored  {original}  from backup {entry['id']}.")
    plain(f"'{original.name}' is now exactly as it was at {entry['timestamp']}.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Infra Guardian backup/restore — the undo button for config work."
    )
    p.add_argument("--config", help="Path to guardian.config.yaml")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--file", help="Path of the file to back up")
    g.add_argument("--list", action="store_true", help="List backups")
    g.add_argument("--restore", metavar="ID", help="Restore a specific backup by ID")
    g.add_argument("--restore-last", action="store_true", help="Restore the most recent backup")
    g.add_argument("--new-session", action="store_true", help="Start a fresh backup session")

    p.add_argument("--reason", default="manual", help="Why this backup was made")
    p.add_argument("--force", action="store_true", help="Back up even if policy would skip")
    p.add_argument("--dry-run", action="store_true", help="Show what would happen, change nothing")
    p.add_argument("--all", action="store_true", help="With --list, show every session")
    p.add_argument("--name", help="With --new-session, give the session a label")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg = load_config(args.config)
    state = load_state(cfg)

    if args.new_session:
        state["current_session"] = None
        save_state(cfg, state)
        get_or_create_session(cfg, state, name=args.name)
        return 0

    if args.list:
        cmd_list(cfg, state, show_all=args.all)
        return 0

    if args.restore:
        entry = _find_entry(state, args.restore)
        if not entry:
            die(f"No backup with ID '{args.restore}'. Run --list to see valid IDs.")
        do_restore(cfg, state, entry)
        return 0

    if args.restore_last:
        if not state["entries"]:
            die("There are no backups to restore yet.")
        do_restore(cfg, state, state["entries"][-1])
        return 0

    if args.file:
        do_backup(cfg, state, Path(args.file), args.reason, args.force, args.dry_run)
        return 0

    build_parser().print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
