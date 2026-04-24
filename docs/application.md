# Application Documentation

## What it is

**ACH Transfer Operations Portal** is a small internal fintech operations tool built as a live demo application. It simulates what a real payments back-office UI might look like: operators submit ACH transfers, watch them appear in a recent transfers table, see alerts, and browse an audit trail.

It is intentionally simple — the point is to be readable, extendable, and demonstrable, not production-grade.

---

## Tech stack

| Layer | Technology |
|---|---|
| Web framework | FastAPI (Python 3.11+) |
| Templates | Jinja2 |
| Styling | Plain CSS (no framework) |
| Persistence | In-memory Python lists |
| Tests | pytest |
| Dev server | uvicorn with `--reload` |

No database. No auth. No background jobs. No Docker required.

---

## Project structure

```
payments-demo/
├── app/
│   ├── main.py          # FastAPI app — mounts static files, includes router
│   ├── config.py        # App-wide config (SUSPICIOUS_TRANSFER_THRESHOLD lives here)
│   ├── models.py        # Transfer, Alert, AuditEvent dataclasses + status enums
│   ├── repository.py    # In-memory store (_transfers, _alerts, _audit_events lists)
│   ├── routes.py        # HTTP routes: GET / and POST /transfers
│   └── services/
│       ├── ach.py       # Transfer submission logic        ← DEMO EXTENSION POINT
│       ├── alerts.py    # Alert creation + check_suspicious_transfer() stub
│       └── audit.py     # Audit event logging
├── templates/
│   ├── base.html        # Header, footer, CSS link
│   └── index.html       # Single-page UI: form + table + alerts + audit log
├── static/
│   └── styles.css       # ~260 lines of plain CSS
├── tests/
│   ├── conftest.py      # autouse clear_store fixture (shared)
│   ├── test_transfers.py
│   └── test_audit.py
├── docs/                # This folder
├── CLAUDE.md            # Claude Code instructions (project constitution)
├── README.md
└── requirements.txt
```

---

## Data models

All models are plain Python dataclasses in `app/models.py`. No ORM.

### Transfer

Represents a single ACH transfer submission.

| Field | Type | Notes |
|---|---|---|
| `id` | `str` | UUID, auto-generated |
| `originator` | `str` | Sending party name |
| `beneficiary` | `str` | Receiving party name |
| `amount` | `float` | USD amount |
| `routing_number` | `str` | 9-digit ABA routing number |
| `account_number` | `str` | Destination account number |
| `memo` | `str` | Optional free-text memo |
| `status` | `TransferStatus` | `pending` / `processed` / `failed` |
| `created_at` | `datetime` | UTC, set at creation |

**TransferStatus enum:** `PENDING`, `PROCESSED`, `FAILED`

### Alert

Represents an operational alert surfaced in the UI.

| Field | Type | Notes |
|---|---|---|
| `id` | `str` | UUID, auto-generated |
| `title` | `str` | Short alert title |
| `message` | `str` | Full alert message |
| `severity` | `AlertSeverity` | `info` / `warning` / `critical` |
| `transfer_id` | `str \| None` | Links alert to a transfer if applicable |
| `created_at` | `datetime` | UTC |

**AlertSeverity enum:** `INFO`, `WARNING`, `CRITICAL`

### AuditEvent

Immutable record of every significant action.

| Field | Type | Notes |
|---|---|---|
| `id` | `str` | UUID |
| `action` | `str` | Machine-readable event name (e.g. `transfer_submitted`) |
| `detail` | `str` | Human-readable description |
| `transfer_id` | `str \| None` | Links event to a transfer |
| `created_at` | `datetime` | UTC |

---

## Repository layer

`app/repository.py` holds three module-level Python lists as the in-memory store:

```python
_transfers:    list[Transfer]
_alerts:       list[Alert]
_audit_events: list[AuditEvent]
```

All service functions call repository functions — services never touch the lists directly.

**To swap for a real database:** replace the list operations in `repository.py` with SQLAlchemy/SQLite calls. Nothing outside `repository.py` needs to change.

`_clear_all()` is a test helper that empties all three stores. It is called by the `clear_store` fixture in `tests/conftest.py`.

---

## Service layer

