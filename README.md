import random
from datetime import datetime


# -----------------------------
# 🌍 CIVILIZATION (SMALL WORLD)
# -----------------------------
class Civilization:

    def __init__(self, cid):

        self.cid = cid
        self.population = random.randint(50, 200)
        self.tech = random.uniform(0.1, 1.0)
        self.resources = random.randint(500, 1000)
        self.alive = True

    def step(self):

        growth = self.population * self.tech * random.uniform(0.8, 1.2)
        cost = random.uniform(20, 100)

        self.resources += growth - cost
        self.population += int(self.tech * 10)

        # survival check
        if self.resources < 0:
            self.alive = False


# -----------------------------
# 🪐 UNIVERSE ENGINE
# -----------------------------
class UniverseV60:

    def __init__(self, num_civilizations=3):

        self.civilizations = [
            Civilization(f"civ_{i}") for i in range(num_civilizations)
        ]

        self.universe_energy = 10000
        self.history = []

    # -----------------------------
    # ⚛️ PHYSICS RULES
    # -----------------------------
    def physics_tick(self):

        self.universe_energy += random.uniform(-50, 100)

        # entropy always increases
        self.universe_energy -= len(self.civilizations) * 2

    # -----------------------------
    # 🌍 CIVILIZATION INTERACTION
    # -----------------------------
    def interactions(self):

        for civ in self.civilizations:

            if not civ.alive:
                continue

            civ.step()

            # random interaction event
            other = random.choice(self.civilizations)

            if other != civ and other.alive:

                # trade or conflict
                if random.random() > 0.5:
                    civ.resources += 50
                    other.resources -= 50
                else:
                    civ.population -= 5

    # -----------------------------
    # ⚖️ UNIVERSE BALANCE
    # -----------------------------
    def balance(self):

        alive = [c for c in self.civilizations if c.alive]

        if len(alive) == 0:
            return "UNIVERSE_DEAD"

        if len(alive) == 1:
            self.universe_energy += 100

        # collapse condition
        if self.universe_energy < 100:
            for c in alive:
                c.alive = False

    # -----------------------------
    # 🌌 WORLD STEP
    # -----------------------------
    def step(self):

        self.physics_tick()
        self.interactions()
        self.balance()

        state = self.status()

        self.history.append({
            "state": state,
            "timestamp": datetime.utcnow().isoformat()
        })

        return state

    # -----------------------------
    # 📊 STATUS REPORT
    # -----------------------------
    def status(self):

        alive = len([c for c in self.civilizations if c.alive])

        return {
            "alive_civilizations": alive,
            "total_civilizations": len(self.civilizations),
            "universe_energy": self.universe_energy
        }