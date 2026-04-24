from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import uuid4


class TransferStatus(str, Enum):
    PENDING = "pending"
    PROCESSED = "processed"
    FAILED = "failed"


class AlertSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


@dataclass
class Transfer:
    originator: str
    beneficiary: str
    amount: float
    routing_number: str
    account_number: str
    memo: str = ""
    id: str = field(default_factory=lambda: str(uuid4()))
    status: TransferStatus = TransferStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class Alert:
    title: str
    message: str
    severity: AlertSeverity = AlertSeverity.INFO
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    transfer_id: str | None = None


@dataclass
class AuditEvent:
    action: str
    detail: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    transfer_id: str | None = None
