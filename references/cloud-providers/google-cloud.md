# Google Cloud — API access

**What it is:** Google's cloud platform. In this stack it's used purely as
an **API provider** — not for hosting VMs. It gives access to a large
catalogue of Google APIs (Weather, YouTube Data, Maps, Translate, etc.)
through a single project + key.

Google Cloud offers cloud computing, hosting services, and APIs, with
$300 in free credits and 20+ always-free products for new accounts [[7]].

## What we use it for
- **Weather API** — forecast / current conditions lookups.
- **YouTube Data API** — video metadata, search, channel stats.
- (Room to add: Maps, Translate, Vision, etc.)

## Setup checklist
1. Create/select a project in the Google Cloud Console.
2. **Enable** each API you need (APIs & Services → Library).
3. Create credentials → **API key** (restrict it to only the APIs above).
4. Store the key in `.env` — never commit it.

## .env keys
| Key | Purpose |
|-----|---------|
| `GOOGLE_CLOUD_API_KEY` | Shared key for enabled Google APIs |
| `YOUTUBE_API_KEY`      | (Optional) separate key scoped to YouTube Data |

## Gotchas
- Each API has its **own quota** — enabling one doesn't lift limits on another.
- Restrict keys by API **and** by referrer/IP where possible.
- YouTube Data API burns quota fast (search = 100 units/call).
