# Nginx / reverse proxy — reference

**In plain English:** The receptionist for your server. It takes incoming web
requests and sends each one to the right app inside.

## What it is used for here
Routing your domains to the correct container; handling HTTPS certificates.

## Where its settings live
- Site config files (per domain) + a certificates store.
- Back these up before ANY edit — a typo can take all sites offline.

## Safe-change checklist
- Test config BEFORE reload: `nginx -t` (this is a dry-run).
- Reload, don't restart, when possible (no downtime).

## Common problems
| Symptom | What it usually means |
|---------|-----------------------|
| 502 Bad Gateway | The app behind the proxy is down. |
| cert expired warning | Auto-renewal failed — check the renewal timer. |

## New terms → add to references/glossary.md
reverse proxy, HTTPS, certificate, 502
