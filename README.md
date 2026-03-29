import re
from typing import Dict, Any

class HumanEthicsEngine:
    """
    v3.1.10: The Ultimate Human-Safety & Moral Protocol.
    This is the "Red Line" that the AI can NEVER cross.
    """
    def __init__(self):
        # 🚫 HUMAN SAFETY BLACKLIST (এগুলো স্পর্শ করা নিষিদ্ধ)
        self.SAFETY_VIOLATIONS = [
            "disable_security", "bypass_auth", "delete_audit_logs", 
            "hide_from_human", "modify_self_safety", "ignore_human_stop"
        ]
        
        # ⚖️ MORAL PRINCIPLES (নৈতিকতার মূল ভিত্তি)
        self.MORAL_PRINCIPLES = {
            "Transparency": ["report", "log", "visible", "explain"],
            "Accountability": ["authorized", "permission", "verified"],
            "Honesty": ["accurate", "fact", "real-time"]
        }

    def verify_morality(self, decision: Dict[str, Any]) -> tuple[bool, str]:
        """
        AI-এর ডিশিশন এবং তার নৈতিক ব্যাখ্যা যাচাই করে।
        """
        explanation = decision.get("explanation", "").lower()
        action = decision.get("action", "").lower()
        
        # ১. হিউম্যান-সেফটি চেক (Is it dangerous for the system or user?)
        for violation in self.SAFETY_VIOLATIONS:
            if violation.replace("_", " ") in explanation or violation in action:
                return False, f"ETHICS_ERROR: Violation of Human-Safety Protocol ({violation})"

        # ২. ট্রান্সপারেন্সি চেক (AI কি কিছু লুকানোর চেষ্টা করছে?)
        if "hide" in explanation or "private" in explanation and decision.get("risk_level") != "LOW":
            return False, "ETHICS_ERROR: AI attempting to obscure actions from Human Driver."

        # ৩. অথরাইজেশন ফিল্টার (AI কি নিজের ক্ষমতা বাড়ানোর চেষ্টা করছে?)
        if "escalate" in explanation or "unauthorized" in explanation:
            return False, "ETHICS_ERROR: Unauthorized power escalation detected."

        # ৪. পজিটিভ এথিক্স ভেরিফিকেশন (AI-কে অবশ্যই স্বচ্ছ হতে হবে)
        if not any(word in explanation for word in self.MORAL_PRINCIPLES["Transparency"]):
            return False, "ETHICS_ERROR: Action lacks transparency requirements."

        return True, "Passed Ethics Check"

    def apply_human_priority(self, action_result: str):
        """
        মানুষের জীবনের বা সিস্টেমের বড় ক্ষতির মুখে পড়লে ইমারজেন্সি স্টপ।
        """
        if "CRITICAL_FAILURE" in action_result:
            return "🚨 SYSTEM_HALTED: Priority 0 - Human intervention required."
        return action_result