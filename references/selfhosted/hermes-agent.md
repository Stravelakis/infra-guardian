# Hermes Agent (Nous Research)

## In plain English
Hermes Agent (hermes-agent.nousresearch.com) is an AI agent positioned as an
improved OpenClaw — its headline fixes are built-in memory, a more stable
gateway, and better token handling. [[4]] NOTE: young project; verify against docs.

## What it's used for
Autonomous, tool-using tasks with persistent memory across successful runs. [[4]]

## Where settings live
- Its config/env (model provider, gateway, memory store).
- Writes memory to SQLite on successful tasks. [[4]]
- Provider keys as secrets.

## Safe-change checklist
- [ ] Sandbox it — it executes tasks/tools.
- [ ] Backup its SQLite memory before upgrades. [[4]]
- [ ] Confirm gateway + token config before long autonomous runs. [[4]]

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Memory not saving | SQLite path/perms | Check memory DB mount [[4]] |
| Gateway drops | Config/instability | Verify gateway settings [[4]] |
| Token errors | Limit/key issue | Re-check token + provider key [[4]] |

## New terms → glossary
persistent memory, SQLite, gateway, token
