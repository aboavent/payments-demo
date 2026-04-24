# ACH Transfer Operations Portal — Claude Code Instructions

A small FastAPI demo app simulating an internal fintech operations tool. Used in live demos.
Keep everything minimal, readable, and demo-friendly.

---

## Architecture

```
app/
  main.py          # FastAPI entrypoint — mounts static, wires router
  config.py        # Config values (SUSPICIOUS_TRANSFER_THRESHOLD lives here)
  models.py        # Transfer, Alert, AuditEvent dataclasses + enums
  repository.py    # In-memory store; swap lists for DB here
  routes.py        # GET / and POST /transfers
  services/
    ach.py         # Transfer submission logic  ← DEMO EXTENSION POINT
    alerts.py      # Alert creation (check_suspicious_transfer stub here)
    audit.py       # Audit event logging
templates/         # Jinja2 HTML (base.html + index.html)
static/styles.css  # Plain CSS, no framework
tests/
  conftest.py      # Shared clear_store fixture (autouse)
  test_transfers.py
  test_audit.py
.github/           # Created live during /devsecops-audit demo — not in baseline
  workflows/
    ci.yml         # GitHub Actions: run pytest on every PR
  pull_request_template.md  # Security checklist enforced on every PR
.claude/
  skills/          # Invokable workflows: spec, plan, build, review, ship, test, simplify, devsecops-audit
  agents/          # Specialist subagents spawned by /devsecops-audit in parallel:
                   #   ci-audit, pr-hygiene-audit, secrets-audit,
                   #   branch-protection-audit, dependency-audit
scripts/
  demo-reset.sh    # Restores baseline state between demo runs
docs/
  specs/           # Saved specs from /spec runs
```

**Run:** `uvicorn app.main:app` (no `--reload` — wipes in-memory store on file changes)  
**Test:** `.venv/bin/pytest tests/ -q`

---

## Workflow

### Decision Framework

Use the **full 4-phase workflow** when any of these apply:
- More than one file will change
- Requirements are ambiguous or the scope is unclear
- Medium/high-risk change: data model, routing logic, alerting, audit
- The change crosses two or more services

Use **lightweight mode** (constraints + success criteria only) when:
- Single-file, low-risk, unambiguous change
- Small fix with obvious root cause
- Urgent incident where speed matters more than ceremony

### Phase 1 — Research

Read before proposing. Never modify files in this phase.

- Identify the relevant service files, models, and tests
- Understand how data flows: routes → services → repository
- When the task is non-trivial, run **parallel investigation tracks**:

  | Track | Questions to answer |
  |---|---|
  | Architecture | Which services are involved? What are the data dependencies? |
  | Tests | What is already covered? What would need a new test case? |
  | Alerts / Audit | Do audit events fire correctly? Is there an alert gap? |
  | Security / Risk | Does this expose account numbers, routing numbers, or amounts in logs? Any injection surface? |

- State what you found before moving on.

### Phase 2 — Specification

Use `/spec` for anything beyond a one-liner. Output:
- Problem statement
- Scope and explicit non-goals
- Files affected and why
- Acceptance criteria (specific, testable)
- Test plan
- Rollout / rollback notes

Do not write code in this phase.

### Phase 3 — Refinement

Ask only the **one highest-leverage unanswered question**.  
Surface assumptions, ambiguities, and operational / compliance risks.  
Do not start coding until ambiguities are resolved.

### Phase 4 — Implementation

Use `/plan` to break the approved spec into atomic tasks.  
Use `/build` to implement one slice at a time — implement → test → verify → next slice.  
Run tests after each slice with `.venv/bin/pytest tests/ -q`.  
Use `/test` to summarize coverage. Use `/review` before reporting done.

---

## Engineering Principles

### Think before coding
- State assumptions explicitly. If uncertain, ask — don't guess silently.
- If multiple interpretations exist, name them. Don't pick one without surfacing the choice.
- If a simpler approach exists, say so. Push back when warranted.
- Define what "done" means before writing a line.

### Simplicity first
- Write the minimum code that solves the problem. Nothing speculative.
- No abstractions for single-use code.
- No "configurability" that wasn't requested.
- Three similar lines are better than a premature abstraction.
- Ask: *"Would a senior engineer say this is overcomplicated?"* If yes, simplify.

