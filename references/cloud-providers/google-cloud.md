# Google Cloud — API access

**What it is:** Google's cloud platform, used here purely as an **API
provider** — not for hosting VMs. One project + key (or per-API keys) gives
access to a large catalogue of Google APIs.

Google Cloud offers cloud computing, hosting services, and APIs, with
$300 in free credits and 20+ always-free products for new accounts.

**Important distinction:** "enabled" ≠ "used." A Google Cloud project
enables dozens of APIs by default or in a batch when you turn on one
related service. The table below reflects everything currently *enabled*
on this account; only one — **Gemini for Google Cloud API** — shows real
traffic (855 requests logged). Treat the rest as "available if needed,"
not "part of the active stack." Update this file when a category moves
from enabled-but-idle to actually used.

## By category

### AI / Gemini
| API | Status |
|---|---|
| Gemini for Google Cloud API | **Active use** (855 requests) — see also `cloud-providers/gemini-vertex.md` for the Vertex-specific access path |
| Gemini Cloud Assist API | Enabled, idle |
| Agent Platform API / Agent Registry API | Enabled, idle |
| Model Armor API | Enabled, idle — AI safety/guardrails product |
| Notebooks API | Enabled, idle — Vertex AI Workbench notebooks |

### Maps Platform (large block, all idle)
Address Validation, Aerial View, Air Quality, Directions, Distance Matrix,
Geocoding, Geolocation, Map Management, Map Tiles, Maps 3D SDK
(Android/iOS), Maps Elevation, Maps Embed, Maps Grounding Lite, Maps
JavaScript, Maps Platform Datasets, Maps SDK (Android/iOS), Maps Static,
Places API (+ New, Aggregate, UI Kit), Pollen, Roads, Route Optimization,
Routes, Solar, Street View (Publish + Static), Time Zone, Weather.

**Note:** the Skilitsa stack uses **OpenStreetMap + Leaflet.js + Nominatim**
for maps/geocoding, not Google Maps — so this whole block is currently
enabled-but-unused overhead. Worth a look at whether it's costing anything
or just sitting there; Maps Platform APIs generally don't charge until
called.

### Workspace / productivity
CalDAV, Google Calendar, Google Chat, Google Classroom, Google Docs,
Google Drive (+ Drive Activity), Google Forms, Google Keep, Google Meet,
Google Sheets, Google Slides, Google Tasks, Google Workspace add-ons,
People API, Gmail API.

**Relevant today:** Google Sheets + Drive — the Skilitsa master data sheet
(`1p0_25dN1XPkiYeeyYvGNafN8dtC74_nCVqQARxm5PLg`) lives here. The rest are
enabled but idle.

### Data / analytics
BigQuery (+ Connection, Data Policy, Data Transfer, Migration,
Reservation, Storage APIs), Analytics Hub, Google Analytics API + Data
API, Dataform, Cloud Dataplex, Cloud Datastore. All idle — no current
project uses BigQuery or GA.

### Infra / compute / storage
Compute Engine, Cloud SQL, Cloud Storage (+ API, JSON API), Cloud
Deployment Manager V2, App Hub / App Lifecycle Manager / App Optimize /
App Topology, Network Security, Network Services, Global Edge Cache
Service, Design Center. All idle — actual hosting/compute for this stack
runs elsewhere (self-hosted / non-Google hosting per `providers/hosting.md`).

### Identity / security / ops
IAM (+ Connector Credentials, Connectors, Service Account Credentials),
Cloud Identity-Aware Proxy, Cloud OS Login, Security Center Management,
Security Command Center, Cloud Logging, Cloud Monitoring, Cloud Trace,
Observability, Telemetry, Recommender, Cloud Asset, Cloud API Registry,
Service Management, Service Usage. These are largely platform-plumbing
APIs that get enabled automatically as dependencies of other services —
not typically something to configure directly.

### Firebase
Firebase Extensions, Firebase Hosting, Firebase Management. Enabled,
idle — no current project uses Firebase.

### Search / web
PageSpeed Insights, Google Search Console, Web Search Indexing, Web
Fonts Developer, Chrome Web Store API. Search Console is worth watching
if/when SEO reporting is automated for skilitsa.com.

### YouTube
YouTube Analytics, YouTube Data API v3, YouTube Embedded Player, YouTube
Reporting. **YouTube Data API v3 is the one in active use** — BlankStare's
doc-link/video search feature relies on it.

### Misc
Cloud Search API, Cloud Text-to-Speech API — enabled, idle.

## Setup checklist
1. Create/select a project in the Google Cloud Console.
2. **Enable** each API you actually intend to use (APIs & Services → Library) — don't assume "enabled" means "safe to rely on," check quota/cost pages per API.
3. Create credentials → **API key**, restricted to only the APIs you use.
4. Store the key in `.env` — never commit it (see `concepts/secrets.md`).

## .env keys
| Key | Purpose |
|-----|---------|
| `GOOGLE_CLOUD_API_KEY` | Shared key for enabled Google APIs |
| `YOUTUBE_API_KEY` | (Optional) separate key scoped to YouTube Data — active use in BlankStare |

## Gotchas
- Each API has its **own quota** — enabling one doesn't lift limits on another.
- Restrict keys by API **and** by referrer/IP where possible.
- YouTube Data API burns quota fast (search = 100 units/call).
- A long enabled-but-idle list (like the Maps Platform block above) is
  normal after using the Cloud Console UI, which enables related APIs in
  batches — it's not a sign of misconfiguration, just noise to filter out
  when reading "what's actually in use."
