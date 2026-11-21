---
checkedAgainst: v0.3
checkedOn: 2026-11-21
---

## Orientation

infra-guardian is a **Claude skill**, not an application. It is one instruction file (`SKILL.md`, ten numbered rules), four small Python 3 scripts in `scripts/`, a config template, and a library of about 50 plain-English notes in `references/`. There is no server, no daemon you must run, no database and no network service of its own. State is a JSON file and a few text files.

The target user is a non-coder who self-hosts WordPress, a CRM, AI chat tools and free-tier LLM providers. The skill's job is to make Claude slow down: back up, preview, ask, change one thing, write it down.

> **Watch out** This page describes the latest release, **v0.3** (5 Jul 2026, no attached download). `main` has five small commits after it (`SKILL.md`, `CHANGELOG.md`, `HANDOFF.md` and one glossary line), then the docs site; two of them touch only `SKILL.md`. One of them matters: see "SKILL.md front matter" under Gotchas. Anything not on `main` is not described here.

Rules that decide arguments, in order (from `SKILL.md` and the scripts):

1. **No verified backup, no success message.** `backup.py` compares SHA-256 of source and copy and exits with an error if they differ.
2. **A restore is itself reversible.** The live file is copied aside before it is overwritten.
3. **Ask first, one change at a time.** This is an instruction to Claude, not code.
4. **Do not nag, do not re-circle.** Also instruction only (`behaviour.no_renagging`, `snooze_hours`, Rule 10).

## What triggers it

Claude Code decides by the `description` in the `SKILL.md` front matter. Per that text it applies when the user:

- asks to change, configure, debug or check anything in their self-hosted stack;
- touches server config, DNS, hosting, WordPress plugins, or a tool listed in `references/`;
- asks "what does X do" about a tool in the stack;
- is about to change a live file or server.

It says **not** to use it for unrelated coding or writing. The install location is not documented in the repo: `INSTALL.md` only says to clone it. Where Claude Code looks for skills is Claude's rule, not this repo's.

## Enforced by code vs. enforced by instruction

This is the single most important thing to know before relying on it.

| Promise | Enforced by |
|---|---|
| Backup copy equals the original (SHA-256) | **Code**: `backup.py`, `do_backup` |
| Restore re-verifies the stored copy, snapshots the live file first, verifies the result | **Code**: `backup.py`, `do_restore` |
| Dry run saves nothing | **Code**: `--dry-run` returns before any backup, session or state is written (it may create the empty backup root folder) |
| Back up before every change | **Instruction** (Rule 1). Nothing stops a file edit that skips `backup.py` |
| Ask first, one change at a time | **Instruction** (Rules 5, 7) |
| Do not nag after "no" or snooze | **Instruction**. No script reads `no_renagging` or `snooze_hours` |
| Do not regenerate settled files | **Instruction** (Rule 10, `HANDOFF.md` status board) |

> **Why** The skill steers Claude's behaviour. It does not wrap or block the tools Claude uses. If Claude does not follow the instructions, the scripts will not stop it.

## Layout

```
SKILL.md                        rules + navigation (the skill itself)
readme.md  GUIDE.md  INSTALL.md human docs; GUIDE and INSTALL feed this site
HANDOFF.md  CHANGELOG.md        session continuity, version history
guardian.config.example.yaml    committed template
.env.example                    placeholders only
guardian.config.yaml  .env      real files, gitignored, you create them
scripts/                        backup.py  doctor.py  setup.py  infra-status-check.py
references/                     index.md (read first), glossary.md, 8 folders of notes
site/                           this docs site (Astro, shared docs-theme)
.github/workflows/deploy-docs.yml  builds site/ on v* tags or by hand
```

`references/` holds 53 Markdown files: the index, the glossary, and 51 notes in `cloud-providers/`, `concepts/`, `infra/`, `models/`, `providers/`, `selfhosted/`, `tool-apis/` and `wordpress/` (with `plugins/`). Each note follows one shape: In plain English, what it is used for, where settings live, safe-change checklist, common problems, new terms.

## `backup.py`

