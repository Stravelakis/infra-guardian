# Tutor LMS Pro

## In plain English
The premium version of Tutor LMS — a plugin that turns WordPress into a
learning-management system (courses, lessons, quizzes, students).

## What it's used for
Building/selling online courses: course builder, quizzes, certificates,
drip content, and (Pro) advanced monetization + reports.

## Where settings live
- WP Admin → Tutor LMS → Settings.
- Course data stored in the WP database (custom post types + meta).

## Safe-change checklist
- [ ] Backup DB before editing course structure or payment settings.
- [ ] Test enrollment/checkout on a staging course first.
- [ ] Verify add-on compatibility before enabling one.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Course content blank | Cache/permalinks | Purge cache, flush permalinks |
| Payment fails | Gateway/add-on config | Test in gateway sandbox |
| Quiz not saving | JS conflict | Disable conflicting plugin, retest |

## New terms → glossary
LMS, drip content, custom post type
