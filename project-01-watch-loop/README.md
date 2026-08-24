# Watch Loop Demo

A beginner-friendly demo of a **long-running task** and how another process can **watch for its completion** using a signal file.

## What it does

`long-task.py`:

1. Prints `Long task started...`
2. Sleeps for **120 seconds** (simulating real work like training a model or processing data)
3. Writes a `task-complete.txt` file containing `Task completed successfully!`
4. Prints `Long task finished!`

## Requirements

- Python 3 (no external packages needed)

## How to run

```bash
python long-task.py
```

## What to expect

- The script blocks for about two minutes before finishing.
- When it finishes, a file named `task-complete.txt` appears **in the directory you ran the command from**, not necessarily next to the script.
- Re-running the script overwrites `task-complete.txt`.

## Try it yourself: build a watcher

While the task runs, open a second terminal and poll for the result every 10 seconds:

```bash
# Linux/macOS
while [ ! -f task-complete.txt ]; do sleep 10; done; echo "Task complete!"
```

```powershell
# Windows PowerShell
while (-not (Test-Path task-complete.txt)) { Start-Sleep -Seconds 10 }
Write-Output "Task complete!"
```

This polling pattern ("check, sleep, repeat") is the basis for wait loops used in scripts, CI pipelines, and automation tools.

## Files

| File | Purpose |
|------|---------|
| `long-task.py` | The simulated long-running task |
| `task-complete.txt` | Created by the script when it finishes (safe to delete) |
