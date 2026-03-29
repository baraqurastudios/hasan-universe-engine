from dataclasses import dataclass
from typing import Literal

@dataclass
class DecisionV31:
    """
    v3.1 Core: The blueprint of every autonomous decision.
    """
    action: Literal["SCALE_UP", "RESTART_SERVICE", "NOOP", "UPDATE_CONFIG"]
    reason: str
    explanation: str
    confidence: float
    risk_level: Literal["LOW", "MEDIUM", "HIGH"] = "LOW"