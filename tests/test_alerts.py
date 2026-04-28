from app.services import ach, alerts
from app.models import AlertSeverity
from app.config import SUSPICIOUS_TRANSFER_THRESHOLD


def test_suspicious_transfer_creates_alert():
    ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=SUSPICIOUS_TRANSFER_THRESHOLD + 1,
        routing_number="021000021",
        account_number="123456789",
    )
    active_alerts = alerts.list_alerts()
    assert len(active_alerts) == 1
    assert active_alerts[0].severity == AlertSeverity.WARNING


def test_normal_transfer_no_alert():
    ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=500.00,
        routing_number="021000021",
        account_number="123456789",
    )
    assert len(alerts.list_alerts()) == 0
