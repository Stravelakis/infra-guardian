# LiteSpeed Cache

## In plain English
A caching + site-speed plugin. Works best on LiteSpeed/OpenLiteSpeed servers
but also offers browser/object caching, image optimization, and CDN options.

## What it's used for
Page caching, minify/combine CSS-JS, image optimization, and QUIC.cloud CDN.

## Where settings live
- WP Admin → LiteSpeed Cache → Cache / Optimization / CDN.
- Server-side rules may live in .htaccess or the LiteSpeed config.

## Safe-change checklist
- [ ] Backup before enabling CSS/JS combine or lazy-load (can break layout).
- [ ] Enable one optimization at a time, then purge + test front-end.
- [ ] Keep a "safe" preset noted so you can revert.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Broken layout after optimize | CSS/JS combine | Disable combine, keep cache |
| Stale content shown | Aggressive cache | Purge all, exclude dynamic pages |
| Login/cart glitches | Cached logged-in pages | Exclude those URLs from cache |

## New terms → glossary
page cache, minify, CDN, TTL
