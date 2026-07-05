# Code Snippets Pro

## In plain English
A plugin to add small pieces of PHP/JS/CSS to WordPress safely, instead of
editing functions.php directly. Pro adds CSS/JS snippet types and more.

## What it's used for
Running site tweaks as toggleable "snippets" with error-catching so a bad
snippet doesn't white-screen the whole site.

## Where settings live
- WP Admin → Snippets.
- Snippets stored in the database, not theme files.

## Safe-change checklist
- [ ] Backup DB before adding/activating a snippet.
- [ ] Use "Only run once"/safe-mode when testing risky PHP.
- [ ] One snippet at a time; note what each does.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| White screen after activate | Fatal PHP in snippet | Add ?snippets-safe-mode=1 to URL |
| Snippet not applying | Wrong scope (admin/front) | Check snippet run location |
| CSS not showing | Cache | Purge cache |

## New terms → glossary
snippet, safe mode, functions.php
