import numpy as np
from sklearn.ensemble import IsolationForest
from collections import defaultdict
from datetime import datetime


class MLBrainV32:
    """
    v3.2 ML Self-Learning Brain
    - Uses anomaly detection (Isolation Forest)
    - Learns patterns from structured logs
    - Produces risk prediction
    """

    def __init__(self):
        self.logs = []
        self.pattern_counter = defaultdict(int)
        self.model = IsolationForest(contamination=0.1, random_state=42)

        self.trained = False

    # -----------------------------
    # 🧾 INGEST DATA
    # -----------------------------
    def ingest(self, logs: list):
        """
        logs format:
        {
            "type": "cpu_spike",
            "value": 0.8,   # normalized metric (0-1)
        }
        """

        for log in logs:
            self.logs.append([
                log.get("value", 0.0)
            ])

            self.pattern_counter[log.get("type", "unknown")] += 1

    # -----------------------------
    # 🧠 TRAIN MODEL
    # -----------------------------
    def train(self):
        if len(self.logs) < 5:
            return "Not enough data to train"

        X = np.array(self.logs)

        self.model.fit(X)
        self.trained = True

        return "Model trained successfully"

    # -----------------------------
    # 🔍 ANOMALY DETECTION
    # -----------------------------
    def detect_anomalies(self):

        if not self.trained:
            return []

        X = np.array(self.logs)

        results = self.model.predict(X)

        anomalies = []

        for i, r in enumerate(results):
            if r == -1:
                anomalies.append({
                    "index": i,
                    "value": self.logs[i],
                    "status": "ANOMALY"
                })

        return anomalies

    # -----------------------------
    # ⚡ RISK SCORING
    # -----------------------------
    def risk_score(self):

        if not self.trained:
            return {"risk": "UNKNOWN"}

        anomalies = len(self.detect_anomalies())
        total = len(self.logs)

        score = anomalies / total if total > 0 else 0

        if score > 0.4:
            level = "HIGH"
        elif score > 0.2:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            "risk_level": level,
            "score": round(score, 3)
        }

    # -----------------------------
    # 🔮 SIMPLE FORECAST
    # -----------------------------
    def forecast(self):

        if not self.pattern_counter:
            return {"forecast": "NO DATA"}

        top_pattern = max(self.pattern_counter, key=self.pattern_counter.get)

        return {
            "most_common_issue": top_pattern,
            "next_likely_event": f"{top_pattern} recurrence possible",
            "confidence": 0.75
        }

    # -----------------------------
    # 📊 FULL REPORT
    # -----------------------------
    def report(self):

        return {
            "trained": self.trained,
            "total_logs": len(self.logs),
            "patterns": dict(self.pattern_counter),
            "anomalies": self.detect_anomalies(),
            "risk": self.risk_score(),
            "forecast": self.forecast(),
            "timestamp": datetime.utcnow().isoformat()
        }