from app.models import AuditEvent
from app import repository


def log(action: str, detail: str, transfer_id: str | None = None) -> AuditEvent:
    event = AuditEvent(action=action, detail=detail, transfer_id=transfer_id)
    return repository.save_audit_event(event)


def list_events(limit: int = 100) -> list[AuditEvent]:
    return repository.list_audit_events(limit=limit)
