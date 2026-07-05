# Cloudflare Tunnel

## In plain English
A secure "pipe" that connects a service running on my machine to the
internet through Cloudflare — without opening any ports or exposing my
real IP address. Great for reaching self-hosted apps safely.

## Where I use it
- Exposing self-hosted apps (Open WebUI, n8n, etc.) behind a domain
- Reaching home/lab services without a public IP

## Good to know
- Runs a small program called `cloudflared` as a background daemon.
- Traffic is encrypted and hidden behind Cloudflare's network.
- No inbound firewall holes needed — the tunnel dials outward.

## Related
- `references/providers/dns.md`
- `references/infra/tailscale.md`
