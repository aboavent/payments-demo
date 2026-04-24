from app.models import Transfer
from app import repository
from app.services import audit


def submit_transfer(
    originator: str,
    beneficiary: str,
    amount: float,
    routing_number: str,
    account_number: str,
    memo: str = "",
) -> Transfer:
    transfer = Transfer(
        originator=originator,
        beneficiary=beneficiary,
        amount=amount,
        routing_number=routing_number,
        account_number=account_number,
        memo=memo,
    )
    repository.save_transfer(transfer)

    audit.log(
        action="transfer_submitted",
        detail=f"ACH transfer of ${amount:,.2f} from '{originator}' to '{beneficiary}' submitted.",
        transfer_id=transfer.id,
    )

    from app.services.alerts import check_suspicious_transfer
    check_suspicious_transfer(transfer)

    return transfer


def list_transfers(limit: int = 50) -> list[Transfer]:
    return repository.list_transfers(limit=limit)
