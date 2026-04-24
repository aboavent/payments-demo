---
name: spec
description: Creates a concise implementation spec before coding. Use when starting any non-trivial change, when requirements are ambiguous, or when the task touches more than one file.
---

# /spec — Implementation Specification

Write a structured spec before writing any code. The spec is the shared source of truth. Code without a spec is guessing.

**Do not write implementation code.** Output only the spec.

---

## When to use full spec mode

- More than one file will change
- Requirements are ambiguous or incomplete
- Medium/high-risk change (data model, alerting, audit, routing)
- The task would take more than a few minutes to implement

## When to use lightweight spec mode

For small, low-risk, single-file changes, produce only:
- **Constraints:** what must not change
- **Success criteria:** what must be true when done

---

## Full Spec Output Format

**Problem statement**  
One or two sentences: what is broken or missing, and why it matters.

**Scope**  
What this change covers.

**Non-goals**  
What this change explicitly does not touch. Be specific.

**Files affected**

| File | Change type | Why |
|---|---|---|
| `app/...` | modify / add / delete | reason |

**Acceptance criteria**
- [ ] Observable, testable outcome
- [ ] Observable, testable outcome

**Test plan**  
Which test cases to add or update, and what each asserts.

**Rollout / rollback**  
For this repo: restart `uvicorn`. Rollback: revert the edit. Note any data state that would be affected.

**Risks and assumptions**  
List each assumption and any non-obvious risk introduced by the change.

**Open questions**  
Anything that must be resolved before implementation begins.

---

## Surface assumptions immediately

Before writing spec content, list what you're assuming:

```
ASSUMPTIONS I'M MAKING:
1. [assumption]
2. [assumption]
→ Correct me or I'll proceed with these.
```

Don't silently fill in ambiguities. The spec's value is in surfacing misunderstandings *before* code gets written.

---

## Save the spec

After producing the spec, save it to `docs/specs/<name>.md` where `<name>` is derived from the task description (lowercase, hyphens, no special characters — e.g. "add suspicious transfer alerting" → `suspicious-transfer-alerting.md`). Create the `docs/specs/` directory if it does not exist. Confirm the saved file path to the user.
