# 🛡️ infra-guardian

**A calm helper that watches over your self-hosted setup so you don't have to be a sysadmin.**

You're building things — websites, AI tools, a CRM — but you're not a
coder, and one wrong click can break something you can't fix. infra-guardian
is the safety net. It keeps an eye on your servers and services, tells you in
plain English what's going on, and *never* changes anything without backing it
up and asking you first.

---

## Is this skill right for you?

✅ **Yes, if you...**
- self-host apps (WordPress, a CRM, AI chat tools) but don't write code
- get nervous touching servers, DNS, or config files
- want a plain-English explanation *before* anything changes
- have broken something once and want that to never happen again

❌ **Maybe not, if you...**
- are an experienced sysadmin who wants full manual control
- prefer editing servers directly with no guardrails

---

## What it actually does for you

- 👀 **Watches** — checks your services are alive and healthy.
- 🗣️ **Explains** — no jargon; if it uses a new word, it adds it to a glossary.
- 💾 **Backs up first** — always saves a copy before touching anything.
- 🙋 **Asks first** — proposes a change, waits for your "yes." One thing at a time.
- 🚫 **Won't nag** — say "no" once and it won't keep re-asking the same thing.
- 📚 **Learns your stack** — keeps simple notes on every tool you use.

---

## The one promise (the safety rule)

> **Back up → preview → ask → change one thing → write it down.**

It never makes a big pile of changes at once, and it never changes something
without a saved backup to undo it. That's the whole philosophy.

---

## Getting started (no coding needed)

1. **Copy the two template files** (your computer does the work):
   - `.env.example` → `.env`
   - `guardian.config.EXAMPLE.yaml` → `guardian.config.yaml`
2. **Leave the secret file (`.env`) as-is for now.** It's full of
   `<placeholders>`. That's on purpose and 100% safe — nothing runs off it
   until *you* choose to add a key. (See "About your secret keys" below.)
3. That's it. The guardian can start watching.

---

## About your secret keys 🔑

Some optional features (like phone/Telegram alerts or live AI models) need a
"key" — a password-like code from another service.

- **You do NOT have to add any keys to use the basics.**
- Keys live only in the `.env` file, which is **hidden and never uploaded**.
- If you'd rather not put keys in a file at all, you can paste them into your
  hosting panel's "secrets" section instead — even safer.
- Good habit: refresh (regenerate) your keys now and then.

---

## What's inside (your reference library)

Plain-English notes are kept for everything you run, so you never have to
google from scratch:

- **Providers** — hosting, domain registrar, DNS
- **AI models** — Mistral, NVIDIA, Groq, Cerebras, OpenRouter, Gemini
- **Self-hosted apps** — Twenty CRM, Uptime Kuma, Dozzle, Camoufox,
  Open WebUI, LibreChat, New API, OpenClaw, OpenHuman, Goose, Hermes Agent
- **WordPress plugins** — ACF, Rank Math Pro, Tutor LMS Pro, Gutenberg,
  Code Snippets Pro, LiteSpeed Cache, Directorist Pro, Aimogen Pro
- **Glossary** — every tech word explained in one line

---
---

## 🔧 For developers (technical detail)

### Layout
- `SKILL.md` — operating rules (canonical, v0.2)
- `basic.py`, `doctor.py`, `infra-status-check.py` — scripts
- `.env.example` / `guardian.config.EXAMPLE.yaml` — safe templates (committed)
- `.env` / `guardian.config.yaml` — real, secret-bearing (gitignored)
- `references/` — `concepts/`, `providers/`, `models/`, `selfhosted/`,
  `wordpress/plugins/`
- `glossary.md` — append-only term bank

### Setup
1. `cp .env.example .env` and fill real tokens locally (never commit).
2. `cp guardian.config.EXAMPLE.yaml guardian.config.yaml` and adjust.
3. Both real files are gitignored — verify with `git status` before pushing.

### Safety model
Every action: backup → checksum → dry-run → one change → log. Proposals honour
`behaviour.no_renagging` (won't re-nag a declined item until status changes).