### `app/services/ach.py` — Transfer processing

`submit_transfer(...)` is the main entry point:
1. Constructs a `Transfer` dataclass
2. Saves it via `repository.save_transfer()`
3. Writes an audit event via `audit.log()`
4. **(Stub)** Would call `check_suspicious_transfer()` — see extension point below

`list_transfers(limit)` returns transfers newest-first.

### `app/services/alerts.py` — Alert management

`create_alert(title, message, severity, transfer_id)` creates and stores an `Alert`.

`list_alerts(limit)` returns alerts newest-first.

`check_suspicious_transfer(transfer)` — **written but commented out**. This is the demo extension point.

### `app/services/audit.py` — Audit logging

`log(action, detail, transfer_id)` creates and stores an `AuditEvent`.

`list_events(limit)` returns events newest-first.

---

## Routes

`app/routes.py` has two routes:

| Method | Path | What it does |
|---|---|---|
| `GET` | `/` | Renders `index.html` with transfers, alerts, and audit events |
| `POST` | `/transfers` | Accepts form data, calls `ach.submit_transfer()`, redirects to `/` |

The redirect after POST follows the standard POST-Redirect-GET pattern to prevent form resubmission on refresh.

---

## UI

Single page (`templates/index.html`) with a two-column layout:

**Left column**
- ACH transfer submission form (originator, beneficiary, amount, routing number, account number, memo)
- Alerts panel (shows `Alert` objects; empty state: "No active alerts.")

**Right column**
- Recent transfers table (ID prefix, originator, beneficiary, amount, status badge, time)
- Audit log (action name, time, detail text)

All styling is in `static/styles.css`. Status badges are color-coded: pending = amber, processed = green, failed = red. Alert items are color-coded by severity.

---

## Config values

`app/config.py`:

```python
APP_TITLE = "ACH Transfer Operations Portal"
APP_VERSION = "1.0.0"

SUSPICIOUS_TRANSFER_THRESHOLD: float = 10_000.00
```

`SUSPICIOUS_TRANSFER_THRESHOLD` is live — the value is set. The logic that reads it is commented out (see extension point below).

---

## Current behavior (what is implemented)

1. Operator fills out the transfer form and submits
2. A `Transfer` is created with status `PENDING` and stored in memory
3. An `AuditEvent` with action `transfer_submitted` is created and stored
4. The page reloads showing the new transfer in the table and the new audit event in the log
5. The alerts panel exists and will render any alerts that exist — currently always empty

---

## Extension point — Suspicious transfer alerting

This feature is **intentionally not wired up**. It is the live demo addition.

### What already exists

| Location | What's there |
|---|---|
| `app/config.py:6` | `SUSPICIOUS_TRANSFER_THRESHOLD = 10_000.00` — value is live |
| `app/services/alerts.py:19–32` | `check_suspicious_transfer()` — complete function body, commented out |
| `app/services/ach.py:31–33` | `# DEMO EXTENSION POINT` comment + two commented-out lines |
| `templates/index.html` | Alerts panel already renders any alerts in the store |

### What the two-line activation looks like

In `app/services/ach.py`, after the audit log call:

```python
# --- DEMO EXTENSION POINT ---
# Uncomment to enable suspicious transfer alerting:
# from app.services.alerts import check_suspicious_transfer
# check_suspicious_transfer(transfer)
```

Uncomment those two lines. That's the entire wiring change.

In `app/services/alerts.py`, uncomment the `check_suspicious_transfer` function body (lines 19–32). That function reads `SUSPICIOUS_TRANSFER_THRESHOLD` from config and calls `create_alert()` with `AlertSeverity.WARNING`.

**No template, model, repository, or route changes needed.**

---

## What is intentionally not implemented

| Feature | Reason not implemented |
|---|---|
| Suspicious transfer alerting | Reserved for live demo addition |
| Authentication / authorization | Out of scope for demo |
| Persistent storage (DB) | In-memory is sufficient; DB swap point is marked in repository.py |
| Transfer status updates | Transfers stay `PENDING`; status progression is a natural next feature |
| Email / webhook notifications | Out of scope for demo |
| Pagination controls in UI | Limits are set server-side (50 transfers, 100 audit events) |