```bash
python3 scripts/backup.py --file PATH [--reason TEXT] [--force] [--dry-run]
python3 scripts/backup.py --list [--all]
python3 scripts/backup.py --restore ID
python3 scripts/backup.py --restore-last
python3 scripts/backup.py --new-session [--name NAME]
python3 scripts/backup.py --config PATH ...     # any of the above
```

- **Config lookup:** `--config`, then `./guardian.config.yaml`, then `~/.infra-guardian/guardian.config.yaml`. With none it prints that it is using safe defaults.
- **Storage:** default root `~/.infra-guardian/backups` (key `backup.root`). A session folder is named by the UTC time, plus `_NAME` if given. Each copy is `<file>.<UTC stamp>.<8 hex id>`, made with `shutil.copy2`. The record is `state.json` in the root, written to a temp file and renamed, so a crash cannot half-write it. Entries hold `id`, `session`, `source`, `stored`, `mirror`, `sha256`, `size`, `reason`, `timestamp`, `verified`.
- **Policy (`should_back_up`):** `--force` always backs up. With `scope: changed_only` it skips a file whose hash equals its last backup, even in `every_change` mode. Then `mode`: `every_change` backs up; `interval` backs up when the number of earlier changes is a multiple of `interval` (the 1st, then the 6th, 11th and so on for 5); `first_plus_interval` behaves the same in practice, because the first change is already a match. Every non-dry-run call, including a skipped one, adds one to the counter.
- **Mirror:** `backup.mirror` names an optional second folder. The mirror copy is verified too, but a bad mirror only prints a warning; the primary backup stands.
- **Restore:** finds the entry (`--restore-last` takes the last entry in `state.json`, across all files and sessions), falls back to the mirror if the primary is missing, **refuses** if the stored copy no longer matches its recorded hash, copies the live file to `<name>.pre-restore.<UTC stamp>` beside it, copies the backup over it, and verifies again.
- **Limits:** single files only. A folder is rejected with "folders not supported yet". `--list` shows only the current session unless `--all`. It needs PyYAML and prints a plain message and exits 2 without it. Any other stop is `STOPPED: ...` on stderr with exit 1 (argparse usage errors exit 2).

## `doctor.py`

A plain report of `PASS`, `WARN` or `FIX`. It checks, in order: `guardian.config.yaml` exists at the repo root and contains the text `mode`; the four scripts exist and have the executable bit; `<repo>/backups` can be created and written; `systemctl --user is-enabled infra-status-check.timer` (a `WARN` if there is no `systemctl`); and whether `.env` has a non-empty `TELEGRAM_BOT_TOKEN` that does not contain `12345678`. It always exits 0.

## `setup.py`

An interactive wizard that writes `guardian.config.yaml` at the repo root with a small hand-written YAML writer (no dependency). If the file exists it asks before overwriting, default no. Ctrl+C writes nothing. Questions: backup mode (a, b, c), interval, scope, retention, ask-before-cleanup, backup folder (default `<repo>/backups`), optional mirror folder, notification channel, and optionally a Telegram token and chat id. Output keys are `backup`, `paths` and `notifications`.

## `infra-status-check.py`

