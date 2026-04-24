from app.models import Alert, AlertSeverity
from app import repository


def create_alert(
    title: str,
    message: str,
    severity: AlertSeverity = AlertSeverity.INFO,
    transfer_id: str | None = None,
) -> Alert:
    alert = Alert(title=title, message=message, severity=severity, transfer_id=transfer_id)
    return repository.save_alert(alert)


def list_alerts(limit: int = 50) -> list[Alert]:
    return repository.list_alerts(limit=limit)


def check_suspicious_transfer(transfer) -> Alert | None:
    return None
