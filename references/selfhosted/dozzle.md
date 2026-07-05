# Dozzle

## In plain English
A lightweight web UI for viewing your Docker container logs in real time — no
database, no persistence, just a live tail in the browser.

## What it's used for
Quick log inspection across containers during debugging.

## Where settings live
- Environment variables on its container (e.g. auth, filters).
- Reads the Docker socket (read-only mount recommended).

## Safe-change checklist
- [ ] Mount the Docker socket READ-ONLY (:ro).
- [ ] Put it behind auth / reverse proxy — logs can leak secrets.
- [ ] Never expose it publicly without protection.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| No containers shown | Socket not mounted | Check /var/run/docker.sock mount |
| Access from anywhere | No auth | Add auth / proxy restriction |
| Logs truncated | It's live-only by design | Use real log driver for history |

## New terms → glossary
Docker socket, log tail, reverse proxy
