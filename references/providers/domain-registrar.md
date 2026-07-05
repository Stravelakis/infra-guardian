# Domain Registrar

## In plain English
This is who you bought the domain name from. They own the "lease" on the name
itself (e.g. example.com) and control who the world asks for its DNS.

## What it's used for
- Registering / renewing the domain (expiry = highest-risk item here).
- Setting the AUTHORITATIVE NAMESERVERS (points the world at your DNS host).
- Registrar lock, WHOIS/privacy, transfer auth (EPP) codes.

## Where settings live
- Registrar control panel (login URL as NON-secret note in `.env`).
- Two things live here and ONLY here: nameserver delegation + renewal.
- Actual DNS records usually live at the DNS host (see dns.md), NOT here.

## Safe-change checklist (guardian discipline)
1. BACK UP FIRST: export/screenshot current nameservers + expiry date.
2. CHECKSUM: record current NS values and registrar-lock state.
3. DRY-RUN: nameserver changes propagate slowly and break email/web if wrong —
   describe blast radius before acting.
4. ONE CHANGE AT A TIME: change NS OR toggle lock, never both.
5. LOG IT: old NS, new NS, timestamp.
6. Keep auto-renew ON unless deliberately retiring the domain.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Whole site down worldwide | Domain expired | Check expiry FIRST; renew before debugging anything |
| DNS changes have no effect | Editing records at wrong place | Confirm which NS the domain delegates to |
| Can't transfer domain | Registrar lock on / no EPP code | Unlock + fetch auth code (60-day post-reg limits apply) |
| Email + web both dead | Nameservers changed wrongly | Revert NS to previous recorded values |

## New terms → glossary
- registrar, authoritative nameserver, delegation, registrar lock, EPP/auth code,
  WHOIS privacy (append only).
