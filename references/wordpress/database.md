# WordPress database (MySQL/MariaDB) — reference

**In plain English:** The filing cabinet holding all your posts, settings,
and users. If the site is the building, this is the records room.

## What it is used for here
Stores everything WordPress remembers. Losing it = losing the site content.

## Where its settings live
- Connection details live inside wp-config.php.
- The data itself lives in the database container/volume.

## Safe-change checklist
- A WordPress backup is only complete WITH a database dump.
- Test-restore the dump before trusting it (per backups.md).

## Common problems
| Symptom | What it usually means |
|---------|-----------------------|
| site slow after time | Database needs optimizing/cleanup. |
| corrupt table error | A repair is needed — restore from backup if it fails. |

## New terms → add to references/glossary.md
database dump, table, MariaDB
