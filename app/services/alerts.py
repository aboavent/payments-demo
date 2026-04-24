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
    # --- DEMO EXTENSION POINT ---
    # Uncomment to enable suspicious transfer alerting:
    # from app.config import SUSPICIOUS_TRANSFER_THRESHOLD
    # if transfer.amount >= SUSPICIOUS_TRANSFER_THRESHOLD:
    #     return create_alert(
    #         title="Suspicious Transfer Detected",
    #         message=f"Transfer of ${transfer.amount:,.2f} from '{transfer.originator}' exceeds threshold.",
    #         severity=AlertSeverity.WARNING,
    #         transfer_id=transfer.id,
    #     )
    return None
