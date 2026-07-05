# Goose

## In plain English
Goose is an open-source AI agent that can act on your machine — running tasks,
using tools, and executing multi-step work (docs at goose-docs.ai). [[goose-docs.ai]]

## What it's used for
Autonomous/assisted coding and ops tasks via extensions ("toolkits"), backed by
a model provider you configure.

## Where settings live
- Its config file (provider, model, extensions).
- Provider API key in env / config → treat as secret.

## Safe-change checklist
- [ ] Run in a sandboxed dir/container — it can execute commands.
- [ ] Enable one extension/toolkit at a time.
- [ ] Review proposed actions before auto-approving (mirrors Rule: dry-run first).

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| No model responses | Provider/key unset | Check provider config |
| Unexpected file changes | Broad permissions | Restrict working directory |
| Extension fails | Missing dependency | Check that toolkit's reqs |

## New terms → glossary
AI agent, toolkit/extension, sandbox
