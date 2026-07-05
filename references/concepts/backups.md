# Backups — reference

**In plain English:** Copies of your data kept safe elsewhere, proven to
actually restore. A backup you've never tested is only a hope.

## What it is used for here
Every guardian action makes a checksummed backup first; this is the record.

## Where its settings live
- Backup targets + schedule in guardian.config.yaml.
- The verified-restore log lives in status.md ("Verified?" column).

## Safe-change checklist
- 3-2-1: 3 copies, 2 media types, 1 off-site.
- A backup is not "verified" until a test restore succeeded.

## Common problems
| Symptom | What it usually means |
|---------|-----------------------|
| backup size = 0 | The job ran but captured nothing — check the path. |
| restore fails | The backup was corrupt; the checksum should have caught it. |

## New terms → add to references/glossary.md
3-2-1, off-site, test restore
