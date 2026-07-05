# Cerebras (cerebras.ai)

## In plain English
Another very-fast inference provider, OpenAI-compatible API.

## What it's used for
High-speed completions; alternate route in new-api load balancing.

## Where settings live
- API base: https://api.cerebras.ai/v1
- Key: CEREBRAS_API_KEY (.env, placeholder)
- guardian.config.yaml → model_providers.cerebras

## Safe-change checklist
- [ ] Verify model availability (catalogue shifts).
- [ ] Keep as failover, not sole provider, until stable.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| 401 | placeholder key | check .env |
| Timeout | region/network | retry, then check status page |

## New terms → glossary
- (none new)
