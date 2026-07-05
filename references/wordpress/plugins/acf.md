# Advanced Custom Fields (ACF)

## In plain English
A plugin that lets you add custom data fields to posts, pages, users, etc., and
display them in your theme — the backbone of many custom WordPress sites.

## What it's used for
Defining structured content (field groups) and outputting it in templates.

## Where settings live
- WP Admin → ACF → Field Groups.
- Field definitions can also be exported to PHP/JSON (acf-json) in the theme.

## Safe-change checklist
- [ ] Backup DB before editing field groups on a live site (renaming a field
      key can orphan existing data).
- [ ] Prefer acf-json version control over live edits.
- [ ] Test template output after any field change.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Field data missing | Field name/key changed | Restore key or migrate data |
| Fields not showing in editor | Location rules | Check field group location |
| Values blank in theme | Wrong get_field context | Verify post ID/context |

## New terms → glossary
field group, field key, acf-json, meta
