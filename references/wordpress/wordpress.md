# WordPress — reference

**In plain English:** The software that runs your website's pages, posts,
and admin area. Most of the web's sites use it.

## What it is used for here
Your public-facing site(s), served through Nginx, backed by a database.

## Where its settings live
- `wp-config.php` — the master settings + secret keys (back up before edits).
- Content + uploads in the site folder; everything else in the database.

## Safe-change checklist
- Back up BOTH files and database before any update (auto).
- Update on a staging copy first when the change is big.

## Common problems
| Symptom | What it usually means |
|---------|-----------------------|
| white screen of death | A plugin or theme crashed the site — disable it. |
| "error establishing DB connection" | The database is down or wp-config is wrong. |

## New terms → add to references/glossary.md
wp-config, staging, plugin, theme
