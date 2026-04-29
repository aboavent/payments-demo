from app.services import ach, alerts
from app.models import AlertSeverity


def test_suspicious_transfer_creates_alert():
    ach.submit_transfer("Acme Corp", "Jane Doe", 25_000.00, "021000021", "123456789")
    result = alerts.list_alerts()
    assert len(result) == 1
    assert result[0].severity == AlertSeverity.WARNING


def test_transfer_below_threshold_no_alert():
    ach.submit_transfer("Acme Corp", "Jane Doe", 24_999.99, "021000021", "123456789")
    assert len(alerts.list_alerts()) == 0


def test_alert_links_to_transfer():
    t = ach.submit_transfer("Acme Corp", "Jane Doe", 25_000.00, "021000021", "123456789")
    result = alerts.list_alerts()
    assert result[0].transfer_id == t.id
