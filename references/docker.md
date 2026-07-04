# Docker — reference

**In plain English:** Docker runs software inside sealed boxes ("containers")
so it can't mess up the rest of your system, and so it runs the same
everywhere.

## What it is used for here
Running most of your self-hosted apps (Portainer, n8n, etc.) as containers.

## Where its settings live
- Compose files: `docker-compose.yml` per project.
- Secrets: never in the compose file — reference `.env`.

## Safe-change checklist (this skill enforces)
- Backup the compose file + `.env` before editing (auto).
- `docker compose config` to validate BEFORE applying (a dry-run).
- `docker compose up -d` to apply; `docker compose logs -f` to watch.

## Common problems (plain English)
| Symptom | What it usually means |
|---------|-----------------------|
| "port already allocated" | Another container is using that door number. |
| container keeps restarting | The app inside is crashing on startup — check logs. |

## New terms → add to references/glossary.md
container, image, compose, volume
