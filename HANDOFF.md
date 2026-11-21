# HANDOFF — Infra Guardian skill
_Last updated: Sunday, 05 July 2026, 15:25 UTC_

## 0. How to use this file
Read this FIRST before generating anything. It records what exists, what's
settled, and the single next action. Do not regenerate settled files (Rule 10,
in `SKILL.md`).

## 1. What this project is
A Claude Skill: a self-hosting infra guardian that watches the setup, proposes
safe changes, always backs up + checksums before acting, explains things in
plain English, and grows its own vocabulary/reference library over time.

## 2. Core operating rules
Canonical version now genuinely lives in `SKILL.md` (repo root) — 10 rules,
reconstructed this session from scattered references across `scripts/*.py`,
`guardian.config.example.yaml`, and `readme.md`. **This is the one item on
this board that needs your eyes before it's trustworthy**: nothing canonical
existed before, so the reconstruction hasn't been confirmed against your
actual intent yet. Read `SKILL.md` once; if it's right, note that here next
session and this caveat goes away.

## 3. File status board
| File | Status | Notes |
|------|--------|-------|
| `SKILL.md` | **CANONICAL — pending your read-through** | Created 2026-07-05. Previously referenced everywhere but never actually existed. See §2. |
| `references/index.md` | CANONICAL | Routing map for all 51 reference files. Add one line here + to glossary when adding a new reference file. |
| `references/glossary.md` | CANONICAL | Append-only. Do NOT recreate or rewrite existing entries. |
| `references/concepts/backups.md` | DONE | |
| `references/concepts/secrets.md` | DONE | `.env`-only discipline, key-rotation checklist. |
| `references/cloud-providers/google-cloud.md` | DONE | Rewritten 2026-07-05 — full enabled-API surface (100+ APIs), categorized, active-vs-idle flagged. |
| `references/cloud-providers/gemini-vertex.md` | DONE | |
| `references/models/*` (6 files) | DONE | `llm-providers.md` is the "start here" cheat sheet. |
| `references/providers/*` (3 files) | DONE | |
| `references/selfhosted/*` (14 files) | DONE | |
| `references/tool-apis/*` (4 files) | DONE | No comparison/cheat-sheet file yet — deferred, low priority (see §6). |
| `references/wordpress/*` + `wordpress/plugins/*` (12 files) | DONE | |
| `references/infra/*` (7 files) | DONE | |
| `basic.py` / `doctor.py` / `infra-status-check.py` | DONE | |
| `guardian.config.example.yaml` | **NEEDS A DECISION** | Duplicate top-level `telegram:`/`behaviour:` keys — see §5. |
| `guardian.config.yaml` | Not in this repo (gitignored, local-only) | Can't verify contents from here — see §7. |
| `.env.example` | DONE | Placeholders only. |
| `.env` | Not in this repo (gitignored, local-only) | Same as above. |
| `.gitignore` | DONE, one small nit | `!guardian.config.EXAMPLE.yaml` (uppercase) doesn't match the actual `guardian.config.example.yaml` (lowercase) — currently harmless since the ignore pattern above it doesn't match either name, but worth correcting for clarity. Not fixed here — same "needs your eyes" bucket as §5. |
| `readme.md` | DONE | |
| `CHANGELOG.md` | DONE | Up to date through v0.3 (this session). |
| `LICENSE` | DONE | |

**Zero-byte / duplicate-file audit (2026-07-05):** 53 files under `references/`
+ root, 0 empty, 0 duplicate filenames. Clean.

## 4. Decisions locked in (carried forward)
- Dual example/proper files: real values only ever go in the non-example
  file, and that file is gitignored.
- Reference-file template shape: In plain English / What it's used for /
  Where settings live / Safe-change checklist / Common problems table /
  New terms → glossary. New files should match this.
- `behaviour` block in guardian config: `no_renagging: true`,
  `snooze_hours: 24` — the config-side equivalent of Rule 10.
- Google Cloud: "enabled" ≠ "used" — the API list is broad because the
  Console enables things in batches; only flag something as "active" in a
  reference file if there's a real reason to believe it's called.

## 5. THE SINGLE NEXT ACTION (start here)
Decide what to do with `guardian.config.example.yaml`'s duplicate
`telegram:`/`behaviour:` blocks (lines 19–25 vs. 27–35, the second under a
`# REAL config` comment). Two of the same top-level YAML key means most
parsers silently use only the last one — so either the first block is inert,
or something's quietly not working the way it looks like it should. Options:
1. Delete the first (now-redundant) block, keep the example single-shaped.
2. The `# REAL config` section was meant for the real `guardian.config.yaml`
   (gitignored, not in this repo) — if so, move it there instead and clean
   the example back to one block.
Once you say which, it's a small, mechanical fix.

## 6. After that (remaining sequence, all low-priority / optional)
1. Fix the `.gitignore` casing nit (§3) while touching config files anyway.
2. Confirm `SKILL.md`'s reconstructed rules match your intent (§2) — once
   confirmed, update this file's §2 note and drop the "pending" caveat.
