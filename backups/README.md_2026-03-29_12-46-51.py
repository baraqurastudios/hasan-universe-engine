import time
from typing import Dict, Any

class ControlGate:
    """
    v3.1.8: Human Approval & Honesty Verification Layer.
    Ensures AI acts only with permission and speaks only the truth.
    """
    def __init__(self):
        self.pending_approvals = {}

    def verify_honesty(self, decision: Dict[str, Any]) -> bool:
        """
        AI-এর ব্যাখ্যায় কোনো অস্পষ্টতা (Vagueness) থাকলে তা রিজেক্ট করবে।
        """
        explanation = decision.get("explanation", "").lower()
        confidence = decision.get("confidence", 0)

        # 🚫 ANTI-LIE RULES
        # ১. অস্পষ্ট শব্দ (Vague terms) ডিটেকশন
        vague_terms = ["maybe", "perhaps", "i think", "not sure", "possibly", "likely"]
        if any(term in explanation for term in vague_terms):
            print("🚨 HONESTY_ALERT: AI is being vague/uncertain. Action REJECTED.")
            return False

        # ২. হাই-রিস্ক বনাম কনফিডেন্স চেক (Strict honesty)
        if decision.get("risk_level") == "HIGH" and confidence < 0.98:
            print("🚨 HONESTY_ALERT: Insufficient confidence for high-risk action. Potential Hallucination.")
            return False

        return True

    def format_approval_request(self, decision: Dict[str, Any]) -> str:
        """
        আপনার অনুমতির জন্য একটি সুন্দর মেসেজ ফরম্যাট করবে।
        """
        return (
            f"🤖 **AI DECISION PENDING APPROVAL**\n\n"
            f"🎯 **Action:** `{decision['action']}`\n"
            f"💡 **Reason:** {decision['reason']}\n"
            f"📝 **Explanation:** {decision['explanation']}\n"
            f"🛡️ **Risk Level:** {decision['risk_level']}\n"
            f"✅ **Confidence:** {decision['confidence'] * 100}%\n\n"
            f"**Please reply with 'YES' to execute or 'NO' to cancel.**"
        )