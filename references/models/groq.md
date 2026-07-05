# Groq (groq.com)

## In plain English
Very fast inference host for open models. Same request shape as OpenAI's API.

## What it's used for
Low-latency chat backend; good default for interactive UIs.

## Where settings live
- API base: https://api.groq.com/openai/v1
- Key: GROQ_API_KEY (.env, placeholder)
- Model block: guardian.config.yaml → model_providers.groq

## Safe-change checklist
- [ ] Confirm model still listed before wiring it in.
- [ ] Note token/min limits — Groq is fast but capped.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| 429 fast | high throughput hit TPM cap | throttle / route overflow via new-api |
| Model 404 | model retired | list models, update ID |

## New terms → glossary
- TPM (tokens per minute)
