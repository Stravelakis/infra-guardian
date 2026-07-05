# Directorist Pro

## In plain English
The premium version of Directorist — a plugin for building directory/listing
sites (business directories, classifieds, listings with search & maps).

## What it's used for
Front-end listing submission, categories, search filters, maps, and (Pro)
monetization add-ons like paid listings.

## Where settings live
- WP Admin → Directory Listings → Settings.
- Listings are custom post types stored in the database.

## Safe-change checklist
- [ ] Backup DB before changing listing fields or pricing plans.
- [ ] Test a front-end submission after form/field changes.
- [ ] Enable add-ons one at a time.

## Common problems
| Symptom | Likely cause | Safe first step |
|---|---|---|
| Maps blank | Missing/invalid API key | Re-check map provider key |
| Submissions not saving | Form field conflict | Test with default fields |
| Search returns nothing | Index/taxonomy issue | Re-save permalinks |

## New terms → glossary
directory listing, taxonomy, custom post type