The scheduled self-check. It reads the config, a minimal `.env` parse, and `status.md` in the repo root. It **does not contact any server**. `diagnose` raises an issue if `status.md` is missing, if the text contains `TODO` or (case-insensitively) `OPEN`, or if it has no `Verified?` column. It appends the result to `self-check.log` and prints the summary and three options (A, B, C), unless it was sent through Telegram. It sends to Telegram only if `telegram.enabled` is true and `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are set in `.env`. It never changes anything. It needs PyYAML.

## Config: which keys does something

| Key | Read by |
|---|---|
| `backup.mode`, `interval`, `scope` (`changed_only` only), `root`, `mirror` | `backup.py` |
| `backup.scope: full`, `retention`, `prompt_cleanup` | nothing; defaults and template only |
| `features.*`, `notifications.*` | nothing |
| `telegram.enabled` | `infra-status-check.py` |
| `behaviour.no_renagging`, `snooze_hours` | nothing; hints for Claude |
| `paths.backup_dir`, `paths.mirror_dir`, `notifications.telegram_*` (written by `setup.py`) | nothing |

Nothing in the repo deletes old backups.

## Run and test

```bash
git clone https://github.com/Stravelakis/infra-guardian.git
cd infra-guardian
cp .env.example .env
cp guardian.config.example.yaml guardian.config.yaml
python3 -m pip install --user pyyaml
python3 scripts/doctor.py
```

There is **no automated test suite** in the repo. To try the backup path safely, copy `scripts/` to a scratch folder, put `backup:\n  root: ./vault-backups` in a `guardian.config.yaml` there, and run `backup.py` against a throwaway file: `--dry-run`, a real backup, `--list`, change the file, `--restore-last`. The captured run on the front page of this site was made exactly that way.

## Extend it

- **A new reference note:** copy the shape of `references/selfhosted/n8n.md` or `references/wordpress/plugins/acf.md`, add one line to `references/index.md`, append new terms to `references/glossary.md` (append only).
- **A new rule or script:** change `SKILL.md`, keep the plain-English output style (`say`, `plain`, `die` in `backup.py`), and give any new setting a safe default.
- **End of a session that changed canonical files:** update the status board in `HANDOFF.md` and add to `CHANGELOG.md` (workflow step 5 in `SKILL.md`).

## The docs site

`site/` is an Astro site from the shared docs-theme. `scripts/sync-docs.mjs` copies `GUIDE.md` and `INSTALL.md` into the Guide and Install sections before every build. `deploy-docs.yml` builds with Node 22 on every `v*` tag or by hand and publishes to docs.stravelakis.com/infra-guardian/.

## Gotchas

- **SKILL.md front matter.** The `v0.3` tag has a proper `---` block with `name:` and `description:`. `main` lost it in commit `1760803` (the `INDEX.md` rename) and `0f61d48` ("Refactor SKILL.md formatting") reformatted it again to `# name infra-guardian` and a bare `description` line. A clone of `main`, which is what `INSTALL.md` tells you to do, therefore has no valid front matter. Whether a given skill loader still picks it up is not confirmed. The tag has the opposite flaw: its `SKILL.md` says `references/INDEX.md` while the file is `index.md`, which fails on case-sensitive file systems. `main` fixed that one.
- **The setup wizard and `backup.py` disagree.** The wizard writes `paths.backup_dir` and `paths.mirror_dir`; `backup.py` reads `backup.root` and `backup.mirror`. The wizard's folder answer is ignored, and backups land in `~/.infra-guardian/backups`. `doctor.py` also checks `<repo>/backups`, a different place. Add `root:` under `backup:` by hand if you want a different folder.
- **Doctor can pass a placeholder.** With `.env.example` copied unchanged, the token is `<paste-real-token-locally>`, so the Telegram line reports `configured`.
- **Doctor is not strictly read-only.** It creates `backups/` in the repo and writes and deletes a test file there.
- **`--restore-last` is global.** After backing up A then B, it restores B.
- **The pre-restore copy is not in `state.json`.** It sits beside the live file and does not show in `--list`.
- **Telegram variable names differ.** The template uses `GUARDIAN_TG_BOT_TOKEN` / `GUARDIAN_TG_CHAT_ID` (`bot_token_env`); the scripts read `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID`, which is also what `.env.example` has. The `_env` keys are not read. A token typed into the wizard is saved in plain text in the config and never used.
- **Duplicate YAML keys.** `guardian.config.example.yaml` has two `telegram:` and two `behaviour:` blocks. PyYAML keeps the last of each. Documented as a known issue in `CHANGELOG.md`.
- **Executable bit.** The four scripts are committed as `100644`, so `doctor.py` warns on Linux and macOS. Run them with `python3 scripts/<name>.py` and ignore it.
- **Untracked state files.** Of the files the skill creates, `.gitignore` covers `.env` and `guardian.config.yaml` only. `backups/`, `status.md` and `self-check.log` are not ignored; check `git status` before you push.
- **`OPEN` is a substring.** The self-check upper-cases `status.md` before looking for `OPEN`, so a line that mentions "open-webui" counts as an open item.
- **Python 3.12 warning.** `infra-status-check.py` uses `datetime.utcnow()` and prints a `DeprecationWarning` there.
