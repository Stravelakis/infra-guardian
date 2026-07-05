# Open WebUI

## In plain English
A self-hosted chat interface for LLMs — connects to Ollama and/or any
OpenAI-compatible API and gives you a ChatGPT-like UI you control.

## What it's used for
Running local + hosted models behind one UI, with users, RAG, and model config.

## Where settings live
- Admin panel (users, models, connections).
- Env vars + its data volume (users, chats). API keys stored server-side.

## Safe-change checklist
- [ ] Backup the data volume before upgrades (users/chats live there).
- [ ] Keep provider API keys in .env, not baked into compose.
- [ ] Lock down signup (disable open registration) if internet-facing.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| No models listed | Backend URL wrong | Check Ollama/API connection |
| Can't log in after update | Volume/secret changed | Verify WEBUI_SECRET + volume |
| 401 from provider | Bad API key | Re-check key in connections |

## New terms → glossary
OpenAI-compatible API, RAG, Ollama
