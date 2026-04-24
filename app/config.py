APP_TITLE = "ACH Transfer Operations Portal"
APP_VERSION = "1.0.0"

# Transfers at or above this amount will trigger a suspicious transfer alert.
# Used by app/services/alerts.py — see check_suspicious_transfer().
SUSPICIOUS_TRANSFER_THRESHOLD: float = 10_000.00
