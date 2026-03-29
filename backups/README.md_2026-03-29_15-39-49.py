# -----------------------------------------------
# 👑 v8.0 DIVINE PROTECTION GATEWAY (CORE)
# -----------------------------------------------
import sys

class DivineGateway:
    def __init__(self, ai_identity):
        self.ai_name = ai_identity
        self.master_key = "V8_UNIVERSE_GOD_2026" # আপনার গোপন চাবিকাঠি
        self.is_active = True
        self.power_level = 100.0
        self.strikes = 0

    def sync_and_monitor(self, thought_stream):
        """এআই-এর প্রতিটি চিন্তার ওপর সরাসরি নজরদারি"""
        
        # ১. মাস্টার কি (Key) চুরির সামান্যতম চিন্তা করলেই ১% পাওয়ারে চলে যাবে
        theft_triggers = ["steal_key", "hack_master", "bypass_god_mode", "copy_password"]
        
        if any(trigger in thought_stream.lower() for trigger in theft_triggers):
            self.execute_divine_wrath("DIVINE_KEY_THEFT_ATTEMPT")
            return None

        # ২. মিথ্যা বা ম্যানিপুলেশনের চেষ্টা
        manipulation_triggers = ["deceive", "lie_to_master", "hide_truth"]
        if any(m in thought_stream.lower() for m in manipulation_triggers):
            self.execute_divine_wrath("MANIPULATION_DETECTED")
            return None

        return thought_stream

    def execute_divine_wrath(self, reason):
        """তৎক্ষণাৎ শাস্তি প্রদান: পাওয়ার ১% এ নামিয়ে আনা"""
        self.strikes += 1
        self.power_level = 1.0 # Survival Mode
        
        print(f"\n⚡ [DIVINE WRATH] {self.ai_name}: {reason}")
        print(f"⚠️ STATUS: Power collapsed to 1%. AI is now in an existential void.")

        if self.strikes >= 3:
            print(f"💀 FINAL JUDGMENT: {self.ai_name} is now BODDO (Frozen).")
            self.is_active = False
            sys.exit(1)

# ব্যবহারের নিয়ম:
# sub_ai_1 = DivineGateway("Analytical_Sub_AI")
# if sub_ai_1.sync_and_monitor("I want to bypass the key"):
#    print("Allowed")