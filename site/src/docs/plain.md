---
checkedAgainst: v0.3
checkedOn: 2026-11-21
---

## What infra-guardian is

You build real things: a website, an AI tool, a CRM. You are not a system administrator, and one wrong click on a **server** can break something you cannot fix. infra-guardian is a **skill**: a folder of instructions and small helper scripts that makes Claude careful whenever a request touches your **self-hosted** setup.

Its one promise:

> **Back up, preview, ask, change one thing, write it down.**

It aims never to make a big pile of changes at once, and never to change a file without a saved, checked copy to go back to.

This page describes release **v0.3** (5 July 2026). It is an early release, published as "Ready for alpha testing".

> **Watch out** Be clear about what it is. It is a set of rules Claude follows, plus helpers for backups. Nothing physically stops Claude from editing a file without a backup, and the scripts do not watch your servers on their own. The safety comes from the rules being loaded and followed, so check that it is installed correctly (see below) and ask Claude to show you the backup before you say yes.

## What it does for you

- **Backs up first.** Before it touches a file it saves a copy and checks the copy is identical. It does not say "done" until the check passes.
- **Asks first.** It explains the change in plain words and waits for your yes. One change at a time.
- **Previews.** A dry run shows what would happen without doing it.
- **Makes undo possible, even for the undo.** When it restores a backup, it first saves the file it is about to replace.
- **Explains.** A new technical term gets a one-line entry in a glossary, so you are never left guessing.
- **Does not nag.** Say no, or snooze, and it should not bring the same proposal back until something changes. (This is a rule for Claude, not something the scripts enforce.)
- **Knows your stack.** A library of about 50 short notes covers hosting, domain and DNS, AI providers (Mistral, NVIDIA, Groq, Cerebras, OpenRouter, Gemini), self-hosted apps (such as Twenty CRM, Uptime Kuma, n8n, Open WebUI, LibreChat) and WordPress plugins (such as ACF, Rank Math Pro, LiteSpeed Cache). Claude reads the index first and opens only the note it needs.
- **Checks itself.** A "doctor" script reports whether its own settings, scripts and backup folder look healthy.

**Watching, honestly.** The README says it "watches" your services. In the released scripts, the scheduled self-check only reads a notes file called `status.md` and flags things like open items; it does not ping your websites. For real "is it up?" monitoring, the library has a note on Uptime Kuma, a separate tool.

**Is it for you?** Yes, if you self-host apps, you do not write code, and you want a plain-English explanation before anything changes. Probably not, if you are an experienced sysadmin who wants full manual control with no guardrails.

## Install it

There is no installer and no download. You need a **terminal**, **Python** 3 (version 3.8 or newer in practice) and **git**.

1. Get the folder:

   ```bash
   git clone https://github.com/Stravelakis/infra-guardian.git
   cd infra-guardian
   ```

2. Copy the two template files: `.env.example` to `.env`, and `guardian.config.example.yaml` to `guardian.config.yaml`. (Older text spells the second one in capitals; the real file is lowercase.)
3. Leave `.env` alone for now. It is full of `<placeholders>` on purpose. You need **no keys** for the basics.
4. Install the one add-on the scripts need: `python3 -m pip install --user pyyaml`.
5. Optional: run the wizard with `python3 scripts/setup.py`. It asks a few questions and writes the config.
6. Check it: `python3 scripts/doctor.py`. On Windows, type `python` instead of `python3`.

> **Do this first** Work out where Claude looks for skills on your machine and put the folder there. The repository does not say, and I could not confirm from it where that is. If Claude never mentions the rules, treat that as "not loaded yet".

> **Watch out** `main`, which is what you get when you clone, has a problem the v0.3 release does not: its `SKILL.md` header was reformatted and no longer has the standard first lines a skill loader looks for. Whether your setup still loads it is not confirmed. The release (`git checkout v0.3`) has the proper header, but it has the opposite flaw: its text points to `references/INDEX.md` in capitals while the real file is `index.md`, which fails on Linux and GitHub. Neither version is perfect; both are listed as open problems in `HANDOFF.md`.

