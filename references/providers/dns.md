# DNS provider

## In plain English
DNS is the internet's phone book. When someone types your domain, DNS is what
turns that name into the actual server address so the browser knows where to go.
Your DNS provider is whoever holds those records — sometimes your registrar,
sometimes a separate service (e.g. Cloudflare) you point the domain at.

## What it's used for
- Pointing a domain (and its subdomains) at this server's IP (A / AAAA records).
- Mail routing (MX), verification (TXT), and aliases (CNAME).
- Proxy / CDN / DDoS protection when the DNS provider also fronts traffic.

## Where settings live
- Provider dashboard → DNS / Zone editor (the record table).
- The domain's **nameservers** decide *which* provider is authoritative — check
  these at the registrar (see providers/domain-registrar.md).
- No DNS secrets belong in this repo. Any API token for automated record edits
  goes in `.env` as a placeholder only.

## Safe-change checklist (guardian discipline)
1. Snapshot the full current zone (export/screenshot) BEFORE editing — this is
   your backup, since DNS has no built-in undo.
2. Change ONE record at a time (Rule 5).
3. Note the record's TTL: a change won't fully propagate until the old TTL expires.
4. Verify with `dig <name>` / `nslookup` from an outside network, not just locally.
5. Never delete NS or MX records "to tidy up" — confirm what each does first.

## Common problems
| Symptom | Likely cause | First safe check |
|---|---|---|
| Domain still points to old server | TTL not expired / cache | `dig +trace`, wait out the old TTL |
| Site works, email dies | MX or SPF/TXT changed | Re-check MX + SPF against a saved snapshot |
| "DNS not authoritative" | Nameservers still at old provider | Fix nameservers at the registrar |
| HTTPS breaks after DNS move | Proxy/SSL mode toggled | Match SSL mode to how the origin serves TLS |

## New terms → glossary
- **DNS**, **A record**, **CNAME**, **MX**, **TXT**, **TTL**, **nameserver**,
  **zone**, **propagation**
