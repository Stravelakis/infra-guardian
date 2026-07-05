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

## v0.3 — 2026-07-05
### Added
- `SKILL.md` created at repo root — the file every prior session referenced
  as canonical but which never actually existed until now. Rules 1–10
  reconstructed from `scripts/backup.py`, `scripts/doctor.py`,
  `scripts/setup.py`, `guardian.config.example.yaml`, and `readme.md`
  (nothing canonical existed to check the reconstruction against —
  pending a read-through to confirm accuracy).
- `references/index.md` — routing map for all 51 reference files, so a
  session opens only the relevant file instead of the whole tree.
- `references/concepts/secrets.md` — `.env`-only discipline, pre-push
  checklist, key-rotation gotchas.

### Changed
- `references/cloud-providers/google-cloud.md` rewritten: broadened from
  "Weather + YouTube" to the full enabled-API surface (100+ APIs),
  organized by category (AI/Gemini, Maps Platform, Workspace, Data/
  Analytics, Infra, Identity/Security, Firebase, Search/Web, YouTube,
  Misc) with active-vs-idle status per category.
- `references/models/gemini.md` — added a cross-link to
  `cloud-providers/gemini-vertex.md` (was previously one-directional).
- `references/glossary.md` — added "rotate (a key)" (introduced by
  `secrets.md` but not appended at the time).

### Fixed
- Case-sensitivity bug: `SKILL.md` referenced `references/INDEX.md`
  (uppercase) in four places; actual committed filename is
  `references/index.md` (lowercase). Harmless on Windows, breaks on
  GitHub/Linux. Corrected to lowercase throughout `SKILL.md`.
- Removed a stray duplicate `# Changelog` H1 header (this file, was
  sitting between the v0.1.0 and v0.2 entries).

### Known issue — not fixed, needs a decision
- `guardian.config.example.yaml` contains **duplicate top-level keys**:
  `telegram:` and `behaviour:` each appear twice (lines 19–25 and a
  second block under a `# REAL config` comment at lines 27–35). Since
  YAML doesn't allow two same-named top-level keys safely, most parsers
  silently use only the last occurrence — meaning the first block is
  dead weight at best, or a bug if anything relies on it. Looks like
  content meant for a separate `guardian.config.yaml` got appended to
  the example file instead. Needs a decision: delete the redundant
  first block, or split the `# REAL config` section out into its own
  file. Not touched here since it wasn't clear which block (if either)
  reflects your actual intended values.
