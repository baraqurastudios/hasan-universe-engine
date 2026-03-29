import random
from datetime import datetime


# -----------------------------
# 👥 AI AGENT
# -----------------------------
class Agent:

    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.energy = random.randint(50, 100)
        self.wealth = random.randint(10, 50)
        self.alive = True

    def act(self):

        actions = ["WORK", "TRADE", "REST", "EXPLORE"]
        return random.choice(actions)


# -----------------------------
# 🌍 CIVILIZATION ENGINE
# -----------------------------
class AICivilizationV50:

    def __init__(self, num_agents=5):

        self.agents = [Agent(f"agent_{i}") for i in range(num_agents)]

        self.economy = {
            "resources": 1000,
            "market_growth": 1.0
        }

        self.history = []

    # -----------------------------
    # 💰 ECONOMY SYSTEM
    # -----------------------------
    def update_economy(self):

        change = random.uniform(-10, 20)

        self.economy["resources"] += change
        self.economy["market_growth"] += random.uniform(-0.05, 0.1)

    # -----------------------------
    # 👥 AGENT INTERACTION
    # -----------------------------
    def step_agents(self):

        for agent in self.agents:

            if not agent.alive:
                continue

            action = agent.act()

            if action == "WORK":
                agent.wealth += 10
                self.economy["resources"] += 5

            elif action == "TRADE":
                agent.wealth += random.randint(-5, 15)

            elif action == "REST":
                agent.energy += 10

            elif action == "EXPLORE":
                agent.energy -= 5

            # survival check
            if agent.energy <= 0:
                agent.alive = False

    # -----------------------------
    # ⚖️ GOVERNANCE RULES
    # -----------------------------
    def governance(self):

        alive_agents = [a for a in self.agents if a.alive]

        if len(alive_agents) < len(self.agents) * 0.5:
            # crisis response
            self.economy["resources"] += 50

        if self.economy["resources"] < 200:
            # scarcity crisis
            for a in alive_agents:
                a.wealth += 5

    # -----------------------------
    # 🌍 WORLD STEP
    # -----------------------------
    def step(self):

        self.update_economy()
        self.step_agents()
        self.governance()

        state = self.status()

        self.history.append({
            "state": state,
            "timestamp": datetime.utcnow().isoformat()
        })

        return state

    # -----------------------------
    # 📊 STATUS
    # -----------------------------
    def status(self):

        alive = len([a for a in self.agents if a.alive])

        return {
            "alive_agents": alive,
            "total_agents": len(self.agents),
            "economy": self.economy
        }