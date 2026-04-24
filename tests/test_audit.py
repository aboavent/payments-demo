from app.services import ach, audit


def test_submit_transfer_creates_audit_event():
    ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=300.00,
        routing_number="021000021",
        account_number="123456789",
    )
    events = audit.list_events()
    assert len(events) == 1
    assert events[0].action == "transfer_submitted"


def test_audit_event_references_transfer_id():
    t = ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=300.00,
        routing_number="021000021",
        account_number="123456789",
    )
    events = audit.list_events()
    assert events[0].transfer_id == t.id


def test_audit_event_detail_contains_amount():
    ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=9_999.99,
        routing_number="021000021",
        account_number="123456789",
    )
    events = audit.list_events()
    assert "9,999.99" in events[0].detail


def test_manual_audit_log():
    event = audit.log("manual_action", "Operator reviewed transfer queue.")
    events = audit.list_events()
    assert len(events) == 1
    assert events[0].action == "manual_action"
    assert events[0].id == event.id


def test_audit_events_returned_most_recent_first():
    audit.log("first_event", "detail a")
    audit.log("second_event", "detail b")
    events = audit.list_events()
    assert events[0].action == "second_event"
    assert events[1].action == "first_event"
