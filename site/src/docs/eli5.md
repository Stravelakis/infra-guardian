---
checkedAgainst: v0.3
checkedOn: 2026-11-21
---

## Start here

This page takes you from "I have never heard of any of this" to "I made a safe copy of a file, broke it on purpose, and put it back". Go slowly. Nothing here can hurt your websites, because every step in the practice part uses a **throwaway file** you make yourself. Every step says what you should see, so you always know if it worked.

You can stop at any step and come back another day.

> **Do this first** You do not have to understand everything before you begin. Read **The ideas** (about ten minutes), then follow the steps. Come back to the rest when you want it.

**What you will have at the end:**

- The infra-guardian folder on your computer.
- A check that its helpers are healthy.
- One real backup, one deliberate mistake, and one successful undo, all on a practice file.
- A clear picture of what it can do for you, and what it cannot.

**What you do not need:** any secret keys, an account, or to know how to code. You need a computer, an internet connection for the downloads, and about 30 minutes.

> **Watch out** infra-guardian is an early release (v0.3, "Ready for alpha testing"). It is a set of careful habits for Claude, with a few small helper programs. It is a safety net, not a guarantee. It will not stop you or Claude from changing something if the rules are not followed, so the habit of "show me the backup first" is yours too.

## The ideas

Take them one at a time. Nothing here is a test.

### 1. A server is a computer that stays on

When you visit a website, the pages come from a **server**. A server is just a computer that is always on and always connected, so anyone can reach what lives on it. It is usually rented from a company, in a building you will never see.

### 2. Self-hosting means you look after it

Many people use ready-made services where a company does the looking after. **Self-hosting** is the other way round: you put things like a WordPress website or a customer list tool on a server that you control, and you are the one responsible for it. You get freedom and lower cost. You also get the risk that one wrong change can break something.

### 3. Files, folders and settings

A **file** is one thing saved on a computer, like a letter in an envelope. A **folder** is a box that holds files. A lot of the settings for a server are just text files. Change one line in the wrong file and a website can stop working.

### 4. A backup is a spare copy made before you change something

A **backup** is a copy of a file, taken *before* you change it. If the change goes wrong, you put the copy back and everything is as it was. It is the single most useful habit in all of computing.

### 5. A checksum proves the copy is perfect

How do you know a copy is exactly right? You work out a **checksum**: a short code made from everything inside the file, like a fingerprint. If the original and the copy give the same fingerprint, they are identical. If even one letter is different, the fingerprint is completely different. infra-guardian will not say "backed up" until the fingerprints match.

### 6. A dry run is practising without doing

A **dry run** shows you what *would* happen and changes nothing. Think of reading the recipe before you cook.

### 7. A restore is the undo button, and the undo can be undone

To **restore** is to put the backup back in place of the changed file. infra-guardian does one extra careful thing: before it puts the old copy back, it saves the file it is about to replace. So even the undo has an undo.

### 8. A skill is a recipe card for Claude

Claude is an AI assistant. A **skill** is a folder of instructions that Claude reads so that, for a certain kind of job, it behaves in a certain careful way. infra-guardian is a skill for jobs that touch your setup. Its instructions are ten short rules. The big promise is:

> **Back up, preview, ask, change one thing, write it down.**

### 9. Rules versus helpers

infra-guardian has two parts, and it helps to know the difference:

- **The rules** (in a file called `SKILL.md`). Claude follows them: ask first, one change at a time, do not nag, explain jargon.
- **The helpers** (four small programs in a folder called `scripts`). They really do things: make a backup and check it, put it back, check the setup is healthy, run a self-check.

The helpers enforce the backup checks. The rules about asking and going slowly are habits Claude is told to keep.

### 10. Secrets stay in one hidden file

Some extras need a **key**, a long secret code from another service, like a library card. Keys live only in a hidden file called `.env`, which is never uploaded to the internet. **You need no keys for any step on this page.**

### 11. The terminal

A **terminal** is a window where you type a command and press Enter, instead of clicking. On Windows, open **PowerShell** from the Start menu. On a Mac, open **Terminal**. You will copy a few commands into it.

## The steps

Each step has what you should see after it. Type or paste the command, then press **Enter**.

### Step 1. Check that Python is installed

The helpers are written in a language called **Python**. You only need it installed. In your terminal:

```bash
python3 --version
```

On Windows, type `python --version` instead.

**What you should see:** a line starting with `Python 3`, such as `Python 3.12.10`. Any 3.8 or newer is fine.

If it says "command not found" or opens a store window, install Python 3 from python.org, close the terminal, open it again, and repeat.

### Step 2. Check that git is installed

**git** is the tool that downloads a project from the internet.

```bash
git --version
```

**What you should see:** `git version` and some numbers. If not, install git, reopen the terminal and try again.

