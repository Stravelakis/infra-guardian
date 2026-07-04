# HANDOFF — Infra Guardian skill
_Last updated: Saturday, 04 July 2026, 08:16 UTC_

## 0. How to use this file
Read this FIRST before generating anything. It records what exists, what's
settled, and the single next action. Do not regenerate settled files (Rule 10).

## 1. What this project is
A "skill": a self-hosting infra guardian that watches the setup, proposes safe
changes, always backs up + checksums before acting, explains things in plain
English, and grows its own vocabulary/reference library over time.

## 2. Core operating rules (canonical — live in SKILL.md)
1–9: (existing rules — backup-before-act, checksum, dry-run first, plain-English,
     one-change-at-a-time, log everything, etc.)
10. NO RE-CIRCLING. Before producing any file, check status.md / HANDOFF.md.
    If a file exists and is CREATED/CANONICAL, do NOT regenerate it. Edit only
    the specific lines that must change, and name those lines. Re-open a settled
    file ONLY when a later decision directly breaks it — then name the decision,
    change the minimum, log it. Default: the existing file stays.

## 3. File status board
| File | Status | Notes |
|------|--------|-------|
| SKILL.md | CANONICAL | Rule 10 added. Bump to v0.2 in CHANGELOG at wrap-up. |
| basic.py | DONE | |
| doctor.py | DONE | Created; infra-status-check untouched by it (by design). |
| infra-status-check.py | DONE (iter 4 is canonical) | Iters 3 & 5 were re-circles — collapsed. Keep ONE file. |
| guardian.config.EXAMPLE.yaml | DONE | Has telegram block (enabled:false). |
| guardian.config.yaml | STUB — fill at END | Dual file; keep identical shape to EXAMPLE. |
| .env.example | DONE | Root. Placeholders only (never real tokens). |
| .env | STUB — fill at END | |
| .gitignore | DEFER to END | Avoid double-append churn; write once at wrap-up. |
| glossary.md | CANONICAL | Do NOT recreate. Append new terms only. |
| references/docker.md | DONE | Template shape = approved standard. |
| references/portainer.md | DONE | |
| references/nginx.md | DONE | |
| references/backups.md | DONE | MISPLACED — belongs in a future concepts/ folder (it's a guardian discipline, not a software ref). Relocate later, don't rebuild. |
| references/wordpress/wordpress.md | DONE | |
| references/wordpress/database.md | DONE | |
| references/wordpress/plugins.md | DONE | |
| references/providers/* | NOT STARTED | ← NEXT TASK |
| README.md | DEFER to END | Choices may still affect it. |
| CHANGELOG.md | PENDING | Record v0.2 at wrap-up (Rule 10 + reference library). |

## 4. Decisions locked in
- Dual example/proper files: CREATE BOTH, FILL ONLY THE EXAMPLE now, real one at end.
- Tokens in .env (example or not) are ALWAYS placeholders, never real.
- guardian.config.yaml gained a behaviour block:
    behaviour:
      no_renagging: true
      snooze_hours: 24
  (guardian-side equivalent of Rule 10 — don't re-raise a snoozed/declined proposal
   until the status fingerprint changes.)
- Reference-file template shape = the docker.md structure (In plain English /
  What it's used for / Where settings live / Safe-change checklist /
  Common problems table / New terms → glossary).

## 5. THE SINGLE NEXT ACTION (start here tomorrow)
Create the `references/providers/` set using the approved template shape,
one file per provider (hosting / domain-registrar / DNS). No shape questions —
produce them, user confirms "done", move on.

## 6. After that (remaining sequence)
1. references/providers/* (next)
2. Relocate backups.md → concepts/ (minimal move)
3. Fill the real .env and guardian.config.yaml
4. Write .gitignore once
5. Write README.md (last — reflects all final choices)
6. CHANGELOG v0.2

## 7. Anti-time-waste reminders for next session
- Follow Rule 10 strictly. We lost several iterations re-generating settled files.
- Give explicit file actions ("create X", "replace lines A–B"), never "here's another version".
- Don't ask "what next?" — advance the sequence in §6 and state the user's action.
