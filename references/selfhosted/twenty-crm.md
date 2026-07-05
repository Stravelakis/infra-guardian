# Twenty (CRM)

## In plain English
Twenty is an open-source CRM — a self-hostable alternative to tools like
Salesforce for tracking companies, people, and deals. [[twenty.com]]

## What it's used for
Contacts, pipelines, and customizable objects, self-hosted so your customer
data stays yours.

## Where settings live
- App settings UI + env vars (server URL, secrets, storage).
- Postgres + Redis volumes hold the data.

## Safe-change checklist
- [ ] Backup Postgres before upgrades/migrations.
- [ ] Set a strong APP_SECRET; keep it in .env.
- [ ] Test object/schema changes on a copy first.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Won't start | Missing SERVER_URL/secret | Check required env vars |
| Data gone after update | Volume not persisted | Verify Postgres volume |
| Login/CORS errors | Wrong SERVER_URL | Match URL to how you access it |

## New terms → glossary
CRM, pipeline, Postgres, Redis
