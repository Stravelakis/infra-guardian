# Guide

## What it is for

infra-guardian is for people who self-host apps (WordPress, a CRM, AI chat tools) but do not write code, and who want a plain-English explanation before anything changes. It is probably not for an experienced sysadmin who wants full manual control with no guardrails.

## The one promise

> Back up, preview, ask, change one thing, write it down.

It never makes a big pile of changes at once, and it never changes something without a saved backup to undo it.

## The ten rules

The rules are written out in `SKILL.md`. In short:

1. Backup before any change.
2. Verify the backup (checksum), do not just take it.
3. Dry-run first: show what would happen.
4. Plain-English mode. New technical words go in the glossary.
5. One change at a time.
6. Log everything.
7. Ask first, always.
8. Restore must be reversible too: the current file is saved before a restore.
9. Do not nag: once you decline or snooze, it stays quiet until the status changes.
10. No re-circling: files marked settled are edited line by line, not regenerated.

## Working with backups

```bash
python3 scripts/backup.py --file PATH --reason "why"
python3 scripts/backup.py --list
python3 scripts/backup.py --restore-last
```

Add `--dry-run` to see what would be backed up without touching anything. `--restore <id>` restores a specific backup. A backup is only reported as done once its checksum matches the original.

## Checking its own health

```bash
python3 scripts/doctor.py
```

It prints a plain pass or fix report for the config, the scripts, the backup folder, the timer and optional Telegram alerts. It changes nothing of yours, apart from creating a `backups` folder in the project if there is none.

## The reference library

`references/index.md` is the map. Plain-English notes cover hosting, domain registrar and DNS; AI model providers (Mistral, NVIDIA, Groq, Cerebras, OpenRouter, Gemini); self-hosted apps (for example Twenty CRM, Uptime Kuma, Open WebUI, LibreChat, n8n); and WordPress plugins (for example ACF, Rank Math Pro, LiteSpeed Cache). `references/glossary.md` explains every tech word in one line.

## About secret keys

You do not need any keys for the basics. Some optional features (Telegram alerts, live AI models) need a key, which lives only in the hidden `.env` file that is never uploaded. If you would rather not keep keys in a file, you can use your hosting panel's secrets section instead.
