# New API

## In plain English
An open-source LLM API gateway/management system (QuantumNous/new-api) — a
next-gen One-API-style hub that unifies many model providers behind one
OpenAI-compatible endpoint with keys, quotas, and billing. [[github: QuantumNous/new-api]]

## What it's used for
One endpoint + key management in front of many providers; usage tracking,
channels, and rate/quota control.

## Where settings live
- Admin UI (channels, tokens, users).
- Env vars + DB (MySQL/SQLite) + Redis. Upstream provider keys added as channels.

## Safe-change checklist
- [ ] Backup the DB before upgrades (tokens/quotas live there).
- [ ] Add one provider channel, test, then add more.
- [ ] Store the admin session secret + provider keys as secrets.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Channel returns error | Bad upstream key | Test that channel in UI |
| Quota exhausted | Token limit hit | Adjust token quota |
| Won't start | DB/Redis unreachable | Check DB + Redis conn |

## New terms → glossary
API gateway, channel, quota, OpenAI-compatible
