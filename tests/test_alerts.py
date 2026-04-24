from app.models import AlertSeverity
from app.services import ach, alerts


def test_transfer_at_threshold_creates_alert():
    transfer = ach.submit_transfer(
        originator="Alice", beneficiary="Bob",
        amount=10_000.00, routing_number="021000021", account_number="123456789",
    )
    all_alerts = alerts.list_alerts()
    assert len(all_alerts) == 1
    assert all_alerts[0].severity == AlertSeverity.WARNING
    assert all_alerts[0].transfer_id == transfer.id


def test_transfer_above_threshold_creates_alert():
    transfer = ach.submit_transfer(
        originator="Alice", beneficiary="Bob",
        amount=15_000.00, routing_number="021000021", account_number="123456789",
    )
    all_alerts = alerts.list_alerts()
    assert len(all_alerts) == 1
    assert all_alerts[0].transfer_id == transfer.id


def test_transfer_below_threshold_creates_no_alert():
    ach.submit_transfer(
        originator="Alice", beneficiary="Bob",
        amount=9_999.00, routing_number="021000021", account_number="123456789",
    )
    assert alerts.list_alerts() == []
