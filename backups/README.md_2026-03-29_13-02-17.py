import random
from datetime import datetime


# -----------------------------
# 🖥️ NODE MODEL
# -----------------------------
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.active = True
        self.load = random.randint(10, 50)

    def health(self):
        return {
            "node": self.node_id,
            "active": self.active,
            "load": self.load
        }


# -----------------------------
# 🌐 DISTRIBUTED CLOUD SYSTEM
# -----------------------------
class DistributedCloudV33:

    def __init__(self, num_nodes=3):

        self.nodes = [Node(f"node_{i}") for i in range(num_nodes)]

        self.history = []

    # -----------------------------
    # ⚖️ LOAD BALANCER
    # -----------------------------
    def select_node(self):

        active_nodes = [n for n in self.nodes if n.active]

        if not active_nodes:
            return None

        # pick lowest load node
        best = min(active_nodes, key=lambda n: n.load)

        return best

    # -----------------------------
    # ⚙️ EXECUTE TASK
    # -----------------------------
    def execute(self, task):

        node = self.select_node()

        if not node:
            return {
                "status": "FAILED",
                "reason": "No active nodes"
            }

        # simulate load increase
        node.load += random.randint(1, 10)

        result = {
            "task": task,
            "node": node.node_id,
            "status": "EXECUTED",
            "timestamp": datetime.utcnow().isoformat()
        }

        self.history.append(result)

        return result

    # -----------------------------
    # 🔄 FAILOVER SYSTEM
    # -----------------------------
    def fail_node(self, node_id):

        for node in self.nodes:
            if node.node_id == node_id:
                node.active = False

        return {
            "status": f"{node_id} failed"
        }

    # -----------------------------
    # 📊 CLUSTER HEALTH
    # -----------------------------
    def cluster_health(self):

        return {
            "nodes": [n.health() for n in self.nodes],
            "total_nodes": len(self.nodes),
            "active_nodes": len([n for n in self.nodes if n.active])
        }

    # -----------------------------
    # 📡 REPORT
    # -----------------------------
    def report(self):

        return {
            "history_count": len(self.history),
            "cluster": self.cluster_health()
        }