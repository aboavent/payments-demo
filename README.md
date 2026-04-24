# ACH Transfer Operations Portal

Internal fintech operations demo — submit ACH transfers, view recent activity, monitor alerts, and browse the audit log.

## Setup

```bash
cd payments-demo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open http://localhost:8000 in your browser.

## Run Tests

```bash
pytest
```

Or with verbose output:

```bash
pytest -v
```

## Project Structure

```
payments-demo/
├── app/
│   ├── main.py          # FastAPI app entrypoint
│   ├── config.py        # App-wide config values
│   ├── models.py        # Transfer, Alert, AuditEvent dataclasses
│   ├── repository.py    # In-memory storage (swap for DB here)
│   ├── routes.py        # HTTP routes
│   └── services/
│       ├── ach.py       # ACH transfer submission logic
│       ├── alerts.py    # Alert creation and listing
│       └── audit.py     # Audit event logging and listing
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── styles.css
└── tests/
    ├── test_transfers.py
    └── test_audit.py
```

## Extension Points: Suspicious Transfer Alerting

Two uncommenting steps wire in threshold-based alerting end-to-end:

1. **`app/services/alerts.py`** — uncomment `check_suspicious_transfer()`. It compares the transfer amount against `SUSPICIOUS_TRANSFER_THRESHOLD` (set to `$10,000` in `app/config.py`) and calls `create_alert()` when the threshold is met.

2. **`app/services/ach.py`** — uncomment the two lines inside `submit_transfer()` marked `DEMO EXTENSION POINT` that import and call `check_suspicious_transfer(transfer)`.

No other changes are needed. `SUSPICIOUS_TRANSFER_THRESHOLD` is already live in `app/config.py`, and the alerts panel in the UI already renders any alerts in the store.
