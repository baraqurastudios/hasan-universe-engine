from collections import defaultdict
from datetime import datetime


class SelfLearningLayerV32:
    """
    v3.2 Self-Learning Brain Layer
    - Learns from system logs
    - Detects repeating patterns
    - Flags anomalies
    """

    def __init__(self):
        # pattern frequency store
        self.pattern_db = defaultdict(int)

        # history log (optional memory trace)
        self.history = []

    # -----------------------------
    # 🧠 INGEST LEARNING DATA
    # -----------------------------
    def ingest(self, logs: list):
        """
        logs format:
        [
            {"type": "cpu_spike", "message": "..."},
            {"type": "error_burst", "message": "..."}
        ]
        """

        for log in logs:
            log_type = log.get("type", "unknown")

            self.pattern_db[log_type] += 1

            self.history.append({
                "type": log_type,
                "time": datetime.utcnow().isoformat()
            })

    # -----------------------------
    # 🔍 PATTERN DETECTION
    # -----------------------------
    def detect_patterns(self):
        patterns = []

        for key, count in self.pattern_db.items():

            if count >= 3:
                severity = "HIGH"
            elif count == 2:
                severity = "MEDIUM"
            else:
                severity = "LOW"

            patterns.append({
                "pattern": key,
                "count": count,
                "severity": severity
            })

        return patterns

    # -----------------------------
    # ⚡ ANOMALY DETECTION
    # -----------------------------
    def detect_anomalies(self):
        anomalies = []

        for key, count in self.pattern_db.items():

            # simple anomaly rule (can upgrade to ML later)
            if count >= 5:
                anomalies.append({
                    "type": key,
                    "status": "ANOMALY_DETECTED",
                    "reason": "Repeated high-frequency occurrence"
                })

        return anomalies

    # -----------------------------
    # 🧠 PREDICTION ENGINE (SIMPLE)
    # -----------------------------
    def predict_next_risk(self):
        if not self.pattern_db:
            return {"risk": "LOW", "message": "No data yet"}

        top_pattern = max(self.pattern_db, key=self.pattern_db.get)
        count = self.pattern_db[top_pattern]

        if count >= 4:
            return {
                "risk": "HIGH",
                "prediction": f"{top_pattern} likely to repeat",
                "suggestion": "Activate mitigation strategy"
            }

        return {
            "risk": "LOW",
            "prediction": "System stable",
            "suggestion": "No action needed"
        }

    # -----------------------------
    # 📊 DEBUG / INSIGHT REPORT
    # -----------------------------
    def report(self):
        return {
            "patterns": dict(self.pattern_db),
            "total_events": len(self.history),
            "anomalies": self.detect_anomalies(),
            "prediction": self.predict_next_risk()
        }