# Secrets & API keys — discipline

## In plain English
Every key, token, or password for any service in this stack lives in one
place (`.env`, gitignored) and nowhere else — never in a reference file,
config example, script, or commit.

## The rule
- Real values → `.env` only. Never `.env.example`, never `guardian.config.yaml`
  comments, never hardcoded in a script "just for testing."
- Example/template files (`.env.example`, `guardian.config.example.yaml`)
  use placeholders only — e.g. `<paste-real-token-locally>`.
- `.gitignore` must cover `.env` and any real (non-example) config file
  before the first commit that could contain one.

## Before every push
- [ ] `git status` — confirm `.env` / real config files aren't staged.
- [ ] If a key was ever committed by mistake: rotate it immediately, don't
      just delete the file — the old key is still in git history.

## Safe-change checklist
- [ ] New service added → add its key to `.env.example` as a placeholder,
      real value only in local `.env`.
- [ ] Rotating a key → update `.env` locally, restart whatever reads it,
      confirm the old key stops working before considering it done.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Key works locally, fails in CI/on server | `.env` not deployed (correctly) or wrong var name | Confirm the target environment loads its own `.env`, not yours |
| Old key still works after "rotating" | Only `.env` changed, provider-side key never revoked | Revoke the old key at the provider, not just swap the local value |
| Key found in a git diff before commit | About to leak a secret | Unstage the file, add it to `.gitignore`, re-check history if already committed |

## New terms → glossary
- gitignore, rotate (a key), placeholder value
