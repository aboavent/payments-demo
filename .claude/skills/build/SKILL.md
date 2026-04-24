---
name: build
description: Implements one approved task slice with minimal, targeted edits. Use after /plan is approved to implement a single task from the plan.
---

# /build — Incremental Implementation

Implement the specified task from the approved plan. One task at a time. Leave the system in a working state after every change.

---

## Workflow gate — check before doing anything

Before implementing, verify the workflow was followed:

1. **Spec exists?** Check `docs/specs/` for a relevant spec file.
   - If no spec file exists → stop and respond:
     ```
     ⛔ No spec found in docs/specs/.
     The 4-phase workflow requires a spec before implementation.
     Run /spec first to define the scope and acceptance criteria.
     ```

2. **Plan exists?** Check for `docs/plans/plan.md` on disk.
   - If the file does not exist → stop and respond:
     ```
     ⛔ No plan found in docs/plans/plan.md.
     The 4-phase workflow requires a plan before implementation.
     Run /plan to break the spec into verifiable tasks before building.
     ```

Only proceed if both a spec and a plan are in place.

---

## Before writing code

- State which task from the plan you're implementing
- List exactly which files will change and why
- Confirm the acceptance criteria you're targeting

## Implementation rules

**Surgical changes only.** Touch only what the task requires.
- Do not improve adjacent code unless asked — mention it instead
- Do not add features not in the approved spec
- Match existing style in this repo (dataclasses, service functions, route pattern)
- Remove any imports or variables that *your* changes make unused; leave pre-existing dead code alone

**Simplicity first.**
- Write the minimum code that satisfies the acceptance criteria
- No abstractions for single-use code
- No speculative configurability
- If it can be done in fewer lines without losing clarity, do it that way

**Keep it compiling.**  
After every file change, the project must build and existing tests must pass.

## After each file change

1. Run `.venv/bin/pytest tests/ -q --tb=short`
2. If tests fail, fix before moving on — don't accumulate broken state
3. Report: what changed, which tests passed, what's next
4. Write the build marker: `echo "build complete" > docs/plans/build.done`

## Scope creep check

If you notice something worth improving outside the task scope, say so:
```
NOTICED BUT NOT TOUCHING: [description]
→ Want me to create a follow-up task?
```

Do not silently expand scope.
