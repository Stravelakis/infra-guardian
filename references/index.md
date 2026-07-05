# References — Index

**Read this file first.** It routes a question to the one (or few) files
that actually answer it. Don't load the whole `references/` tree to answer
a single question — open only what's listed below.

Each entry: `path — one-line description`.

---

## cloud-providers/
- `cloud-providers/google-cloud.md` — Full enabled-API surface (100+ APIs across Maps, Workspace, BigQuery, Firebase, IAM, YouTube, etc.), categorized with active-vs-idle status — not general GCP compute/hosting.
- `cloud-providers/gemini-vertex.md` — Gemini accessed through Google Cloud/Vertex, with billing and quota controls (separate from the free AI Studio key in `models/gemini.md`).

## concepts/
- `concepts/backups.md` — The backup discipline itself: why an unverified backup isn't a backup, and what "tested" means.
- `concepts/secrets.md` — Where API keys/tokens live (`.env` only), pre-push checklist, key-rotation discipline.

## infra/ (server-level infrastructure)
- `infra/aapanel.md` — Free web control panel for managing a Linux server.
- `infra/cloudflare-tunnel.md` — Exposes a local/self-hosted service to the internet without opening ports.
- `infra/docker.md` — Containers: isolating and running apps consistently.
- `infra/nginx.md` — Reverse proxy: routes incoming requests to the right app.
- `infra/portainer.md` — Web UI for managing Docker containers by click instead of command line.
- `infra/searxng.md` — Self-hosted metasearch engine (privacy-respecting, aggregates other search engines).
- `infra/tailscale.md` — Zero-config VPN connecting your devices into one private network.

## models/ (LLM providers — free-tier focus)
- `models/llm-providers.md` — **Start here.** Cheat-sheet comparing all providers below.
- `models/groq.md` — Very fast inference, OpenAI-compatible API, generous free tier.
- `models/gemini.md` — Google's LLM family via the free AI Studio key.
- `models/mistral.md` — European provider, free "La Plateforme" tier.
- `models/cerebras.md` — High-speed inference, OpenAI-compatible, free tier.
- `models/nvidia.md` — Hosted open models via NIM microservices, credit-based free tier.
- `models/openrouter.md` — One key routing to many providers; some models tagged free.

## providers/ (who runs your domain/hosting)
- `providers/hosting.md` — The company running your actual server (VPS/dedicated/shared).
- `providers/domain-registrar.md` — Who you bought the domain name from.
- `providers/dns.md` — How your domain name resolves to a server (the internet's phone book).

## selfhosted/ (apps you run yourself)
- `selfhosted/hermes-agent.md` — Nous Research's AI agent; part of the active agent-tooling setup.
- `selfhosted/openclaw.md` — Open-source AI agent framework.
- `selfhosted/openhuman.md` — AI agent, same family as OpenClaw (tinyhumans.ai).
- `selfhosted/goose.md` — Open-source AI agent that can act directly on your machine.
- `selfhosted/open-webui.md` — Self-hosted chat UI for LLMs (Ollama and API-based models).
- `selfhosted/librechat.md` — Self-hosted multi-provider AI chat platform.
- `selfhosted/new-api.md` — Self-hosted LLM API gateway/management layer.
- `selfhosted/langfuse.md` — Traces and debugs AI workflow steps (prompts, cost, errors).
- `selfhosted/n8n.md` — Visual no-code automation; connects apps and AI workflows.
- `selfhosted/twenty-crm.md` — Self-hosted open-source CRM.
- `selfhosted/uptime-kuma.md` — "Is my stuff up?" monitoring dashboard.
- `selfhosted/dozzle.md` — Real-time web viewer for Docker container logs.
- `selfhosted/camoufox.md` — Stealth/anti-detect Firefox build for browser automation.
- `selfhosted/github-desktop.md` — GitHub Desktop app + Codespaces workflow notes.

## tool-apis/ (hosted APIs used by agents/tools)
- `tool-apis/exa.md` — Search API.
- `tool-apis/tavily.md` — Search API.
- `tool-apis/parallel.md` — Live web search returning source-backed answers for agents.
- `tool-apis/browserbase.md` — Hosted browser infrastructure for agents (click/scroll/read without self-hosting a browser).
- No head-to-head comparison file exists yet for exa/tavily/parallel — Hermes Agent currently uses SearXNG (self-hosted, `infra/searxng.md`) for search and Firecrawl for extraction, so these three are alternatives/backups rather than the active path. Worth a `llm-providers.md`-style cheat sheet if usage grows.

## wordpress/
- `wordpress/wordpress.md` — WordPress core basics.
- `wordpress/database.md` — The MySQL/MariaDB database behind a WP site.
- `wordpress/plugins.md` — Plugins/themes in general — also the #1 source of breakage.
- `wordpress/_hosting.md` — Where your WP sites physically live (hosting specifics for WP).
- `wordpress/plugins/acf.md` — Advanced Custom Fields — custom data fields on posts/pages/users.
- `wordpress/plugins/gutenberg.md` — The built-in block editor.
- `wordpress/plugins/code-snippets-pro.md` — Add small PHP/JS/CSS snippets safely, without editing theme files.
- `wordpress/plugins/rank-math-pro.md` — SEO plugin (paid tier).
- `wordpress/plugins/litespeed-cache.md` — Caching + speed plugin (best on LiteSpeed servers).
- `wordpress/plugins/tutor-lms-pro.md` — Turns WordPress into a course/LMS platform (paid tier).
- `wordpress/plugins/directorist-pro.md` — Directory/listing site builder (paid tier).
- `wordpress/plugins/aimogen-pro.md` — All-in-one AI content writer/editor/chatbot plugin.

## Other
- `glossary.md` — Every jargon term used across all files above, in one line each. Append new terms here when writing a new reference file — never rewrite existing entries.
- `../SKILL.md` — Lives one level up (repo root, not under `references/`). Has the safety rules and the workflow this index supports.

---

**Adding a new file?** Put it in the right domain folder above, follow the
standard shape (see `SKILL.md` → "Navigating the reference library"), then
add one line to this index and any new terms to `glossary.md`.
