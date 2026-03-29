import random
import copy
from datetime import datetime


# -----------------------------
# 🌐 WORLD SIMULATION ENGINE
# -----------------------------
class WorldSimulationV42:

    def __init__(self, base_state, brain):

        self.base_state = base_state
        self.brain = brain

        self.simulations = []
        self.history = []

    # -----------------------------
    # 🌍 CREATE WORLD COPY
    # -----------------------------
    def _clone_world(self):

        return copy.deepcopy(self.base_state)

    # -----------------------------
    # 🔮 SIMULATE FUTURE
    # -----------------------------
    def simulate_future(self, action):

        world = self._clone_world()

        # random environmental drift (uncertainty)
        world["noise"] = random.uniform(0, 1)

        # apply action effect
        if action == "SCALE_UP":
            world["performance"] += 10

        elif action == "OPTIMIZE":
            world["efficiency"] += 15

        elif action == "LOCKDOWN":
            world["stability"] += 20

        # random failure chance
        world["risk"] = random.uniform(0, 1)

        score = (
            world.get("performance", 50)
            + world.get("efficiency", 50)
            + world.get("stability", 50)
            - world["risk"] * 20
        )

        return {
            "action": action,
            "projected_score": score,
            "world_state": world
        }

    # -----------------------------
    # 🧠 SIMULATION-BASED DECISION
    # -----------------------------
    def decide_via_simulation(self, possible_actions):

        results = []

        for action in possible_actions:
            sim = self.simulate_future(action)
            results.append(sim)

        best = max(results, key=lambda x: x["projected_score"])

        self.simulations.append(results)

        return {
            "best_action": best["action"],
            "score": best["projected_score"],
            "all_simulations": results
        }

    # -----------------------------
    # 🔄 RUN WORLD STEP
    # -----------------------------
    def world_step(self, signal):

        actions = self.brain.decide(signal).get(
            "possible_actions",
            ["NOOP", "OPTIMIZE", "SCALE_UP"]
        )

        decision = self.decide_via_simulation(actions)

        self.history.append({
            "signal": signal,
            "decision": decision,
            "timestamp": datetime.utcnow().isoformat()
        })

        return decision

    # -----------------------------
    # 📊 WORLD STATUS
    # -----------------------------
    def status(self):

        return {
            "simulations_run": len(self.simulations),
            "history": len(self.history),
            "base_state": self.base_state
        }