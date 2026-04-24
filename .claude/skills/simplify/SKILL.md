---
name: simplify
description: Identifies unnecessary complexity and proposes simpler alternatives. Use after a feature works and tests pass, when code feels heavier than it needs to be.
---

# /simplify — Complexity Review

Find what is more complex than it needs to be and propose simpler alternatives. Preserve behavior exactly.

**Do not change behavior.** Simplification that requires modifying tests to pass has changed behavior — stop and reconsider.

---

## Before simplifying anything

Apply Chesterton's Fence: understand why the code is the way it is before removing or changing it.

```
BEFORE TOUCHING ANYTHING, ANSWER:
- What is this code's responsibility?
- What calls it? What does it call?
- Is there a test that defines the expected behavior?
- Why might it have been written this way?
```

If you can't answer these, read more context first.

---

## What to look for in this repo

| Pattern | Signal | What to do |
|---|---|---|
| Service function doing two things | Long function with two distinct responsibilities | Split or clarify |
| Commented-out dead code | Orphaned comments or stubs | Remove if clearly unused |
| Generic variable names | `data`, `result`, `item` without context | Rename to describe content |
| Redundant re-imports | Same module imported in two styles | Consolidate |
| Over-qualified type annotations | Annotation that adds no information | Simplify or remove |
| Abstraction used once | Helper function called exactly once, adds no clarity | Inline it |

---

## Output format

For each candidate:
```
FILE: app/services/ach.py, line N
ISSUE: [description]
BEFORE: [current code]
AFTER: [proposed simplification]
BEHAVIOR PRESERVED: yes / needs verification
```

Then:  
**Recommended:** which simplifications to apply (and in what order)  
**Skip:** which ones are fine as-is or risky to change

---

## Rules

- Scope to changed or recently modified code by default
- Do not simplify unrelated files unless explicitly asked
- Do not reduce line count at the expense of readability
- Do not remove abstractions that exist for testability
- Submit simplifications separately from feature changes
