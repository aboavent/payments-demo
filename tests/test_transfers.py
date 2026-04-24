from app.services import ach
from app.models import TransferStatus


def test_submit_transfer_stores_transfer():
    t = ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=500.00,
        routing_number="021000021",
        account_number="123456789",
    )
    transfers = ach.list_transfers()
    assert len(transfers) == 1
    assert transfers[0].id == t.id


def test_submit_transfer_default_status_is_pending():
    t = ach.submit_transfer(
        originator="Acme Corp",
        beneficiary="Jane Doe",
        amount=250.00,
        routing_number="021000021",
        account_number="987654321",
    )
    assert t.status == TransferStatus.PENDING


def test_submit_transfer_stores_all_fields():
    t = ach.submit_transfer(
        originator="Originator Inc",
        beneficiary="Bob Smith",
        amount=1_200.50,
        routing_number="011401533",
        account_number="555000111",
        memo="Invoice #99",
    )
    assert t.originator == "Originator Inc"
    assert t.beneficiary == "Bob Smith"
    assert t.amount == 1_200.50
    assert t.routing_number == "011401533"
    assert t.account_number == "555000111"
    assert t.memo == "Invoice #99"


def test_list_transfers_returns_most_recent_first():
    ach.submit_transfer("A", "B", 100, "021000021", "111")
    ach.submit_transfer("C", "D", 200, "021000021", "222")
    transfers = ach.list_transfers()
    assert transfers[0].amount == 200
    assert transfers[1].amount == 100


def test_multiple_transfers_all_stored():
    for i in range(5):
        ach.submit_transfer("Orig", "Ben", float(i * 100), "021000021", str(i))
    assert len(ach.list_transfers()) == 5
