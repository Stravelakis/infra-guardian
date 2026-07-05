# Mistral (mistral.ai)

## In plain English
A European LLM provider. You hand it a prompt over an API, it hands back text.

## What it's used for
Chat/completion + embeddings backend for the app layer (Open WebUI, LibreChat,
new-api routing).

## Where settings live
- API base: https://api.mistral.ai/v1
- Key: MISTRAL_API_KEY in .env (placeholder only — Rule: never real tokens)
- Model IDs referenced in guardian.config.yaml under model_providers.mistral

## Safe-change checklist
- [ ] Dry-run: hit /v1/models before switching a live model ID.
- [ ] One provider change at a time.
- [ ] Backup guardian.config.yaml before editing the mistral block.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| 401 | key missing/placeholder still in .env | check .env, don't paste key in logs |
| 429 | rate limit | back off, check tier |
| Unknown model | model ID renamed/retired | GET /v1/models, update ID |

## New terms → glossary
- (append: "OpenAI-compatible endpoint" if not already present)
