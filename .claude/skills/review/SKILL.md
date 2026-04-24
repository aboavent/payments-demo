---
name: review
description: Multi-axis review of a change. Use before reporting any non-trivial task complete, or when asked to review a diff.
---

# /review — Change Review

Review the current change on five axes. Flag real issues directly — don't soften them. Don't rubber-stamp.

**Do not rewrite code.** Report findings and recommended actions only.

---

## Review axes

### Correctness
- Does the logic do what the spec or task requires?
- Are edge cases handled (empty inputs, zero amounts, missing fields)?
- Are error paths handled — not just the happy path?
- Do tests actually cover the changed behavior?

### Security / Compliance
*(This is a fintech demo — treat it seriously even in demo mode)*
- Are account numbers or routing numbers appearing in logs, audit details, or error messages?
- Are inputs validated at the boundary (`routes.py`) before reaching service logic?
- Would a real compliance review flag anything here?

### Maintainability
- Is the change consistent with existing patterns (dataclasses, service functions, route structure)?
- Does it introduce a new pattern without justification?
- Is there unnecessary complexity or abstraction?
- Would a new team member understand this without asking?

### Operational risk
- Could this cause silent failures or data loss in the in-memory store?
- Do audit events still fire correctly after this change?
- Is there a clear rollback path (revert the edit)?
- Does the change behave correctly after a server restart (i.e., no hidden persistent state)?

### Assumptions and scope
- Did the implementation stay within the approved spec?
- Are there any assumptions baked in that weren't surfaced during Refinement?
- Did scope creep in silently?

---

## Output format

For each axis: **OK** / **Note** / **Risk** + one-line explanation.

```
Correctness:     OK — logic matches spec, edge cases covered
Security:        Note — routing number appears in audit detail; acceptable for demo
Maintainability: OK — follows existing service pattern
Operational:     Risk — if X happens, Y will silently fail
Assumptions:     Note — assumed Z; should confirm with requester
```

**Recommended next actions** — short list of concrete steps.  
**Blocking issues** — anything that must be fixed before this is demo-ready (may be empty).
