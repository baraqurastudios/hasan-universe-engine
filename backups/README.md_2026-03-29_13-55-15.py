import random
from datetime import datetime


# -----------------------------
# ⚛️ DYNAMIC RULE ENGINE
# -----------------------------
class RuleEngine:

    def __init__(self):

        self.rules = {
            "gravity": 9.8,
            "entropy": 0.01,
            "growth_factor": 1.0
        }

    # -----------------------------
    # 🧬 SELF-EVOLVING RULES
    # -----------------------------
    def mutate_rules(self):

        for key in self.rules:

            change = random.uniform(-0.1, 0.1)
            self.rules[key] += change

        # emergent new rule creation
        if random.random() > 0.7:

            new_rule = f"rule_{random.randint(1,100)}"
            self.rules[new_rule] = random.uniform(0.1, 5.0)

    # -----------------------------
    # 📊 RULE STATE
    # -----------------------------
    def state(self):

        return self.rules


# -----------------------------
# 🌌 SELF-CREATING UNIVERSE
# -----------------------------
class SelfCreatingUniverseV70:

    def __init__(self, civilizations):

        self.rules = RuleEngine()
        self.civilizations = civilizations

        self.timeline = []
        self.age = 0

    # -----------------------------
    # 🧬 META EVOLUTION
    # -----------------------------
    def evolve_civilizations(self):

        for civ in self.civilizations:

            if not civ.alive:
                continue

            # rules affect evolution
            civ.tech *= self.rules.rules.get("growth_factor", 1.0)

            civ.population += int(civ.tech * 5)

            # entropy effect
            if random.random() < self.rules.rules.get("entropy", 0.01):
                civ.alive = False

    # -----------------------------
    # ⚛️ UNIVERSE REWRITE STEP
    # -----------------------------
    def universe_step(self):

        self.age += 1

        # universe rewrites itself
        self.rules.mutate_rules()

        # civilizations evolve under new physics
        self.evolve_civilizations()

        state = self.status()

        self.timeline.append({
            "age": self.age,
            "state": state,
            "rules": self.rules.state(),
            "timestamp": datetime.utcnow().isoformat()
        })

        return state

    # -----------------------------
    # 📊 UNIVERSE STATUS
    # -----------------------------
    def status(self):

        alive = len([c for c in self.civilizations if c.alive])

        return {
            "age": self.age,
            "alive_civilizations": alive,
            "total_civilizations": len(self.civilizations),
            "rules": self.rules.state()
        }