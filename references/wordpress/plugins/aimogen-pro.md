# Aimogen Pro

## In plain English
An all-in-one AI WordPress plugin: content writer, editor, chatbot, and
automation toolkit. The free "Aimogen" gives basic AI tools; Pro unlocks
advanced automation and publishing. [[1]] [[7]]

## What it's used for
Generating/rewriting posts, bulk content, an on-site AI chatbot, and
scheduled/automated publishing. [[7]]

## Where settings live
- WP Admin → Aimogen → Settings.
- Your AI provider API key is stored in plugin settings (treat as a secret;
  mirror to .env if the plugin supports it — never commit real keys).

## Safe-change checklist
- [ ] Backup DB before enabling any auto-publish automation.
- [ ] Dry-run generation to DRAFT, review, then publish.
- [ ] One automation rule at a time; log token spend.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Generation fails | Bad/empty API key or quota | Re-check provider key + credit |
| Auto-posts spammy | Over-broad automation rule | Switch rule to draft-only |
| Chatbot silent | Missing model config | Re-select model in settings |

## New terms → glossary
API key, auto-publish, token spend
