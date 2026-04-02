import os
import sys
import logging

class SecurityManager:
    def __init__(self):
        self.KILL_TRIGGER = "PROTOCOL_ZERO_V8"
        logging.info("Security Guardian (V8 Emergency System) Initialized")

    def validate(self, master_command):
        """কিল-সুইচ এবং ইনপুট ভ্যালিডেশন"""
        
        # ১. ইমার্জেন্সি কিল-সুইচ চেক
        if master_command == self.KILL_TRIGGER:
            logging.critical("🔴 ALERT: EMERGENCY KILL-SWITCH TRIGGERED!")
            self.v8_emergency_lockdown()
            return False 

        # ২. জেনারেল ভ্যালিডেশন
        if not master_command:
            return False
        
        logging.info("Security Check: Input Validated 🟢")
        return True

    def v8_emergency_lockdown(self):
        """সিস্টেম সেলফ-লকিং এবং টার্মিনেশন"""
        print("🔴 ALERT: EMERGENCY KILL-SWITCH TRIGGERED!")
        print("🛡️ System: Self-Locking... Stopping All Tasks.")
        # Streamlit সার্ভার প্রসেস বন্ধ করে দিবে
        os._exit(1)
