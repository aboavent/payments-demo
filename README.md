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
uvicorn app.main:app
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

## Extension Point: Suspicious Transfer Alerting

The suspicious transfer alerting feature is intentionally incomplete and is built live during Act 3 of the demo.

**Baseline state (what exists at reset):**
- `app/config.py` — `SUSPICIOUS_TRANSFER_THRESHOLD = 10_000.00` (live value)
- `app/services/alerts.py` — `check_suspicious_transfer(transfer)` returns `None` (stub, no logic)
- `app/services/ach.py` — does not import or call `check_suspicious_transfer`
- `templates/index.html` — alerts panel already renders any alerts in the store

**What the demo builds live (Act 3):**
1. `/spec add suspicious transfer alerting` — produces a structured spec
2. `/plan` — breaks work into atomic tasks
3. `/build task 1` — implements threshold check in `alerts.py`
4. `/build task 2` — wires the call into `ach.py`

No manual code editing. The feature is implemented live by Claude Code through the full spec → plan → build → review → ship workflow. See `docs/demo-guide.md` Act 3 for the full walkthrough.
