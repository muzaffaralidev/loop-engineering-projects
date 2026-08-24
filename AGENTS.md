# AGENTS.md

## What this repo is

- Learning series: 8 "Loop Engineering" projects, each in its own `project-NN-name/` folder under the root. New projects are added here daily.
- `README.md` at the root is the index: each project gets a row in the Projects table (#, name, concept, status emoji). Update it when adding/completing a project.
- Plain Python 3 only. No manifests, test suite, lint/typecheck config, codegen, or CI anywhere — do not invent any.

## Git workflow

- The parent repo is canonical: everything (README, AGENTS.md, every `project-NN-name/` folder with all its files) lives in its single history and is pushed from here.
- Never run `git init` inside a project folder. An embedded `.git` makes the parent track the folder as a gitlink (mode 160000): commits/pushes then silently exclude its files and `git status` reads clean while content changes. This already happened once with `project-01-watch-loop`; if it recurs, fix with `git rm --cached <folder>`, delete `<folder>/.git`, re-add.
- Daily workflow: add the new `project-NN-name/` folder + update the README table, commit, `git push origin main`.

## Existing instructions

- `project-01-watch-loop/AGENTS.md` covers that project's quirks: `long-task.py` sleeps 120 s, writes `task-complete.txt` relative to the process CWD (not the script), and must not be killed mid-run. Read it before touching that folder.
