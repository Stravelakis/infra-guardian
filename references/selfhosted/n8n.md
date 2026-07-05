# n8n

**In one line:** A visual automation tool — you drag boxes ("nodes") and
connect them to make apps talk to each other, no code required.

## What it's for
- Connect services: "When X happens in app A, do Y in app B."
- Build AI workflows: webhook → call an LLM → post the result to Slack/WordPress.
- Schedule jobs (like cron, but visual).

## How it fits your stack
- Self-hosted, so your data and API keys stay on your own server.
- Talks to almost anything with an API — including your LLM providers,
  Twenty CRM, and WordPress.
- Often paired with Langfuse (to trace AI steps) and a reverse proxy
  (Nginx Proxy Manager / Cloudflare Tunnel) for safe public access.

## Key facts
- License: "fair-code" (Sustainable Use License) — free to self-host,
  restrictions on reselling it as a service.
- Self-host: Docker; default port `5678`.
- Needs a database for anything serious — Postgres recommended over the
  default SQLite in production.
- Set `N8N_ENCRYPTION_KEY` so stored credentials survive restarts.

## Watch out for
- Exposing it to the internet without a login is dangerous — it can run code.
- Always put it behind auth + HTTPS.

## New glossary terms
| Term | In plain English |
|------|------------------|
| node | A single step/box in an automation workflow. |
| webhook | A URL that other apps call to trigger your workflow. |
| cron | A time-based scheduler ("run every day at 3am"). |
