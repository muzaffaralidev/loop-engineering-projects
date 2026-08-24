# 🔄 Loop Engineering — 8 Practical Projects

A practical implementation of the **Loop Engineering** concepts from the GIAIC Final Graduation Exam preparation.

This repository contains **8 hands-on projects**, starting from a simple in-session watch loop and gradually progressing toward more advanced autonomous and reliable loops.

The goal is not just to understand loops theoretically, but to **build, test, observe, and understand how AI agent loops work in practice.**

---

## 🎯 Objectives

Through these projects, we will learn how to:

- Build AI agent loops
- Monitor long-running tasks
- Use heartbeats and periodic checks
- Define stopping conditions
- Handle failures and retries
- Control cost and execution time
- Add human approval when needed
- Build reliable autonomous workflows
- Understand different loop patterns

---

## 📚 Projects

| # | Project | Concept | Status |
|---|---|---|---|
| 01 | A Watch Loop | In-Session Loop | ✅ Completed |
| 02 | TBD | — | ⏳ |
| 03 | TBD | — | ⏳ |
| 04 | TBD | — | ⏳ |
| 05 | TBD | — | ⏳ |
| 06 | TBD | — | ⏳ |
| 07 | TBD | — | ⏳ |
| 08 | TBD | — | ⏳ |

> Project names and concepts will be updated as each project is completed.

---

# 🚀 Project 01 — A Watch Loop

### Concept

**In-Session Loop**

### Goal

Build a loop that monitors a long-running task and tells the user when the task is finished.

### Workflow

```text
Long Task
    ↓
Watch Loop
    ↓
Check Task Status
    ↓
Task Finished?
   ↙       ↘
 NO        YES
 ↓          ↓
Wait      Report
 ↓          ↓
Check     STOP