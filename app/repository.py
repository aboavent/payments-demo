from app.models import Transfer, Alert, AuditEvent

# In-memory store — swap for SQLite/Postgres by replacing these lists
_transfers: list[Transfer] = []
_alerts: list[Alert] = []
_audit_events: list[AuditEvent] = []


# --- Transfers ---

def save_transfer(transfer: Transfer) -> Transfer:
    _transfers.append(transfer)
    return transfer


def list_transfers(limit: int = 50) -> list[Transfer]:
    return list(reversed(_transfers))[:limit]


def get_transfer(transfer_id: str) -> Transfer | None:
    return next((t for t in _transfers if t.id == transfer_id), None)


# --- Alerts ---

def save_alert(alert: Alert) -> Alert:
    _alerts.append(alert)
    return alert


def list_alerts(limit: int = 50) -> list[Alert]:
    return list(reversed(_alerts))[:limit]


# --- Audit Events ---

def save_audit_event(event: AuditEvent) -> AuditEvent:
    _audit_events.append(event)
    return event


def list_audit_events(limit: int = 100) -> list[AuditEvent]:
    return list(reversed(_audit_events))[:limit]


# --- Test helpers ---

def _clear_all() -> None:
    """Reset all stores; used only in tests."""
    _transfers.clear()
    _alerts.clear()
    _audit_events.clear()
