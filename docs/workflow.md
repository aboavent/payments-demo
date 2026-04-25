# Workflow Documentation

How Claude Code is instructed to work in this repository — the 4-phase workflow, decision framework, skills, and hooks.

---

## The core idea

Most AI coding mistakes happen not because the model writes bad code, but because it starts writing before the problem is understood. This workflow enforces a discipline: research before specifying, specify before planning, plan before implementing. Each phase has a clear output and a gate.

The workflow adapts to task size. A one-line fix doesn't need a full spec. A multi-file feature does.

---

## Decision framework

### When to use the full 4-phase workflow

Use all four phases when any of these are true:

- More than one file will change
- The requirements are ambiguous or incomplete
- The change is medium or high risk (data model, alerting logic, audit events, routing)
- The change crosses two or more services

### When to use lightweight mode

For small, low-risk, single-file changes, skip to a two-line spec:
- **Constraints:** what must not change
- **Success criteria:** what must be true when done

Then implement directly.

Examples of lightweight-mode tasks:
- Fix a typo in a label
- Change a config value
- Add a missing `memo` to an audit event detail

---

## Phase 1 — Research

**Goal:** understand before proposing anything. No file changes in this phase.

What Claude Code does:
- Reads the relevant service files, models, and tests
- Traces the data flow: routes → services → repository
- States what it found before moving on

### Parallel investigation tracks

For non-trivial tasks, research runs on four tracks simultaneously:

| Track | Questions answered |
|---|---|
| **Architecture** | Which services are involved? What are the data dependencies? What calls what? |
| **Tests** | What behavior is already covered? What new test cases would be needed? |
| **Alerts / Audit** | Do audit events fire correctly after this change? Is there an alerting gap? |
| **Security / Risk** | Are sensitive fields (account numbers, routing numbers) exposed? Any new injection surface? |

These tracks are independent and can be investigated in parallel. The outputs converge into the spec.

---

## Phase 2 — Specification

**Goal:** produce a written spec before any code is written.

Invoked with: `/spec [description]`

The spec is the shared source of truth. Code without a spec is guessing. The spec forces clarity about what we're building *before* the cost of rework kicks in.

### Full spec format

```
Problem statement    — what is broken or missing and why it matters
Scope               — what this change covers
Non-goals           — what it explicitly does not touch
Files affected      — table: file | change type | reason
Acceptance criteria — bulleted, observable, testable
Test plan           — which test cases to add or update
Rollout / rollback  — how to deploy; how to undo
Risks / assumptions — non-obvious risks and baked-in assumptions
Open questions      — anything that must be resolved before implementation
```

### Surfacing assumptions

Before writing spec content, Claude lists its assumptions:

```
ASSUMPTIONS I'M MAKING:
1. [assumption]
2. [assumption]
→ Correct me or I'll proceed with these.
```

This is the most valuable part of the spec. Assumptions are the most dangerous form of ambiguity — they're invisible until they're wrong.

---

## Phase 3 — Refinement

**Goal:** resolve the one highest-leverage unanswered question before coding starts.

Claude asks at most one clarifying question. Not five. The constraint forces prioritization: if you can only ask one thing, you ask the right thing.

What gets surfaced in refinement:
- Assumptions baked into the spec that need explicit confirmation
- Operational risks (what happens to in-flight state?)
- Compliance risks (does this touch sensitive fields?)
- Scope ambiguity (does "alerting" mean UI alert, or also an audit event, or also an email?)

Once refinement is resolved, the spec is locked. Implementation can begin.

---

## Phase 4 — Implementation

**Goal:** implement the approved spec in atomic, testable slices.

### Step 1 — Break into tasks

Invoked with: `/plan`

The plan decomposes the spec into tasks, each with:
- One-sentence description
- Explicit acceptance criteria
- Verification step (test command or manual check)
- Files that will change
- Size: XS / S / M (L or larger means split it)

Tasks are ordered by dependency. Foundations before features.

### Step 2 — Build one slice at a time

Invoked with: `/build task N`

Rules during build:
- Touch only the files in the approved task
- Leave the system in a working state after every file change
- Run tests after each change — don't accumulate broken state
- Report scope creep rather than silently acting on it

The PostToolUse hook auto-runs pytest after every `Edit` or `Write` to `app/` or `tests/`. Claude gets immediate test feedback without having to ask.

### Step 3 — Verify

Invoked with: `/test`

Runs the full test suite and summarizes: what passed, what failed, what coverage exists, what's missing.

### Step 4 — Review before closing

Invoked with: `/review`

Five-axis review: correctness, security/compliance, maintainability, operational risk, assumptions and scope. Returns a verdict per axis and a list of recommended actions.

### Step 5 — Ship

Invoked with: `/ship`

Pre-ship checklist: tests pass, no debug artifacts, `/review` passed, feature works end-to-end, rollback path documented.

For this repo, "ship" means: restart uvicorn. Rollback: revert the edited files.

---

## Skills reference

All skills live in `.claude/skills/`. Each is invoked as a slash command.

| Command | Phase | What it does |
|---|---|---|
| `/spec` | 2 — Specification | Produces structured spec, no code |
| `/plan` | 4 — Implementation | Breaks approved spec into atomic tasks |
| `/build` | 4 — Implementation | Implements one task slice with surgical changes |
| `/test` | 4 — Implementation | Runs tests, summarizes coverage and gaps |
| `/review` | 4 — Implementation | Multi-axis change review |
| `/ship` | 4 — Implementation | Pre-ship checklist + rollback notes |
| `/refactor` | Any | Identifies unnecessary complexity after a feature works |
| `/devsecops-audit` | Any | Audits CI/CD and security posture; spawns 5 parallel specialist subagents to fix gaps |
| `/demo-reset` | Setup | Restores baseline state between demo runs |

---

## The PostToolUse hook

Defined in `.claude/settings.json`:

```json
{
  "matcher": "Edit|Write",
  "hooks": [{
    "type": "command",
    "command": "jq -r '.tool_input.file_path // empty' | grep -qE '^(app|tests)/' && .venv/bin/pytest tests/ -q --tb=short 2>&1 || true",
    "timeout": 30,
    "statusMessage": "Running tests..."
  }]
}
```

**What it does:**
1. Fires after every `Edit` or `Write` tool call
2. Reads the file path from tool input
3. Checks whether the path is under `app/` or `tests/`
4. If yes: runs pytest with short tracebacks; shows "Running tests..." in the status bar
5. Exits 0 regardless — test failures are visible output, not session-blockers
6. Skips silently for templates, CSS, docs, and skill files

**Why it matters:** This is the backpressure mechanism. Every code change gets immediate feedback. A failing test surfaces before Claude moves to the next file. Broken state never accumulates.

---

## Definition of done

A task is complete when all of these are true:

- [ ] The code does what the spec requires
- [ ] Existing tests still pass
- [ ] New tests cover the changed logic (if non-trivial)
- [ ] The diff is small and reviewable
- [ ] Assumptions, tradeoffs, and risks have been stated
- [ ] `/review` has passed with no blocking issues

---

## Review checklist

Before reporting any task complete:

| Axis | Check |
|---|---|
| Correctness | Does the code match the spec? |
| Security | No sensitive fields in logs; inputs validated at boundary |
| Maintainability | Follows existing patterns; no unjustified abstractions |
| Operational | No silent failure modes; audit events fire as expected |
| Tests | Coverage exists for changed logic; all tests pass |
