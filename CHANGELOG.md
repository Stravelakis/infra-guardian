# Changelog

All notable changes to infra-guardian are documented here.
Format based on Keep a Changelog; this project uses semantic versioning.

## [0.1.0] — 2026-07-02
### Added
- Initial SKILL.md with 9 non-negotiable rules, standard workflow,
  status.md machinery, and scheduled self-check (systemd --user timer).
- Backup policy: back up before every change (tweakable via setup.py).
- Plain-English mode (dev-English -> English translation layer).
- HANDOFF.md as a reusable project-continuity artifact.

### Not yet built
- scripts/backup.py, scripts/setup.py, scripts/infra-status-check.py
- references/glossary.md and the per-software references/ ecosystem

# Changelog

## v0.2 — 2026-07-05
### Added
- Rule 10 (no re-circling) to SKILL.md.
- Reference library:
  - providers/: hosting, domain-registrar, dns
  - models/: mistral, nvidia, groq, cerebras, openrouter, gemini
  - selfhosted/: twenty-crm, uptime-kuma, dozzle, camoufox, open-webui,
    librechat, new-api, openclaw, openhuman, goose, hermes-agent
  - wordpress/plugins/: acf, rank-math-pro, tutor-lms-pro, gutenberg,
    code-snippets-pro, litespeed-cache, directorist-pro, aimogen-pro
- behaviour block (no_renagging / snooze_hours) to guardian config.
- Real .env and guardian.config.yaml (gitignored, placeholders only).
- README.md.

### Changed
- Relocated references/backups.md → references/concepts/backups.md.
- .gitignore rewritten and merge-conflict markers removed.

### Fixed
- Collapsed infra-status-check re-circles to a single canonical file (iter 4).
