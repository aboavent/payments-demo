from app.services import ach, alerts
from app.config import SUSPICIOUS_TRANSFER_THRESHOLD
from app.models import AlertSeverity


def test_suspicious_transfer_creates_alert():
    ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=SUSPICIOUS_TRANSFER_THRESHOLD + 1,
        routing_number="021000021",
        account_number="123456789",
    )
    alert_list = alerts.list_alerts()
    assert len(alert_list) == 1
    assert alert_list[0].severity == AlertSeverity.WARNING
    assert alert_list[0].title == "Suspicious Transfer Detected"


def test_below_threshold_no_alert():
    ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=SUSPICIOUS_TRANSFER_THRESHOLD - 1,
        routing_number="021000021",
        account_number="123456789",
    )
    assert len(alerts.list_alerts()) == 0


def test_alert_message_excludes_sensitive_fields():
    account = "123456789"
    routing = "021000021"
    ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=SUSPICIOUS_TRANSFER_THRESHOLD + 1,
        routing_number=routing,
        account_number=account,
    )
    alert_list = alerts.list_alerts()
    assert len(alert_list) == 1
    assert account not in alert_list[0].message
    assert routing not in alert_list[0].message
