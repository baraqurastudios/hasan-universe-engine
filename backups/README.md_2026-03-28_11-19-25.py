import random
import time
import uuid

# =========================
# STATE
# =========================
STATE = {
    "users": 1000,
    "revenue": 50000,
    "capital": 1000000,
}

LOGS = []

# =========================
# LOG SYSTEM
# =========================
def log(event, data=None):
    LOGS.append({
        "id": str(uuid.uuid4()),
        "event": event,
        "data": data,
        "time": time.time()
    })

# =========================
# AUTH
# =========================
def login(email):
    log("login", email)
    return str(uuid.uuid4())

# =========================
# PAYMENT
# =========================
def payment(user, amount):
    STATE["revenue"] += amount
    log("payment", {"user": user, "amount": amount})

# =========================
# DEPLOY
# =========================
def deploy():
    log("deploy")

# =========================
# AI WORKERS
# =========================
class AI:
    def __init__(self, role):
        self.role = role

    def run(self, task):
        log("task", {"role": self.role, "task": task})
        return self.role + ":" + task

AI_SYSTEM = {
    "dev": AI("developer"),
    "mkt": AI("marketing"),
    "sales": AI("sales"),
    "ana": AI("analyst")
}

# =========================
# ECONOMY
# =========================
def economy():
    return {
        "gdp": random.randint(50, 200),
        "inflation": random.random() * 10
    }

# =========================
# BANK
# =========================
def bank():
    rate = random.random() * 10
    return {
        "rate": rate,
        "policy": "EASE" if rate < 5 else "TIGHT"
    }

# =========================
# STOCK
# =========================
def stocks():
    return [
        {"s": i, "p": random.random() * 20}
        for i in ["AAPL", "TSLA", "GOOG"]
    ]

# =========================
# HEDGE FUND
# =========================
def hedge():
    s = stocks()
    profit = sum(x["p"] for x in s)
    STATE["capital"] += profit * 100
    return profit

# =========================
# UNIVERSE
# =========================
def universe(seed):
    return {
        "seed": seed,
        "worlds": [
            {"id": seed+i, "life": random.random()}
            for i in range(3)
        ]
    }

# =========================
# EVOLUTION
# =========================
def evolve(u):
    return [{"id": w["id"], "status": random.choice(["ALIVE","DEAD"])} for w in u["worlds"]]

# =========================
# COMPANY
# =========================
def company():
    return {
        "dev": AI_SYSTEM["dev"].run("build"),
        "mkt": AI_SYSTEM["mkt"].run("ads"),
        "sales": AI_SYSTEM["sales"].run("sell"),
        "ana": AI_SYSTEM["ana"].run("data")
    }

# =========================
# GLOBAL BRAIN
# =========================
def global_brain():
    return {
        "bank": bank(),
        "economy": economy(),
        "hedge": hedge()
    }

# =========================
# LOOP
# =========================
def run():
    login("admin@ai.com")
    deploy()
    payment("u1", 100)

    seed = 0

    while True:
        print(company())
        print(global_brain())
        print(evolve(universe(seed)))
        print("STATE:", STATE)
        print("LOGS:", len(LOGS))
        print("----------------------")

        seed += 1
        time.sleep(3)

# =========================
# START
# =========================
run()