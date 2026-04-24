---
name: ship
description: Provides a pre-ship checklist, rollback notes, and next steps. Use before declaring a feature ready for demo or production.
---

# /ship — Pre-Ship Checklist

Confirm the change is demo-ready. For this repo "shipping" means: safe to demo live, tests pass, the UI works, and there's a clear rollback path.

---

## Pre-ship checklist

### Code quality
- [ ] All tests pass: `.venv/bin/pytest tests/ -q`
- [ ] No debugging prints or `TODO` left in changed files
- [ ] `/review` passed with no blocking issues

### Behavior
- [ ] The feature works end-to-end through the UI (form → transfer → audit log)
- [ ] Alerts panel renders correctly (empty state or populated)
- [ ] Audit log shows correct events in correct order

### Security (demo-mode standard)
- [ ] No account numbers or routing numbers in visible logs or UI
- [ ] Form inputs reach services as validated types

### Rollout
For this repo: restart `uvicorn app.main:app --reload`.  
No migrations, no DB changes, no infrastructure.

### Rollback
Revert the edited files. Because the store is in-memory, state resets automatically on restart.  
Time to rollback: < 1 minute.

---

## Next steps after ship

State what was implemented, what is still stubbed, and what the natural next task would be.

Example:
```
SHIPPED: suspicious transfer alerting wired up end-to-end
STILL STUBBED: email notification on alert
NATURAL NEXT: add severity filter to alerts panel
```
