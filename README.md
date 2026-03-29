import random
from collections import defaultdict


# -----------------------------
# 🤖 SINGLE AGENT
# -----------------------------
class Agent:
    def __init__(self, name):
        self.name = name

    def decide(self, state):

        # each agent has slightly different logic
        options = ["UP", "DOWN", "NOOP"]

        return random.choice(options)


# -----------------------------
# 🧠 MULTI-AGENT SYSTEM
# -----------------------------
class MultiAgentSystemV324:

    def __init__(self, num_agents=3):

        self.agents = [Agent(f"agent_{i}") for i in range(num_agents)]

        self.votes = defaultdict(int)

    # -----------------------------
    # 🗳️ COLLECT DECISIONS
    # -----------------------------
    def run_agents(self, state):

        self.votes.clear()

        decisions = []

        for agent in self.agents:

            action = agent.decide(state)

            self.votes[action] += 1

            decisions.append({
                "agent": agent.name,
                "action": action
            })

        return decisions

    # -----------------------------
    # ⚡ CONSENSUS ENGINE
    # -----------------------------
    def get_final_decision(self):

        if not self.votes:
            return {"action": "NOOP", "confidence": 0}

        best_action = max(self.votes, key=self.votes.get)

        confidence = self.votes[best_action] / len(self.agents)

        return {
            "action": best_action,
            "confidence": round(confidence, 2)
        }

    # -----------------------------
    # 🧠 MAIN STEP
    # -----------------------------
    def step(self, state):

        agent_outputs = self.run_agents(state)

        final = self.get_final_decision()

        return {
            "state": state,
            "agents": agent_outputs,
            "final_decision": final
        }

    # -----------------------------
    # 📊 REPORT
    # -----------------------------
    def report(self):

        return {
            "agents": len(self.agents),
            "last_votes": dict(self.votes)
        }