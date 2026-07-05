# Gutenberg (Block Editor)

## In plain English
The block-based content editor built into WordPress. "Gutenberg" is also the
standalone plugin providing the newest, pre-release editor features.

## What it's used for
Composing pages/posts as reusable "blocks"; templates and site editing (FSE).

## Where settings live
- Per-post: the editor itself.
- Site-wide: Appearance → Editor (block themes).

## Safe-change checklist
- [ ] Keep the plugin OFF on production unless you want bleeding-edge features
      (core already ships a stable block editor).
- [ ] Backup before switching classic ↔ block or changing templates.
- [ ] Test one template change, then review front-end.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Editor won't load | JS conflict / old browser | Disable other editor plugins |
| Blocks look broken | Theme/CSS mismatch | Check theme block support |
| Lost classic layout | Switched editors | Restore backup or Classic Editor plugin |

## New terms → glossary
block, Full Site Editing (FSE), block theme
