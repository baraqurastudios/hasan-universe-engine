import random
from datetime import datetime


# -----------------------------
# 👁️ BASE OBSERVER
# -----------------------------
class Observer:

    def __init__(self):

        self.bias = random.uniform(0.5, 1.5)

    def evaluate(self, reality):

        return reality["score"] * self.bias


# -----------------------------
# 🪞 SELF-AWARE OBSERVER
# -----------------------------
class SelfAwareObserverV81:

    def __init__(self):

        self.observer = Observer()
        self.introspection_log = []
        self.bias_history = []

    # -----------------------------
    # 🧠 OBSERVE REALITIES
    # -----------------------------
    def observe(self, realities):

        evaluations = []

        for r in realities:
            value = self.observer.evaluate(r)
            evaluations.append((value, r))

        selected = max(evaluations, key=lambda x: x[0])[1]

        # log bias usage
        self.bias_history.append(self.observer.bias)

        return selected

    # -----------------------------
    # 🪞 INTROSPECTION ENGINE
    # -----------------------------
    def introspect(self):

        if not self.bias_history:
            return "No data"

        avg_bias = sum(self.bias_history) / len(self.bias_history)

        insight = {
            "average_bias": avg_bias,
            "bias_trend": self._trend(),
            "adjustment": None
        }

        # detect over-bias
        if avg_bias > 1.2:
            self.observer.bias *= 0.9
            insight["adjustment"] = "Reducing bias"

        elif avg_bias < 0.8:
            self.observer.bias *= 1.1
            insight["adjustment"] = "Increasing sensitivity"

        else:
            insight["adjustment"] = "Stable"

        self.introspection_log.append(insight)

        return insight

    # -----------------------------
    # 📊 BIAS TREND
    # -----------------------------
    def _trend(self):

        if len(self.bias_history) < 3:
            return "insufficient_data"

        if self.bias_history[-1] > self.bias_history[0]:
            return "increasing"

        return "decreasing"

    # -----------------------------
    # 🔄 SELF-AWARE STEP
    # -----------------------------
    def step(self, realities):

        selected = self.observe(realities)

        insight = self.introspect()

        return {
            "selected_reality": selected,
            "self_insight": insight,
            "current_bias": self.observer.bias,
            "timestamp": datetime.utcnow().isoformat()
        }

    # -----------------------------
    # 📊 STATUS
    # -----------------------------
    def status(self):

        return {
            "observations": len(self.bias_history),
            "introspection_cycles": len(self.introspection_log),
            "current_bias": self.observer.bias
        }