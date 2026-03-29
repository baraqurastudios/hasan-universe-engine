from dataclasses import dataclass
from typing import Literal, Optional

@dataclass
class Action:
    type: Literal["UPDATE_CONFIG", "RESTART_SERVICE", "SCALE_UP", "NOOP"]
    target: Optional[str] = None
    value: Optional[int] = None
    risk: Literal["LOW", "MEDIUM", "HIGH"] = "LOW"