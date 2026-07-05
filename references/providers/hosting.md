# Hosting Provider

## In plain English
This is the company that runs the actual machine (VPS, dedicated box, or
cloud instance) your stack lives on. If the server exists somewhere other
than your own home/office, this is who you rent it from.

## What it's used for
- Provisioning and powering the server (CPU/RAM/disk).
- Console/root access, reboots, rescue mode.
- Firewall rules at the provider edge, snapshots, backups-of-last-resort.
- Bandwidth and the public IP(s) your services answer on.

## Where settings live
- Provider control panel (login URL recorded in `.env` as a NON-secret note;
  credentials NEVER stored here — placeholders only).
- Server-side: `/etc/`, cloud-init/user-data, provider metadata endpoint.
- Snapshot/backup schedule: provider dashboard, not the guardian.

## Safe-change checklist (guardian discipline)
1. BACK UP FIRST: take a provider snapshot AND note its ID.
2. CHECKSUM: record current IP, open ports, and running services.
3. DRY-RUN: describe the change in plain English before touching anything.
4. ONE CHANGE AT A TIME: never resize + reconfigure firewall together.
5. LOG IT: what changed, snapshot ID, timestamp, rollback step.
6. Confirm reachability AFTER (SSH + one live service) before closing.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Can't SSH after change | Provider firewall or new IP | Use provider web console, check edge firewall |
| Server "gone" | Failed resize / suspended acct | Check billing + snapshot list before rebuilding |
| Wrong public IP | Floating/elastic IP detached | Reattach in panel; don't edit DNS yet |
| Slow / throttled | Bandwidth cap hit | Check usage graph; don't restart blindly |

## New terms → glossary
- snapshot, floating IP / elastic IP, rescue mode, cloud-init, metadata endpoint
  (append to `glossary.md` only if not already present — do NOT recreate glossary).

# Hosting providers & control panels

Three environments, three control panels. Same idea in each: a web GUI
that manages the web server so you don't touch the command line.

| Panel   | Provider       | Role in stack        |
|---------|----------------|----------------------|
| aaPanel | Self-hosted    | Our own server(s)    |
| cPanel  | AsuraHosting   | Managed shared/VPS   |
| hPanel  | Hostinger      | Managed hosting      |

## aaPanel (self-hosted)
Simple but powerful **open-source** web hosting control panel that manages
the web server through a web-based GUI [[5]]. Free and a common
open-source alternative to cPanel [[1]].
- **Min specs:** 1 core CPU, 512 MB RAM (768 MB+ recommended), the pure
  panel uses ~60 MB [[3]].
- Use for: the servers we own and administer directly.

## cPanel — AsuraHosting
- Managed hosting; cPanel is the industry-standard commercial panel.
- Use for: sites hosted on AsuraHosting.
- Access: provider dashboard → cPanel login.

## hPanel — Hostinger
- Hostinger's own custom panel (not cPanel).
- Use for: sites hosted on Hostinger.
- Access: Hostinger account → hPanel.

## Rule of thumb
- **Self-managed / full control →** aaPanel.
- **Managed convenience →** cPanel (AsuraHosting) or hPanel (Hostinger).