### Step 3. Download the folder

This copies the whole project to a new folder called `infra-guardian`, inside the folder your terminal is in.

```bash
git clone https://github.com/Stravelakis/infra-guardian.git
cd infra-guardian
```

**What you should see:** some lines about "Cloning into 'infra-guardian'", then nothing else after the second command. You are now inside the folder.

### Step 4. Make your two settings files from the templates

The project ships two **templates**. You copy each one to a new name. The copies are yours, and they are never uploaded.

On Windows (PowerShell):

```bash
Copy-Item .env.example .env
Copy-Item guardian.config.example.yaml guardian.config.yaml
```

On Mac or Linux:

```bash
cp .env.example .env
cp guardian.config.example.yaml guardian.config.yaml
```

**What you should see:** nothing at all. In a terminal, silence usually means it worked. The two new files now exist.

> **Why** The `.env` file is full of things like `<paste-real-token-locally>`. That is on purpose. Nothing uses them until you decide to add a key, so leave the file alone.

### Step 5. Add the one add-on the helpers need

```bash
python3 -m pip install --user pyyaml
```

On Windows: `python -m pip install --user pyyaml`.

**What you should see:** lines about downloading and installing, ending with something like "Successfully installed", or a note that it is already installed. Either is fine.

### Step 6. Ask the doctor to check everything

```bash
python3 scripts/doctor.py
```

**What you should see:** a short report. Lines starting `[PASS]` are good. `[WARN]` is optional, not a problem. `[FIX]` means something needs action. On a fresh setup you will most likely see `PASS` for the config, the four scripts (on Mac and Linux these may say `WARN ... not executable`, which you can ignore) and the backups folder, and a `WARN` for the self-check timer and one more line about Telegram.

> **Watch out** Because you copied `.env.example`, the Telegram line may say `configured` even though you set nothing up. That is a harmless false cheer: the doctor sees the placeholder text and thinks it is a real value. Telegram stays off.

### Step 7. Make a throwaway file

You will practise on a file that does not matter. Make one and look inside:

```bash
echo hello > practice.txt
cat practice.txt
```

**What you should see:** the word `hello`.

### Step 8. Preview a backup (the dry run)

```bash
python3 scripts/backup.py --file practice.txt --reason "practice" --dry-run
```

**What you should see:** a line starting `[DRY RUN] Would BACK UP practice.txt`, and under it an "In plain English" line. Nothing was saved. It only said what it would do.

### Step 9. Make the real backup

Same command, without the preview flag:

```bash
python3 scripts/backup.py --file practice.txt --reason "practice"
```

**What you should see:** "Started a new backup session", then a line starting `Backed up  ->` with a path, then "A verified safe copy of 'practice.txt' now exists", and a short ID such as `c7c31945` (yours will differ). The words "verified safe copy" only appear after the fingerprints matched.

> **Why** With the settings you copied, backups go into a hidden-style folder called `.infra-guardian` in your home folder. The path is printed so you can find it.

### Step 10. See your backups

```bash
python3 scripts/backup.py --list
```

**What you should see:** a small table with an ID, a time (in UTC, the world standard time), the file name `practice.txt` and the reason "practice".

### Step 11. Break the file on purpose

```bash
echo oops-I-broke-it > practice.txt
cat practice.txt
```

**What you should see:** `oops-I-broke-it`. The file is now "broken". Good. This is exactly the moment a backup is for.

### Step 12. Undo it

```bash
python3 scripts/backup.py --restore-last
cat practice.txt
```

