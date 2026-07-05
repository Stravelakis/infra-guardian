# Uptime Kuma

## In plain English
A self-hosted "is my stuff up?" monitor with a clean dashboard — pings your
sites/services and alerts you when something goes down.

## What it's used for
HTTP/TCP/ping/keyword monitors, status pages, and notifications (Telegram,
email, webhooks) — pairs naturally with this guardian's Telegram block.

## Where settings live
- In-app UI (Settings, Monitors, Notifications).
- Data in its volume (SQLite/DB). Container config in your compose file.

## Safe-change checklist
- [ ] Backup its data volume before upgrades.
- [ ] Add one monitor, confirm it alerts, then add more.
- [ ] Store notification tokens as secrets, not in plain compose.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| False "down" alerts | Interval/timeout too tight | Loosen check interval |
| No notifications | Bad token/chat ID | Re-test notification in UI |
| Dashboard blank after update | Volume not mounted | Verify volume path |

## New terms → glossary
uptime monitor, status page, webhook
