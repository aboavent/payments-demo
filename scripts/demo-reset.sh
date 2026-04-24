#!/usr/bin/env bash
# Resets the demo to its baseline state.
# Run this between demo sessions to restore the extension point stubs.
# Usage: bash scripts/demo-reset.sh

set -e
cd "$(dirname "$0")/.."

echo "==> Stopping uvicorn (if running)..."
kill $(lsof -ti :8000) 2>/dev/null && echo "    stopped" || echo "    not running"

echo "==> Restoring app/services/ach.py..."
cat > app/services/ach.py << 'EOF'
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

    # --- DEMO EXTENSION POINT ---
    # Uncomment to enable suspicious transfer alerting:
    # from app.services.alerts import check_suspicious_transfer
    # check_suspicious_transfer(transfer)

    return transfer


def list_transfers(limit: int = 50) -> list[Transfer]:
    return repository.list_transfers(limit=limit)
EOF

echo "==> Restoring app/services/alerts.py..."
cat > app/services/alerts.py << 'EOF'
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
EOF

echo "==> Removing test_alerts.py (belongs to the feature, not the baseline)..."
rm -f tests/test_alerts.py

echo "==> Removing .github/ (Act 4 DevSecOps demo — Claude creates this live)..."
rm -rf .github/

echo "==> Running tests to confirm baseline..."
.venv/bin/pytest tests/ -q --tb=short

echo ""
echo "✓ Demo reset complete. Start the server with:"
echo "  uvicorn app.main:app"
