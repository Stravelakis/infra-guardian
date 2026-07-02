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