**What you should see:** a line "Saved the current version first" (that is the undo's own undo), then "Restored" and the file path, then after `cat`, the word `hello` again. A new file called `practice.txt.pre-restore.` plus a time now sits beside it. That is the broken version, kept just in case. When you are done practising, you may delete `practice.txt` and that extra file; they only exist for the practice.

> **In short** You have just done the whole promise on a small scale: preview, back up and check, change, undo. A real change to a real file works the same way, with Claude doing the typing and you saying yes.

### Step 13. Let Claude know about the skill

For Claude to follow the rules, it has to be able to find the infra-guardian folder as a skill. This repository does not say where Claude keeps its skills on your computer, so do not guess. Ask Claude directly in a chat:

> Where do skills go on this computer? Please put the `infra-guardian` folder there and tell me how to check it is loaded.

**What you should see:** Claude tells you where it put the folder. Then start a fresh chat and say something like "I want to change a setting on my server". If the skill is working, Claude should talk about backing up and asking you first, not jump straight to changing it.

> **Watch out** The default branch of the project (`main`, which is what you just downloaded) has a reformatted header in `SKILL.md`, and I could not confirm that a skill loader still accepts it. The release (`git checkout v0.3`) has the proper header but points to a file name in the wrong capitals. If Claude does not behave as above, tell the project owner. Both problems are written down in `HANDOFF.md`.

## What it does when you use it for real

1. **You ask** Claude to change something. It checks the notes file `HANDOFF.md` first so it does not redo finished work.
2. **It explains** the change in plain words.
3. **It backs up** the file and checks the copy.
4. **It shows a preview.**
5. **You say yes or no.** One change at a time.
6. **It makes the change** and writes it down.
7. **If you say no,** it should not ask again until something changes.

It also has a library of about 50 short notes about tools people often self-host, so Claude can explain "what is this thing" without making things up: hosting, domain names and DNS, AI providers, apps like a CRM or a monitoring dashboard, and WordPress plugins.

**What it does not do:** it does not watch your websites all day. The helper called the self-check only reads a notes file named `status.md` and says what looks open or out of date. For "is my site up?" alerts, use a separate tool such as Uptime Kuma, which the notes explain.

## When something goes wrong

<details>
<summary>"command not found" or "'python3' is not recognized"</summary>

The computer cannot find the program. On Windows, try `python` instead of `python3`. If that also fails, Python is not installed, or the terminal was opened before you installed it: close it, open a fresh one, try again.
</details>

<details>
<summary>"This tool needs the 'PyYAML' package to read your settings file"</summary>

Run `python3 -m pip install --user pyyaml` (on Windows, `python -m pip install --user pyyaml`), then repeat your command.
</details>

<details>
<summary>The backup says "Skipped backup ... file unchanged since last backup"</summary>

That is normal and good. The file is exactly the same as the last copy, so there is nothing new to save. If you really want another copy, add `--force` to the command.
</details>

<details>
<summary>"STOPPED: Can't find the file to back up"</summary>

The file name or place is wrong. Make sure you are in the `infra-guardian` folder, and that the name is spelled exactly right. For a file somewhere else, write its full path.
</details>

<details>
<summary>"That path isn't a single file (folders not supported yet)"</summary>

The backup helper copies one file at a time, not a whole folder. Back up the individual file you are about to change.
</details>

<details>
<summary>"Backup copy did NOT match the original"</summary>

The fingerprint check failed, so the helper refused to call it a backup. Nothing was changed. Try again, and check that the disk is not full.
</details>

<details>
<summary>"No backup with ID ..."</summary>

You typed an ID that does not exist. Run `python3 scripts/backup.py --list` and copy the ID from the first column. By default `--list` shows only the current session; add `--all` to see every one.
</details>

<details>
<summary>I restored the wrong file</summary>

`--restore-last` restores the most recent backup of any file, not the file you were thinking of. Look in the folder for a file with `.pre-restore.` in its name next to your file; that is what you had just before the restore. Next time use `--list` and then `--restore` with the exact ID.
</details>

<details>
<summary>The doctor says "FIX"</summary>

Read the words after the dash. "guardian.config.yaml missing" means you skipped step 4. "cannot write" for the backups folder means the project folder is read-only or the disk is full.
</details>

<details>
<summary>I want backups in a different folder</summary>

Open `guardian.config.yaml` in a text editor and under the `backup:` heading add a line like `  root: D:/my-backups` (with two spaces in front). The setup wizard (`scripts/setup.py`) asks for a folder, but the backup helper does not read that answer, so this line is the way to do it. Keep the spaces; in this kind of file the spaces are part of the meaning.
</details>

<details>
<summary>I am afraid I will upload a secret by accident</summary>

Your `.env` and `guardian.config.yaml` are on the list of files git never uploads. Other things the helpers create, such as a `backups` folder or `self-check.log`, are not on that list. Before you ever upload (push) anything, run `git status` and read what it says. If you are unsure, do not push, and ask.
</details>

## A small dictionary

- **Backup:** a spare copy, made before a change.
- **Checksum:** a fingerprint for a file. Same fingerprint, same file.
- **Dry run:** a preview. It changes nothing.
- **Restore:** putting the backup back. The file you replace is saved first.
- **Server:** a computer that is always on, so others can reach your website or app.
- **Self-hosting:** running your own tools on a server you look after.
- **Skill:** a folder of instructions Claude reads for a certain kind of job.
- **Terminal:** the window where you type commands.
- **`.env`:** a hidden file for secret keys. Never uploaded.
- **Config:** the settings file, `guardian.config.yaml`.

## Where to go next

- The **English** level (the switch at the top left) has the same ground in fewer words, plus the list of safety promises and which ones the scripts really enforce.
- The **Dev** level has the file layout, every command flag, and a list of known quirks.
- Your next real step: pick one small, low-risk file on a real setup, ask Claude to change one thing in it, and watch for the backup, the preview, and the question before the change.