### Surgical changes
- Touch only what the task requires.
- Don't improve adjacent code unless asked — mention it instead.
- Match existing style, even if you'd write it differently.
- Every changed line must trace directly to the task.
- If your changes create orphaned imports or variables, remove them. Don't touch pre-existing dead code.

### Solve root causes
- Don't add workarounds when the actual cause can be fixed.
- Don't silently broaden scope — name adjacent issues and ask whether to address them.

### State tradeoffs
- Before significant decisions: "Option A is simpler but doesn't handle X. Option B handles X but adds N lines. I'll go with A unless you say otherwise."

---

## Debugging

- Reproduce the issue before changing any code.
- Read the actual error message — don't assume you know what it says.
- Inspect logs and stack traces before forming a hypothesis.
- Prefer evidence over intuition.
- Isolate failures: find the smallest input that reproduces the problem.
- If the fix feels too clever, you probably haven't found the root cause yet.

---

## Code Quality

- Readability over cleverness.
- Consistency over novelty — match existing patterns in this repo.
- Small, reviewable diffs.
- Preserve backwards compatibility unless explicitly asked to change it.
- No dead code, backwards-compatibility shims, or `# removed` comments.
- Default to no comments. Add one only when the *why* is non-obvious.

---

## Security Expectations

This is a fintech demo. Even in demo mode:
- Never log account numbers, routing numbers, or full amounts in error messages.
- Validate all form inputs at the boundary (`routes.py`), not deep in services.
- The in-memory store has no SQL injection risk — if replacing with a real DB, use parameterized queries.
- Treat `routing_number` and `account_number` as sensitive fields in any new logging or export.

---

## Testing

- Add tests for any non-trivial logic change.
- Tests live in `tests/`. The shared `clear_store` fixture is in `tests/conftest.py` (autouse).
- Run: `.venv/bin/pytest tests/ -q --tb=short`
- Test behavior, not implementation details.
- The PostToolUse hook auto-runs tests after any edit to `app/` or `tests/`.

---

## Definition of Done

A task is done when all of these are true:
- [ ] The code does what the spec or task requires
- [ ] Existing tests still pass
- [ ] New tests cover the changed logic (if non-trivial)
- [ ] The diff is small and reviewable
- [ ] Assumptions, tradeoffs, and risks have been stated
- [ ] `/review` has been run or the change is self-evidently safe

---

## Review Checklist

Before reporting any task complete:
- [ ] **Correctness** — does the code match the spec?
- [ ] **Security** — no sensitive fields in logs; inputs validated at boundary
- [ ] **Maintainability** — follows existing patterns; no unjustified abstractions
- [ ] **Operational** — no silent failure modes; audit events fire as expected
- [ ] **Tests** — coverage exists for the changed logic; all tests pass

---

## Known Extension Point — Do Not Implement Until Asked

The suspicious transfer alerting feature is **intentionally incomplete**:

| File | What exists | What's missing |
|---|---|---|
| `app/config.py` | `SUSPICIOUS_TRANSFER_THRESHOLD = 10_000.00` | Nothing — value is live |
| `app/services/alerts.py` | `check_suspicious_transfer()` — written but commented out | Uncomment function body |
| `app/services/ach.py` | `# DEMO EXTENSION POINT` + commented import and call | Uncomment 2 lines to wire up |

The UI alerts panel already renders any alerts in the store — no template changes needed.

**Do not implement this feature unless explicitly asked.**  
When asked, use `/spec` first to confirm scope before writing a single line.

---

## Demo Reset

To restore the repo to its baseline demo state between runs:

```bash
bash scripts/demo-reset.sh
```

This script:
- Kills any running uvicorn process on port 8000
- Restores `app/services/ach.py` and `app/services/alerts.py` to commented-out state
- Runs the test suite to confirm baseline (should be 10 passed)

After reset, start the server with `uvicorn app.main:app` (no `--reload`).

The reset script also removes `.github/` — this folder is created live during the `/devsecops-audit` demo act and must not exist at the start of the demo.