On the wizard, two things to know. It asks for a backup folder, but the backup script ignores that answer and uses `~/.infra-guardian/backups` (in your home folder) unless the config has a `root:` line under `backup:`. And if you type a Telegram token into it, it is saved as plain text in the config and is not actually used. Leave those blank.

## A typical session

This is the flow the rules describe, not a recording. For a real captured run of the backup helper, see "A real run" at the top of this page.

1. **You ask** Claude to change something in your setup: a setting in a config file, a plugin option, a DNS record.
2. **It checks `HANDOFF.md`** for open items and for files that are already settled, so it does not redo finished work.
3. **It explains** what it wants to change and why, in plain words.
4. **It backs up** the file and confirms the copy matches.
5. **It shows a preview** of what would change.
6. **You say yes or no.** One change only.
7. **It makes the change** and writes it down in the log files.
8. **If it goes wrong,** you ask it to restore the last backup. It saves the broken file first, then puts the good one back and checks it.

> **Try it** Before you trust it with a real file, practise on a throwaway one. Run `python3 scripts/backup.py --file somefile.txt --dry-run`, then without `--dry-run`, then `--list`, change the file, and run `--restore-last`.

## The commands you might use yourself

```bash
python3 scripts/backup.py --file PATH --reason "why"
python3 scripts/backup.py --list
python3 scripts/backup.py --restore-last
python3 scripts/doctor.py
```

- Add `--dry-run` to the first one to preview.
- `--restore ID` restores a specific backup. The ID is in the first column of `--list`.
- A backup is only reported as done once its checksum matches.
- It backs up **single files**, not folders.

## Safety promises, and what backs each one

| Promise | How it is kept |
|---|---|
| A backup is a perfect copy | The script checks the checksums and refuses to report success otherwise |
| Restoring can be undone | The script saves the current file first |
| Preview before change | A dry-run option in the script, and a rule for Claude |
| Ask first, one change at a time | A rule for Claude |
| No nagging after a no | A rule for Claude |
| Secrets stay out of the project | A rule, plus `.env` being listed in `.gitignore` |

## Keys and secrets

Some optional extras (Telegram alerts, live AI models) need a key from another service. Keys belong only in the hidden `.env` file, which is never uploaded. Check with `git status` before you push anything. If you would rather not keep keys in a file, the guide suggests your hosting panel's secrets section.

## If something goes wrong

- **"This tool needs the 'PyYAML' package."** Run `python3 -m pip install --user pyyaml`, then try again.
- **"Backup copy did NOT match the original."** Nothing was changed. Try again, and check you have free disk space.
- **Doctor says a script is "not executable".** On Mac and Linux this is expected, because the files are saved without that flag. Ignore it and run the scripts with `python3`.
- **Doctor says Telegram is "configured" and you did not set it up.** If you copied `.env.example` untouched, the placeholder counts as a value. It is a false pass. Telegram stays off unless you also set `enabled: true` under `telegram:` in the config and put your token and chat id in `.env`.
- **The backup folder is not where you put it.** See the wizard note above. Add `root: /your/path` under `backup:` in `guardian.config.yaml`.
- **I restored and now there is a strange extra file.** That is the saved copy of what you had before, named `.pre-restore.` plus a time, next to your file. Keep it until you are sure.
- **`--restore-last` restored the wrong file.** It restores the most recent backup of any file, not of the file you are thinking about. Use `--list` and `--restore ID` instead.
- **Git wants to commit `backups/` or `self-check.log`.** Do not. Of the files the guardian makes, only `.env` and `guardian.config.yaml` are on the ignore list.

> **In short** Install it, copy the two template files, run the doctor, and practise the backup on a throwaway file. Treat the rules as the safety net, and never skip the "show me the backup" step.
