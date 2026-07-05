# OpenRouter (openrouter.ai)

## In plain English
A router/aggregator: one key, many providers' models behind one endpoint.

## What it's used for
Single access point + fallback across providers; simplifies new-api config.

## Where settings live
- API base: https://openrouter.ai/api/v1
- Key: OPENROUTER_API_KEY (.env, placeholder)
- guardian.config.yaml → model_providers.openrouter
- Optional headers: HTTP-Referer / X-Title for attribution

## Safe-change checklist
- [ ] Model IDs are namespaced (provider/model) — copy exactly.
- [ ] Watch per-model pricing before defaulting to an expensive one.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| 402 | credits exhausted | top up / route elsewhere |
| Wrong model | missing provider prefix | use full "vendor/model" ID |

## New terms → glossary
- Model routing / aggregator
