# OpenHuman

## In plain English
OpenHuman (tinyhumans.ai/openhuman) is an AI agent in the same wave as OpenClaw
and Hermes Agent. NOTE: early/limited public documentation — treat details as
provisional and confirm on its site. [[2]] [[3]]

## What it's used for
Autonomous agent tasks; frequently compared head-to-head with OpenClaw and
Hermes Agent. [[2]] [[3]]

## Where settings live
- Its config/env (model provider + keys).
- Provider keys as secrets.

## Safe-change checklist
- [ ] Sandbox / isolate before granting real access.
- [ ] Verify provider + memory setup before long runs.
- [ ] Change one capability at a time.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Agent won't start | Provider/key unset | Check model config |
| Inconsistent behaviour | Immature build | Pin version, log runs |
| Data not retained | No persistence | Verify storage config |

## New terms → glossary
autonomous agent, persistence, provider
