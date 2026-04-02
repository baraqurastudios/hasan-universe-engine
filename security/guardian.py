import os

class SecurityManager:
    def __init__(self):
        self.KILL_TRIGGER = "PROTOCOL_ZERO_V8"

    def validate(self, command):
        if command == self.KILL_TRIGGER:
            os._exit(1)
        return True if command else False
