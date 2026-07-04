# Portainer — reference

**In plain English:** A web dashboard for seeing and controlling all your
Docker containers with clicks instead of typed commands.

## What it is used for here
The visual front door to everything Docker is running.

## Where its settings live
- Runs as its own container; data in a Docker volume `portainer_data`.
- Login/admin password set on first launch — store it in your password manager.

## Safe-change checklist
- Back up the `portainer_data` volume before upgrades (auto).
- Note the current image tag before pulling a new one (rollback path).

## Common problems
| Symptom | What it usually means |
|---------|-----------------------|
| can't reach the dashboard | Container down, or wrong port in the browser. |
| lost admin password | Reset via the recovery container procedure. |

## New terms → add to references/glossary.md
volume, dashboard, image tag
