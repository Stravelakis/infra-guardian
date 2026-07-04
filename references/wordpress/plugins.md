# WordPress plugins & themes — reference

**In plain English:** Add-ons that give your site extra features or looks.
Also the #1 source of site breakage and security holes.

## What it is used for here
Anything WordPress can't do alone. Each one is code someone else wrote.

## Where its settings live
- In the site folder + database; versions tracked by WordPress itself.

## Safe-change checklist
- Back up before adding/updating/removing any plugin (auto).
- Change ONE at a time so you know what broke if something does.
- Remove unused plugins — they're still an attack surface.

## Common problems
| Symptom | What it usually means |
|---------|-----------------------|
| site broke after update | The last plugin changed is the suspect. |
| unexpected admin behaviour | Possible compromised/abandoned plugin. |

## New terms → add to references/glossary.md
attack surface, abandoned plugin
