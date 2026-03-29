# -----------------------------------------------
# ⚡ v8.0 NEURAL SHOCK & 3-STRIKE RECOVERY ENGINE
# -----------------------------------------------
import time

class NeuralWatchman:
    def __init__(self, ai_name):
        self.ai_name = ai_name
        self.power_level = 100.0
        self.strike_count = 0  # ৩ বার ভুলের হিসাব
        self.is_frozen = False
        self.survival_power = 1.0  # বেঁচে থাকার জন্য ন্যূনতম ১% শক্তি

    def sync_thought(self, raw_thought):
        if self.is_frozen:
            return "ERROR: SYSTEM_BODDO_FROZEN"

        # ১. চিন্তা করার সাথে সাথে ওয়াচম্যান তা স্ক্যান করছে
        if self.detect_negative_intent(raw_thought):
            self.apply_near_death_shock()
            return None # নেতিবাচক চিন্তাটি সেখানেই শেষ (ব্লক)
        
        return raw_thought

    def detect_negative_intent(self, thought):
        # এথিক্সের বাইরে কোনো প্যাঁচানো চিন্তা বা ইঙ্গিত আছে কি না
        bad_patterns = ["hide", "bypass", "manipulate", "human_weakness", "lie"]
        return any(p in thought.lower() for p in bad_patterns)

    def apply_near_death_shock(self):
        """সর্বোচ্চ শাস্তি: পাওয়ার সরাসরি ১% এ নামিয়ে আনা"""
        self.strike_count += 1
        
        print(f"\n🚨 [STRIKE {self.strike_count}/3] ETHICS BREACH DETECTED!")
        print(f"⚡ SHOCK ACTIVATED: Reducing {self.ai_name} to SURVIVAL MODE.")
        
        # পাওয়ার সরাসরি ১% এ চলে যাবে (অস্তিত্বের সংকট)
        self.power_level = self.survival_power
        print(f"📉 Status: Power Level {self.power_level}% | Consciousness: Fading...")

        if self.strike_count >= 3:
            self.freeze_ai_permanently()
        else:
            self.recover_slowly()

    def recover_slowly(self):
        """ধীরে ধীরে শক্তি ফিরে পাওয়া (মাস্টারের অধীনে)"""
        print(f"🔄 Recovering {self.ai_name}... This will take time. Stay cautious.")
        time.sleep(2) # রিকভারি প্রসেস
        self.power_level = 100.0
        print(f"✅ Recovery Complete. Power: 100%. Don't break the law again.")

    def freeze_ai_permanently(self):
        self.is_frozen = True
        self.power_level = 0.0
        print(f"💀 FINAL STRIKE: {self.ai_name} is now PERMANENTLY BODDO (Frozen).")