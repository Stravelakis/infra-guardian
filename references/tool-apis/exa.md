# Exa — search API

**What it is:** A search API built for AI/agents — returns clean,
content-rich results (not just links) meant to be fed straight to an LLM.

## What we use it for
- Semantic / neural web search where relevance matters more than keywords.
- Pulling page contents alongside results (fewer follow-up fetches).

## Setup
- Account: already created (dashboard holds usage + billing).
- Auth: **API key** in `.env`.

## .env keys
| Key | Purpose |
|-----|---------|
| `EXA_API_KEY` | Authenticates search + contents calls |

## Gotchas
- Usage is metered per request — watch the dashboard quota.
- Great for research/discovery; pair with a scraper for full-page detail.
