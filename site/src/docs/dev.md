---
# Not reviewed yet: owner ticks templates/docs/REVIEW-CHECKLIST.md, then adds
# checkedAgainst: v0.3 and checkedOn: YYYY-MM-DD here.
---

## infra-guardian: developer view

A Claude Skill for a non-coder who self-hosts (WordPress, self-hosted AI tools, a CRM, free-tier LLM providers). Latest release `v0.3`, MIT licence. The operating rules live in `SKILL.md`.

- **Safety model.** Every change: backup, checksum, dry-run, one change, log. Ten numbered rules in `SKILL.md` (backup before any change, verify the backup, dry-run first, plain-English mode, one change at a time, log everything, ask first, reversible restore, do not nag, no re-circling).
- **Scripts (`scripts/`).**
  - `backup.py --file PATH [--reason TEXT] [--force] [--dry-run]`, plus `--list`, `--restore <id>`, `--restore-last`, `--new-session`. It never reports success on an unverified backup, and snapshots the live file before a restore.
  - `setup.py`: a wizard that writes `guardian.config.yaml`.
  - `doctor.py`: checks the config, scripts, backup folder, timer and optional Telegram. Changes nothing.
  - `infra-status-check.py`: scheduled self-check. Reads `status.md`, detects drift, proposes A/B/C next steps, never acts on its own. Needs PyYAML. Telegram is optional.
- **Config.** `guardian.config.example.yaml` is the committed template; `guardian.config.yaml` is the real, gitignored copy. `behaviour.no_renagging` and `snooze_hours` implement the do-not-nag rule.
- **Secrets.** `.env.example` holds placeholders only. The real `.env` is gitignored.
- **Reference library.** `references/index.md` routes to about 51 files across `cloud-providers/`, `concepts/`, `infra/`, `models/`, `providers/`, `selfhosted/`, `tool-apis/` and `wordpress/`. `references/glossary.md` is append-only.
- **Handoff.** `HANDOFF.md` records what is settled and what is next; `CHANGELOG.md` holds the version history.
