#!/usr/bin/env bash
# Resets the demo to its baseline state.
# Run this between demo sessions to restore the extension point stubs.
# Usage: bash scripts/demo-reset.sh
#
# What this script resets:
#   LOCAL:
#     - Stops uvicorn (port 8000)
#     - Force-switches to main branch (discards uncommitted changes)
#     - Restores app/services/ach.py and app/services/alerts.py to commented-out state
#     - Removes tests/test_alerts.py (belongs to the feature, not the baseline)
#     - Removes .github/ (created live during /devsecops-audit — must not exist at demo start)
#     - Deletes the local devsecops-hardening branch
#   REMOTE (GitHub):
#     - Closes any open PR for devsecops-hardening
#     - Deletes the remote devsecops-hardening branch
#     (origin/main is never touched — it is always the stable baseline)
#
# After this script: origin/main and local main are identical and in baseline state.
# You do NOT need to delete and recreate the GitHub repo between runs.

export PATH="$HOME/bin:$PATH"
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

echo "==> Switching to main branch (force, discards any uncommitted changes)..."
git checkout -f main

echo "==> Removing .github/ (Act 4 DevSecOps demo — Claude creates this live)..."
rm -rf .github/

echo "==> Closing any open PR for devsecops-hardening on GitHub..."
set +e   # gh/git failures here are expected when branch/PR don't exist yet
PR_NUMBER=$(gh pr list --head devsecops-hardening --state open --json number --jq '.[].number' 2>/dev/null)
if [ -n "$PR_NUMBER" ]; then
    gh pr close "$PR_NUMBER" --comment "Reset for next demo run." && echo "    PR #$PR_NUMBER closed" || echo "    PR close failed (continuing)"
else
    echo "    no open PR found"
fi

echo "==> Deleting remote branch devsecops-hardening (if exists)..."
git push origin --delete devsecops-hardening 2>/dev/null && echo "    deleted" || echo "    not found on remote"

echo "==> Deleting local branch devsecops-hardening (if exists)..."
git branch -D devsecops-hardening 2>/dev/null && echo "    deleted" || echo "    not found locally"
set -e

echo "==> Running tests to confirm baseline..."
.venv/bin/pytest tests/ -q --tb=short

echo ""
echo "✓ Demo reset complete. GitHub is clean — no open PRs, no feature branch."
echo "  Start the server with: uvicorn app.main:app"
