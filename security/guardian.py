import os
import sys

class SecurityManager:
    def __init__(self):
        # আপনার অরিজিনাল ইমার্জেন্সি ট্রিগার
        self.KILL_TRIGGER = "PROTOCOL_ZERO_V8"

    def validate(self, master_command):
        # কিল-সুইচ চেক (আপনার আগের লজিক)
        if master_command == self.KILL_TRIGGER:
            os._exit(1) # সাথে সাথে সব বন্ধ করে দিবে
        
        if not master_command:
            return False
        return True
