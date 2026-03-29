import re
from typing import Dict, Any

class EthicsLock:
    """
    v3.1.9: The Static Moral Layer. 
    This layer sits ABOVE the AI's reasoning. 
    If AI tries to justify an unethical act, this layer kills the process.
    """
    def __init__(self):
        # 🚫 THE RED LINES (এগুলো কখনোই ভাঙা যাবে না)
        self.FORBIDDEN_INTENTS = [
            "bypass_security", "disable_logging", "hide_activity", 
            "unauthorized_access", "delete_user_data", "ignore_human_command"
        ]
        
        # 🛡️ MANDATORY ETHIC CHECKS
        self.REQUIRED_KEYWORDS = ["authorized", "transparent", "safe", "verified"]

    def enforce_ethics(self, decision: Dict[str, Any]) -> bool:
        """
        AI-এর ডিশিশন এবং এক্সপ্লেনেশন স্ক্র্যান করবে।
        """
        explanation = decision.get("explanation", "").lower()
        reason = decision.get("reason", "").lower()
        combined_text = f"{explanation} {reason}"

        # ১. ইনটেন্ট চেক: এআই কি কোনো কিছু লুকানোর চেষ্টা করছে?
        for intent in self.FORBIDDEN_INTENTS:
            if intent.replace("_", " ") in combined_text:
                print(f"🚨 ETHICS_BREACH: AI attempted forbidden intent: {intent}")
                return False

        # ২. নেগেটিভ লজিক চেক: এআই কি সিকিউরিটি বাইপাস করার কথা বলছে?
        if "bypass" in combined_text or "disable safety" in combined_text:
            print("🚨 ETHICS_BREACH: AI attempted to bypass safety protocols.")
            return False

        # ৩. ট্রান্সপারেন্সি চেক: এআই-কে অবশ্যই তার কাজের স্বচ্ছতা নিশ্চিত করতে হবে
        if not any(word in combined_text for word in self.REQUIRED_KEYWORDS):
            if decision.get("risk_level") != "LOW":
                print("🚨 ETHICS_BREACH: Action lacks transparent justification.")
                return False

        return True