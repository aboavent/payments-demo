# Claude Code Setup

How the Claude Code workflow layer is configured in this repository — CLAUDE.md, skills, settings, and hooks.

---

## Overview

The Claude Code layer consists of four parts:

| Part | Location | Purpose |
|---|---|---|
| Project constitution | `CLAUDE.md` | Loaded every session; defines architecture, workflow, principles, and known extension points |
| Skills | `.claude/skills/*/SKILL.md` | Slash commands invoked during the demo workflow |
| Settings | `.claude/settings.json` | Default mode, permissions, PostToolUse hook |
| Local settings | `.claude/settings.local.json` | Per-machine overrides (not committed) |

---

## CLAUDE.md — Project Constitution

`CLAUDE.md` is loaded automatically at the start of every Claude Code session in this directory. It is the highest-priority set of instructions Claude receives about this project.

### What it contains

**Architecture map** — the file tree with one-line descriptions, the run command, and the test command. Claude reads this before touching any file.

**Workflow** — the full 4-phase workflow and the decision framework (when to use full mode vs. lightweight mode). This is the first thing Claude applies when a task arrives.

**Engineering principles** — Karpathy-derived rules: think before coding, simplicity first, surgical changes, solve root causes, state tradeoffs. These govern moment-to-moment behavior.

**Debugging principles** — reproduce before changing, read the actual error, prefer evidence over intuition.

**Code quality rules** — readability over cleverness, consistency over novelty, small reviewable diffs.

**Security expectations** — fintech-specific: sensitive field handling, input validation at boundary, parameterized queries if a real DB is added.

**Testing expectations** — where tests live, how to run them, the autouse fixture, what the hook does.

**Definition of done** — a checklist that must all be true before a task is reported complete.

**Review checklist** — five axes, must pass before closing any non-trivial task.

**Known extension point** — an explicit table telling Claude exactly where the suspicious transfer alerting feature lives, what is already there, and that it must not be implemented until asked.

### Why it matters

Without `CLAUDE.md`, Claude has general-purpose coding knowledge but no knowledge of:
- Which files do what in this specific repo
- What patterns to follow or avoid
- What the demo extension point is
- What "done" means here

With `CLAUDE.md`, every session starts with full project context. The model doesn't need to be re-briefed.

---

## Skills

Skills live in `.claude/skills/`. Each skill is a markdown file that Claude reads when the corresponding slash command is invoked. They don't run code — they instruct Claude on how to behave for that specific action.

### `/spec` — Implementation Specification

**File:** `.claude/skills/spec/SKILL.md`

Invoked at the start of any non-trivial task. Produces a structured spec with no implementation code.

Two modes:
- **Full spec** — problem statement, scope, non-goals, files affected, acceptance criteria, test plan, rollout/rollback, risks and assumptions, open questions
- **Lightweight spec** — constraints + success criteria only, for small single-file changes

The skill's key instruction: surface assumptions before writing anything.

**When to invoke:** before any change that touches more than one file, or when requirements are ambiguous.

### `/plan` — Task Breakdown

**File:** `.claude/skills/plan/SKILL.md`

Invoked after a spec is approved. Decomposes the spec into atomic tasks. No implementation code.

Each task includes:
- One-sentence description
- Acceptance criteria
- Verification step (test command or manual check)
- Files affected
- Size: XS / S / M (L or larger means split it)

Adds checkpoints after every 2–3 tasks.

**When to invoke:** after `/spec` is approved, before `/build`.

### `/build` — Incremental Implementation

**File:** `.claude/skills/build/SKILL.md`

Implements one task from the approved plan. Surgical changes only — touches exactly the files in the task, nothing else.

Key behaviors:
- States which task it's implementing before writing any code
- Removes orphaned imports/variables created by its changes; doesn't touch pre-existing dead code
- Reports scope creep rather than acting on it
- Runs tests after each file change; fixes failures before moving on

**When to invoke:** for each task in the plan, one at a time.

### `/test` — Test Runner and Coverage

**File:** `.claude/skills/test/SKILL.md`

Runs the full test suite and summarizes results. For new features, proposes missing test cases.

Output: pass/fail count, any failure details, a coverage table for the changed logic, whether existing coverage is sufficient.

**When to invoke:** after `/build` completes, or when assessing whether a change needs more tests.

### `/review` — Change Review

**File:** `.claude/skills/review/SKILL.md`

Multi-axis review of the current change. Five axes:

