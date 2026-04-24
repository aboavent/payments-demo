# Spec: Add Suspicious Transfer Alerting

## Problem statement
Suspicious transfer alerting exists as a stub but is inactive — `check_suspicious_transfer()` returns `None` unconditionally and is never called. Transfers above $10,000 are processed with no alert raised, leaving fraud detection dormant.

## Scope
Implement threshold-based alerting in `alerts.py` and wire the call into `ach.py`.

## Non-goals
- No changes to `config.py`, `models.py`, `repository.py`, `routes.py`, or any template
- No email or external notification
- No UI changes — the alerts panel already renders whatever is in the store
- No change to the threshold value

## Files affected

| File | Change type | Why |
|---|---|---|
| `app/services/alerts.py` | modify | Implement `check_suspicious_transfer()` — read threshold, create WARNING alert if exceeded |
| `app/services/ach.py` | modify | Import and call `check_suspicious_transfer(transfer)` after the audit log |
| `tests/test_alerts.py` | add | Tests for above/below/at-threshold behavior |

## Acceptance criteria
- [ ] Transfer >= $10,000 creates a `WARNING` alert visible in the UI alerts panel
- [ ] Transfer < $10,000 creates no alert
- [ ] Transfer of exactly $10,000 creates an alert (boundary: `>=`)
- [ ] All existing 10 tests still pass
- [ ] Alert message contains no account number or routing number

## Test plan
In `tests/test_alerts.py`:
- `test_alert_created_above_threshold` — $15,000 transfer → 1 alert, severity `WARNING`
- `test_no_alert_below_threshold` — $5,000 transfer → 0 alerts
- `test_alert_created_at_threshold` — $10,000 transfer → 1 alert

## Rollout / rollback
Rollout: restart `uvicorn app.main:app`. No migrations, no persistent state.
Rollback: revert `ach.py` and `alerts.py`. Store resets on restart.

## Risks and assumptions
- `check_suspicious_transfer` return value is unused in `ach.py` — fire-and-forget, correct by design.
- `clear_store` fixture is `autouse=True` in `conftest.py` — test isolation is automatic.
- Threshold imported from `app.config.SUSPICIOUS_TRANSFER_THRESHOLD` — no magic numbers.

## Open questions
None.
