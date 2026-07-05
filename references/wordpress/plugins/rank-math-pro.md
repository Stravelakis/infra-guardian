# Rank Math Pro

## In plain English
The paid tier of Rank Math, a WordPress SEO plugin that combines many SEO tools
into one and uses AI-powered features to help pages rank in modern/AI search. [[4]] [[9]]

## What it's used for
On-page SEO scoring, schema/rich snippets, sitemaps, redirections, and
analytics integration; Pro adds advanced schema, keyword tracking, and bulk tools.

## Where settings live
- WP Admin → Rank Math SEO → General / Titles & Meta / Sitemap.
- License/activation under Rank Math → Help/Account.

## Safe-change checklist
- [ ] Backup DB before changing sitemap or redirect rules (they alter live URLs).
- [ ] Dry-run schema changes on one post type first.
- [ ] One setting group at a time; re-check Search Console after.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Sitemap 404 | Permalinks/cache | Flush permalinks, purge cache |
| Duplicate meta | Theme also outputs SEO tags | Disable theme SEO, keep Rank Math |
| License inactive | Token/domain mismatch | Re-check account, not .env |

## New terms → glossary
schema markup, canonical URL, sitemap