3. Optional: sub-group `selfhosted/` in `index.md` by kind (agents / chat
   UIs / gateways / monitoring) if the flat 14-item list starts feeling
   cluttered — deferred as low-value at current size.
4. Optional: a `llm-providers.md`-style comparison file for
   `tool-apis/` (exa vs. tavily vs. parallel vs. browserbase) if any of
   them become actively used — currently Hermes Agent uses SearXNG +
   Firecrawl instead, so these four are dormant alternatives.

## 7. Things this agent could NOT verify (need your confirmation, not mine)
- Actual contents of the real `guardian.config.yaml` and `.env` — both are
  correctly gitignored, so they were never visible from a GitHub clone.
  If either has drifted from what `guardian.config.example.yaml` describes,
  only you can catch that.
- Whether the CHANGELOG v0.2 line "Real .env and guardian.config.yaml
  (gitignored, placeholders only)" is accurate — "real" and "placeholders
  only" read as contradictory. Possibly just loose wording, possibly a
  sign the real files still need real values filled in. Worth a quick check
  next time you're at the machine that has them.

## 8. Anti-time-waste reminders for next session
- Follow Rule 10 strictly (in `SKILL.md` now, for real). Don't regenerate
  a file marked DONE/CANONICAL above — edit only the lines that changed.
- Give explicit file actions ("edit lines X–Y in file Z"), not "here's
  another version."
- This file was rewritten from scratch this session because the prior
  version's status board was stale (claimed `SKILL.md` was canonical
  before it existed, and several "next actions" from v0.2 were already
  done by the time this was written). If something here looks off against
  what actually happened, trust the repo over this file and say so — that's
  exactly the kind of drift this document exists to catch.

## 9. Docs site, three reading levels (2026-11-21)

**What changed (docs only, nothing in the skill):** `site/` moved to the v2 docs theme; `site/src/docs/dev.md`, `plain.md`, `eli5.md` and `site/glossary.yml` rewritten from the repo's real files; front page rebuilt (feature cards, an annotated real run of `backup.py` and `doctor.py`, level cards). Pages are stamped `checkedAgainst: v0.3`, `checkedOn: 2026-11-21`. Two doc-source fixes: `INSTALL.md` (PyYAML is needed by `backup.py` too, Python 3.8+) and `GUIDE.md` (doctor creates a `backups/` folder).

**Not documented (unreleased):** nothing on `main` beyond v0.3 is described except where marked; the five skill commits after the tag only touch `SKILL.md`, `CHANGELOG.md`, `HANDOFF.md` and one glossary line.

**Problems found in the skill itself (NOT fixed, need a decision):**
1. `SKILL.md` on `main` lost its `---` front matter (commit `1760803`, reformatted again in `0f61d48`); the v0.3 tag has it. The tag instead says `references/INDEX.md` while the file is `index.md` (fails on Linux).
2. `setup.py` writes `paths.backup_dir` / `paths.mirror_dir` / `notifications.telegram_*`; `backup.py` reads `backup.root` / `backup.mirror`. The wizard's folder answer is ignored; a Telegram token typed there is stored in plain text and never used.
3. Telegram variable names disagree: the example config says `GUARDIAN_TG_BOT_TOKEN` / `GUARDIAN_TG_CHAT_ID`; the scripts and `.env.example` use `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID`. `doctor.py` reports a placeholder token as "configured".
4. No script reads `retention`, `prompt_cleanup`, `scope: full`, `features.*`, `no_renagging` or `snooze_hours`. Nothing deletes old backups. The "don't nag" rule is instruction only.
5. `doctor.py` creates and writes in `<repo>/backups/` (it claims to change nothing) and checks a different folder than `backup.py` uses (`~/.infra-guardian/backups`).
6. `infra-status-check.py` does not contact any server despite "watches your services" wording in `readme.md`/`GUIDE.md`; it only reads `status.md` (absent from the repo). Its `OPEN` check matches any word containing "open". It writes `self-check.log` in the repo root (not gitignored). It uses `datetime.utcnow()` (DeprecationWarning on 3.12). No systemd timer unit ships, though `doctor.py` looks for one.
7. `readme.md` still names `basic.py`, `guardian.config.EXAMPLE.yaml` and a root `glossary.md`, and calls `SKILL.md` v0.2; `.gitignore` has `!guardian.config.EXAMPLE.yaml` (wrong case).
8. `--restore-last` restores the newest backup of any file; the `.pre-restore.` copy is not recorded in `state.json`.
9. Scripts are committed `100644`, so `doctor.py` warns "not executable" on Linux/macOS.
10. Where Claude should load the skill from is not documented anywhere in the repo.

**Claims not confirmed:** whether a skill loader accepts the current `main` `SKILL.md` header; whether the scripts are ever invoked by Claude in practice (only the instructions say so); contents of the real (gitignored) `guardian.config.yaml` and `.env` (already §7).
