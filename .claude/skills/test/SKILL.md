---
name: test
description: Runs or proposes the right tests and summarizes results. Use after implementing a change, or when assessing test coverage for a service or feature.
---

# /test — Test Runner and Coverage Summary

Run the test suite and report what is and isn't covered. For new features, propose the test cases that should exist.

---

## Run tests

```bash
.venv/bin/pytest tests/ -v --tb=short
```

Report:
- Total: N passed / N failed / N warnings
- Any failures: test name, assertion, root cause
- Time taken

## Coverage check (when proposing new tests)

For the changed or reviewed code, answer:

| Scenario | Covered? | Test name or proposed name |
|---|---|---|
| Happy path | yes / no | `test_...` |
| Edge case: [describe] | yes / no | `test_...` |
| Error case: [describe] | yes / no | `test_...` |

## Test writing guidelines (for this repo)

- Tests live in `tests/`. The shared fixture is in `tests/conftest.py` — do not add `clear_store` to individual test files.
- Test behavior, not implementation details.
- Use plain `assert` — no testing framework magic.
- Keep test data minimal and readable.
- Test names should read as sentences: `test_submit_transfer_creates_audit_event`.

## When tests are already sufficient

Say so clearly: "Existing coverage is adequate for this change. No new tests needed."

Do not add redundant tests for the sake of having more tests.
