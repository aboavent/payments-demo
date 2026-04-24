from app.services import ach, alerts
from app.models import AlertSeverity


def test_transfer_at_threshold_creates_alert():
    t = ach.submit_transfer("Acme Corp", "Jane Doe", 10_000.00, "021000021", "123456789")
    result = alerts.list_alerts()
    assert len(result) == 1
    assert result[0].severity == AlertSeverity.WARNING
    assert result[0].transfer_id == t.id


def test_transfer_above_threshold_creates_alert():
    ach.submit_transfer("Acme Corp", "Jane Doe", 15_000.00, "021000021", "123456789")
    result = alerts.list_alerts()
    assert len(result) == 1
    assert result[0].severity == AlertSeverity.WARNING


def test_transfer_below_threshold_creates_no_alert():
    ach.submit_transfer("Acme Corp", "Jane Doe", 9_999.00, "021000021", "123456789")
    assert alerts.list_alerts() == []
