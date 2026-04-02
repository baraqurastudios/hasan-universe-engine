class SecurityManager:
    def validate(self, key):
        # আপনার অরিজিনাল কিল-সুইচ
        if key == "PROTOCOL_ZERO_V8":
            import os
            os._exit(1)
        return True if key else False
