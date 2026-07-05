# Google Gemini (ai.google.dev)

## In plain English
Google's LLM family. Native API differs slightly; also has an OpenAI-compat shim.

## What it's used for
Chat, long-context, multimodal backend option.

## Where settings live
- Native base: https://generativelanguage.googleapis.com
- OpenAI-compat base: https://generativelanguage.googleapis.com/v1beta/openai
- Key: GEMINI_API_KEY (.env, placeholder)
- guardian.config.yaml → model_providers.gemini

## Safe-change checklist
- [ ] Decide native vs OpenAI-compat path and keep it consistent per app.
- [ ] Verify model ID (e.g. version suffixes change).

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| 403 | key/region restriction | check .env + project access |
| 404 model | version retired | list models, update ID |

## New terms → glossary
- OpenAI-compatible shim

## See also
This is the free AI Studio key path. For Gemini accessed through Google
Cloud/Vertex (billing, quotas, IAM controls), see
`cloud-providers/gemini-vertex.md` instead.