1. **Correctness** — does the logic match the spec? edge cases handled?
2. **Security / Compliance** — are sensitive fields (account numbers, routing numbers) leaking into logs or error messages? inputs validated at the route boundary?
3. **Maintainability** — consistent with existing patterns? no unjustified abstractions?
4. **Operational risk** — silent failure modes? audit events still firing? clear rollback path?
5. **Assumptions and scope** — did implementation stay within the approved spec? any assumptions baked in silently?

Output format:
```
Correctness:     OK / Note / Risk — explanation
Security:        OK / Note / Risk — explanation
Maintainability: OK / Note / Risk — explanation
Operational:     OK / Note / Risk — explanation
Assumptions:     OK / Note / Risk — explanation

Recommended next actions: [list]
Blocking issues: [list or "none"]
```

**When to invoke:** before reporting any non-trivial task complete.

### `/ship` — Pre-Ship Checklist

**File:** `.claude/skills/ship/SKILL.md`

Confirms the change is demo-ready. Checks: tests pass, no debug artifacts, `/review` passed, feature works end-to-end in the UI, rollback path documented.

For this repo: rollout = restart uvicorn; rollback = revert the edited files.

Closes with a "SHIPPED / STILL STUBBED / NATURAL NEXT" summary.

**When to invoke:** after `/review` passes, before declaring the feature done.

### `/simplify` — Complexity Review

**File:** `.claude/skills/simplify/SKILL.md`

Post-feature pass to identify unnecessary complexity. Applies Chesterton's Fence: understand why code exists before removing or changing it. Produces a candidate table (file, issue, before, after, behavior preserved) with a recommendation on what to apply and what to skip.

Behavior preservation is the hard rule: if a simplification requires modifying tests to pass, it changed behavior — stop.

**When to invoke:** after a feature is working and tests pass, when the implementation feels heavier than it needs to be.

---

## Settings

### `.claude/settings.json`

```json
{
  "defaultMode": "acceptEdits",
  "permissions": {
    "allow": [
      "Bash(python3*)",
      "Bash(pip*)",
      "Bash(.venv/bin/pip*)",
      "Bash(pytest*)",
      "Bash(uvicorn*)",
      "Bash(ls*)",
      "Bash(find*)"
    ]
  },
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path // empty' | grep -qE '^(app|tests)/' && .venv/bin/pytest tests/ -q --tb=short 2>&1 || true",
        "timeout": 30,
        "statusMessage": "Running tests..."
      }]
    }]
  }
}
```

**`defaultMode: acceptEdits`** — file edits are accepted automatically without a confirmation prompt. Bash commands and other tools still require approval unless in the allow list.

**Permissions allow list** — the commands Claude can run without prompting:
- `python3*` — virtual env creation, running scripts
- `pip*` / `.venv/bin/pip*` — dependency installation
- `pytest*` / `.venv/bin/pytest*` — test runner (both system and venv)
- `uvicorn*` — dev server
- `ls*` / `find*` — directory inspection

**PostToolUse hook** — fires after every `Edit` or `Write` tool call:
1. Reads the edited file path from tool input via `jq`
2. Checks whether path is under `app/` or `tests/`
3. If yes: runs `.venv/bin/pytest tests/ -q --tb=short`; shows "Running tests..." in status bar
4. Always exits 0 (`|| true`) — failures are visible output, not session-blockers
5. Skips for templates, CSS, docs, settings, and skill files

### `.claude/settings.local.json`

Personal overrides for this project (not committed to git, listed in `.gitignore`). Contains some additional allow rules added during initial setup.

---

## How it all fits together in a demo session

```
Session starts
    ↓
CLAUDE.md loads automatically
(Claude knows: architecture, workflow, principles, extension point)
    ↓
Task arrives: "add suspicious transfer alerting"
    ↓
CLAUDE.md: decision framework → full 4-phase (multi-file, medium risk)
    ↓
Phase 1: Research (Claude reads ach.py, alerts.py, config.py, tests)
    ↓
/spec   → produces spec, surfaces assumptions
    ↓
Phase 3: Refinement (one clarifying question if needed)
    ↓
/plan   → atomic tasks with acceptance criteria
    ↓
/build task 1
    ↓
[Edit ach.py] → hook fires → pytest runs → "10 passed" in status bar
    ↓
[Edit alerts.py] → hook fires → pytest runs → "10 passed"
    ↓
/test   → confirms coverage
    ↓
/review → all axes OK, no blocking issues
    ↓
/ship   → checklist complete; rollback: revert two files
```

The entire workflow — from research to shipping — runs inside one Claude Code session, with no external tools, no pipeline, and no context switching.
