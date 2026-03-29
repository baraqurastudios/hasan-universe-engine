import redis
import json

class RedisMemory:
    def __init__(self, host="localhost", port=6379):
        # v2.2: Connecting to persistent storage
        self.r = redis.Redis(host=host, port=port, decode_responses=True)

    def save_state(self, key, data):
        self.r.set(key, json.dumps(data))

    def get_state(self, key):
        data = self.r.get(key)
        return json.loads(data) if data else None

    def push_incident(self, event):
        # v2.2: Storing history for audit and rollback
        self.r.lpush("incident_history", json.dumps(event))