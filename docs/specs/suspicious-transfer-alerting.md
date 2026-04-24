# Spec: Add Suspicious Transfer Alerting

## Assumptions

1. The existing commented-out stubs are the complete intended implementation — no redesign needed
2. Severity stays `WARNING` for all transfers at or above the threshold
3. No additional audit event is needed for alert creation — `transfer_submitted` already covers it
4. No UI or template changes needed — the alerts panel already renders any alerts in the store

---

## Problem statement

When a transfer is submitted at or above `SUSPICIOUS_TRANSFER_THRESHOLD` ($10,000), no alert is raised. Operators have no automated visibility into high-value transfers. Two prepared stubs exist but are commented out — uncommenting them closes the gap.

## Scope

Activate the two existing stubs: `check_suspicious_transfer()` in `alerts.py` and its call site in `ach.py`. No new logic is written.

## Non-goals

- No new models, routes, or templates
- No change to threshold value or severity levels
- No audit event specific to alert creation
- No email, webhook, or any external notification
- No UI changes — alerts panel already works

## Files affected

| File | Change type | Why |
|---|---|---|
| `app/services/alerts.py` | modify | Uncomment `check_suspicious_transfer()` body |
| `app/services/ach.py` | modify | Uncomment the import and call site |

## Acceptance criteria

- [ ] Submitting a transfer of exactly $10,000 creates a `WARNING` alert visible in the UI
- [ ] Submitting a transfer of $10,001 also creates a `WARNING` alert
- [ ] Submitting a transfer of $9,999 creates no alert
- [ ] Audit event still fires on every transfer regardless of amount
- [ ] All existing tests still pass

## Test plan

New file `tests/test_alerts.py`:
- `test_transfer_at_threshold_creates_alert` — submit $10,000, assert one `WARNING` alert linked to the transfer id
- `test_transfer_above_threshold_creates_alert` — submit $15,000, assert alert created
- `test_transfer_below_threshold_creates_no_alert` — submit $9,999, assert no alerts exist

## Rollout / rollback

**Rollout:** restart `uvicorn app.main:app`. No migrations, no state changes.
**Rollback:** re-comment the two lines in `ach.py` and the function body in `alerts.py`. Server restart resets in-memory state.

## Risks and assumptions

- `float` comparison (`amount >= threshold`) is sufficient for a demo; a production system would use `Decimal`
- Alert message includes originator name and full amount — consistent with existing audit log pattern

## Open questions

None. Implementation is fully defined by the existing stubs. Ready for `/plan`.
