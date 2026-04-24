## Summary
<!-- What changed and why -->

## Test plan
- [ ] Tests pass locally: `pytest tests/ -q`
- [ ] New behavior tested manually in the UI
- [ ] No account numbers or routing numbers in logs

## Security checklist
- [ ] No sensitive fields exposed in error messages or logs
- [ ] Input validation at the route boundary (not deep in services)
- [ ] No new dependencies added without review

## Rollback
<!-- How to undo this change: revert files + server restart / migration rollback -->
