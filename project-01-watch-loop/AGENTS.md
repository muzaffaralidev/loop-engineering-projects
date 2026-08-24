# AGENTS.md

## Overview

- Single-file demo repo. The only source file is `long-task.py`; there is no manifest, test suite, lint/typecheck config, or CI. Do not invent any.

## long-task.py behavior

- Sleeps 120 seconds, then writes `task-complete.txt` containing a success message.
- The output path is relative to the **process's current working directory**, not the script location. When looking for `task-complete.txt`, check both the directory `python` was launched from and this repo root.
- Never edit or kill a running `long-task.py` process mid-run; let it finish.

## Git state quirk

- Branch `master` has no commits yet and `long-task.py` is untracked, so `git log` fails and `git status` shows everything as new.
