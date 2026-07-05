# LibreChat

## In plain English
A self-hosted, multi-provider AI chat platform — one interface across many
model providers, with conversation history and multi-user support.

## What it's used for
Unified chat over OpenAI/Anthropic/Google/etc., presets, and team access.

## Where settings live
- `librechat.yaml` (endpoints/models) + `.env` (keys, auth).
- MongoDB volume holds users/conversations.

## Safe-change checklist
- [ ] Backup MongoDB volume before upgrades.
- [ ] Edit librechat.yaml one endpoint at a time; validate on restart.
- [ ] All provider keys → .env, never committed.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Endpoint missing | YAML typo | Validate librechat.yaml |
| Login broken | Mongo/auth env changed | Check DB conn + auth vars |
| Provider errors | Bad/expired key | Re-check that key in .env |

## New terms → glossary
endpoint, preset, MongoDB
