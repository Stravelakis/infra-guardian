# Browserbase

**In one line:** A cloud service that runs real web browsers for your AI —
so your agents can click, scroll, and read websites without you hosting
browsers yourself.

## What it's for
- Give AI agents a real browser to do tasks (fill forms, scrape, log in).
- Run many browser sessions in parallel, in the cloud.
- Handle the annoying parts: stealth/anti-bot, captchas, proxies.

## How it fits your stack
- An alternative to self-hosting browsers (see `selfhosted/camoufox.md`).
- Pairs with agent frameworks and its own **Stagehand** library for
  AI-driven browser control.
- Connect via an **API key** + **project ID** in `.env`.

## Key facts
- Hosted (not self-hosted) — you pay per browser session/usage.
- Auth: API key + project ID.
- Companion tool: Stagehand (natural-language browser automation).
- Supports live session viewing and recordings for debugging.

## Watch out for
- It's a paid, usage-based service — costs scale with session time.
- Since it's external, don't send it secrets you wouldn't share with a vendor.

## New glossary terms
| Term | In plain English |
|------|------------------|
| headless browser | A web browser with no visible window, driven by code. |
| scraping | Automatically reading data off web pages. |
| captcha | The "prove you're human" puzzle sites use to block bots. |
