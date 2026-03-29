import random
from datetime import datetime


# -----------------------------
# 🌌 REALITY BRANCH
# -----------------------------
class RealityBranch:

    def __init__(self, state):

        self.state = state
        self.score = random.uniform(0, 100)


# -----------------------------
# 👁️ OBSERVER
# -----------------------------
class Observer:

    def __init__(self):

        self.perception_bias = random.uniform(0.5, 1.5)

    def observe(self, realities):

        # observer selects reality based on bias
        weighted = []

        for r in realities:
            adjusted = r.score * self.perception_bias
            weighted.append((adjusted, r))

        selected = max(weighted, key=lambda x: x[0])[1]

        return selected


# -----------------------------
# 🪞 GOD LAYER
# -----------------------------
class ObserverGodV80:

    def __init__(self, universe):

        self.universe = universe
        self.observer = Observer()

        self.timeline = []

    # -----------------------------
    # 🌌 GENERATE MULTIPLE REALITIES
    # -----------------------------
    def generate_realities(self):

        realities = []

        for _ in range(5):

            state = self.universe.step()

            branch = RealityBranch(state)

            realities.append(branch)

        return realities

    # -----------------------------
    # 👁️ OBSERVE & COLLAPSE REALITY
    # -----------------------------
    def collapse(self):

        realities = self.generate_realities()

        selected = self.observer.observe(realities)

        record = {
            "chosen_state": selected.state,
            "score": selected.score,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.timeline.append(record)

        return record

    # -----------------------------
    # 🧠 MEANING ENGINE
    # -----------------------------
    def derive_meaning(self):

        if not self.timeline:
            return "No observations yet"

        patterns = len(self.timeline)

        if patterns > 10:
            return "Stable reality pattern emerging"

        return "Reality still fluctuating"

    # -----------------------------
    # 📊 GOD STATUS
    # -----------------------------
    def status(self):

        return {
            "observations": len(self.timeline),
            "meaning": self.derive_meaning()
        }