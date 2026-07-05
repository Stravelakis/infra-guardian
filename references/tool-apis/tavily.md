# Tavily — search API

**What it is:** A search API designed specifically for LLMs and agents.
Returns concise, ranked, answer-ready results with optional source content.

## What we use it for
- Fast factual lookups and live web context for the agent.
- "Search then summarize" flows where you want tidy inputs.

## Setup
- Account: already created (dashboard holds usage + billing).
- Auth: **API key** in `.env`.

## .env keys
| Key | Purpose |
|-----|---------|
| `TAVILY_API_KEY` | Authenticates search calls |

## Gotchas
- Metered per call — check the free-tier limit before heavy loops.
- Overlaps with Exa; keep a note of which one each script uses so you
  don't double-spend quota.
