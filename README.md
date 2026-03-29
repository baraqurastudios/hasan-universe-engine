import time
from collections import deque, defaultdict


class StreamingBrainV323:
    """
    v3.2.3 Real-Time Streaming Intelligence Brain
    - Processes continuous data stream
    - Learns instantly from incoming events
    """

    def __init__(self, window_size=10):
        self.window = deque(maxlen=window_size)

        # live counters
        self.event_count = defaultdict(int)

        # live risk score
        self.risk_score = 0.0

    # -----------------------------
    # ⚡ STREAM INPUT
    # -----------------------------
    def stream_event(self, event: dict):

        """
        event format:
        {
            "type": "cpu_spike",
            "value": 0.8
        }
        """

        self.window.append(event)

        event_type = event.get("type", "unknown")
        value = event.get("value", 0)

        self.event_count[event_type] += 1

        # live risk update
        self._update_risk(value)

        return self.live_state()

    # -----------------------------
    # 📊 RISK ENGINE (REAL TIME)
    # -----------------------------
    def _update_risk(self, value):

        # exponential smoothing style
        alpha = 0.3
        self.risk_score = (alpha * value) + (1 - alpha) * self.risk_score

    # -----------------------------
    # 🔍 ANOMALY SIGNAL (LIVE)
    # -----------------------------
    def detect_live_anomaly(self):

        if len(self.window) < 3:
            return {"status": "INSUFFICIENT DATA"}

        recent_values = [e["value"] for e in self.window]

        avg = sum(recent_values) / len(recent_values)

        if avg > 0.75:
            return {
                "status": "ANOMALY",
                "reason": "High sustained load detected"
            }

        return {
            "status": "NORMAL"
        }

    # -----------------------------
    # 🧠 LIVE DECISION ENGINE
    # -----------------------------
    def decide(self):

        anomaly = self.detect_live_anomaly()

        if anomaly["status"] == "ANOMALY":
            return {
                "action": "SCALE_UP",
                "confidence": 0.9,
                "reason": anomaly["reason"]
            }

        if self.risk_score > 0.6:
            return {
                "action": "PREPARE_SCALE",
                "confidence": 0.7,
                "reason": "Rising risk detected"
            }

        return {
            "action": "NOOP",
            "confidence": 0.8,
            "reason": "System stable"
        }

    # -----------------------------
    # 📡 LIVE SYSTEM STATE
    # -----------------------------
    def live_state(self):

        return {
            "risk_score": round(self.risk_score, 3),
            "event_counts": dict(self.event_count),
            "decision": self.decide(),
            "window_size": len(self.window)
        }

    # -----------------------------
    # 📊 REPORT
    # -----------------------------
    def report(self):

        return {
            "risk_score": self.risk_score,
            "events": dict(self.event_count),
            "current_decision": self.decide()
        }