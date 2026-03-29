class StrategistV3_1:
    """
    v3.1 Core: Every decision must be explainable.
    """

    def analyze(self, logs):
        if "cpu spike" in logs.lower():
            return {
                "action": "SCALE_UP",
                "reason": "CPU spike detected in recent logs",
                "confidence": 0.86,
                "explanation": "System load exceeded threshold based on pattern match"
            }

        if "error burst" in logs.lower():
            return {
                "action": "RESTART_SERVICE",
                "reason": "Error burst anomaly",
                "confidence": 0.72,
                "explanation": "Repeated failure pattern detected in service logs"
            }

        return {
            "action": "NOOP",
            "reason": "System stable",
            "confidence": 0.99,
            "explanation": "No anomaly detected in current observation window"
        }