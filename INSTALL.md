# Install

infra-guardian is a folder of instructions, scripts and notes. At the time of writing, the repository has one release, `v0.3` ("Ready for alpha testing"), with no attached download, so you get it by cloning the repository.

```bash
git clone https://github.com/Stravelakis/infra-guardian.git
cd infra-guardian
```

## Set it up (no coding)

1. Copy the two template files:
   - `.env.example` to `.env`
   - `guardian.config.example.yaml` to `guardian.config.yaml`

   (The README spells the second one with capital letters; the file in the repository is lowercase.)
2. Leave `.env` as it is for now. It is full of `<placeholders>` on purpose, and nothing runs off it until you add a key.
3. Optional: run the friendly wizard, which asks a few questions and writes `guardian.config.yaml` for you:

   ```bash
   python3 scripts/setup.py
   ```
4. Check everything is in place:

   ```bash
   python3 scripts/doctor.py
   ```

## What it needs

- Python 3 (3.8 or newer).
- PyYAML, for `scripts/backup.py` and `scripts/infra-status-check.py` (`pip install pyyaml`).

## Keys

You do not need any key for the basics. Optional extras (phone or Telegram alerts, live AI models) need a key from the other service. Keys live only in `.env`, which is gitignored. Check with `git status` before you push anything.
