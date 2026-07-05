# Langfuse

**In one line:** An open-source dashboard that records what your AI apps
are doing — every prompt, response, cost, and error — so you can debug and
improve them.

## What it's for
- **Tracing:** See the full step-by-step of an LLM call (input → model →
  output), including chained/agent steps.
- **Cost tracking:** Tallies token usage and dollar cost per call, user, or feature.
- **Evaluation:** Score outputs (manually or automatically) to catch quality drops.
- **Prompt management:** Store and version prompts outside your code.

## How it fits your stack
- Sits *alongside* your apps (LibreChat, n8n, Goose). They send data to it.
- Self-hosted via Docker; needs a Postgres database.
- You connect apps with a **public key** + **secret key** (kept in `.env`).

## Key facts
- License: open-source (MIT core).
- Self-host: `docker compose` — includes web UI + worker + Postgres.
- Default port: `3000`.
- SDKs: Python, JS/TS; also OpenAI drop-in wrapper and OpenTelemetry.

## Watch out for
- The database grows fast under heavy tracing — plan storage/retention.
- Keep the secret key out of git (it's in `.gitignore` already).

## New glossary terms
| Term | In plain English |
|------|------------------|
| trace | A recorded timeline of one AI request from start to finish. |
| observability | Being able to see what software is doing internally, after the fact. |
| token usage | How many word-pieces an AI read and wrote — what you get billed on. |
