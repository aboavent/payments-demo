---
name: plan
description: Breaks an approved spec into ordered, atomic tasks with acceptance criteria. Use after /spec is approved and before implementation begins.
---

# /plan — Task Breakdown

Decompose the approved spec into small, verifiable tasks. Each task must be implementable and testable in a single focused session.

**Do not write implementation code.** Output only the plan.

---

## Workflow gate — check before doing anything

**Spec exists?** Check `docs/specs/` for a relevant spec file.
- If no spec file exists → stop and respond:
  ```
  ⛔ No spec found in docs/specs/.
  The 4-phase workflow requires a spec before planning.
  Run /spec first to define the scope and acceptance criteria.
  ```

Only proceed if a spec is in place.

---

## Planning rules

- Read-only mode during planning — no code changes
- Each task changes one logical thing
- Each task has explicit acceptance criteria and a verification step
- Tasks are ordered by dependency (foundations first)
- No task should touch more than ~5 files
- Prefer vertical slices: each task leaves the system in a working state

## Task format

```
- [ ] Task N: [Short title]
  - What: [One sentence description]
  - Acceptance: [Specific, testable condition]
  - Verify: `.venv/bin/pytest tests/ -q` or [manual check]
  - Files: [list]
  - Size: XS / S / M
```

Size guide: **XS** = 1 file, 1 function | **S** = 1–2 files | **M** = 3–5 files | **L+ = too big, split it**

## Parallelization

Note if any tasks are independent and could run in parallel. Otherwise, order is sequential.

## Checkpoint

Add a checkpoint after every 2–3 tasks:
```
## Checkpoint
- [ ] All tests pass
- [ ] System is in a working state
- [ ] Ready to continue or review
```

## Risks and open questions

List any risks identified during task breakdown, or questions that came up while decomposing the work.

---

## Save the plan

After producing the plan, save it to `docs/plans/plan.md`. Create the `docs/plans/` directory if it does not exist. Confirm the saved path to the user.

This file is the on-disk signal that `/build` checks to verify the workflow was followed. Without it, `/build` will refuse to proceed.
