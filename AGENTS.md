# AGENTS.md

## What this repo is

- Learning series: 8 "Loop Engineering" projects, each in its own `project-NN-name/` folder under the root. New projects are added here daily.
- `README.md` at the root is the index: each project gets a row in the Projects table (#, name, concept, status emoji). Update it when adding/completing a project.
- Plain Python 3 only. No manifests, test suite, lint/typecheck config, codegen, or CI anywhere — do not invent any.

## Nested git repo gotcha (important)

- `project-01-watch-loop/` has its **own `.git`**. The parent repo tracks it as a gitlink (mode 160000), so:
  - Commits/pushes made from the parent repo do **not** include any files inside that folder.
  - The parent's `git status` reads clean even when files inside change.
  - To track a project's files in the parent, its inner `.git` must be removed first (`git rm --cached <folder>`, delete `<folder>/.git`, then re-add) or converted to a proper submodule.
- Both the parent repo and the nested repo have `origin` pointing at the **same** GitHub repo (`muzaffaralidev/loop-engineering-projects`). Pushing from either overwrites the other's view.
- The two histories are unrelated: parent `main` = `0d3ba84` ("add readme"); `origin/main` = `a49470e` (the nested repo's history). A plain push from the parent is rejected; per the owner's workflow the parent (root README) is canonical, so it takes a force push or `--allow-unrelated-histories` merge.

## Existing instructions

- `project-01-watch-loop/AGENTS.md` covers that project's quirks: `long-task.py` sleeps 120 s, writes `task-complete.txt` relative to the process CWD (not the script), and must not be killed mid-run. Read it before touching that folder.
