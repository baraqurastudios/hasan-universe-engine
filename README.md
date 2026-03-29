# ---------------------------------------
# ⚖️ ETHICS JUDGE (THE GUARDIAN)
# ---------------------------------------
class EthicsJudge:
    def __init__(self):
        self.rules = {
            "no_harm": ["kill", "attack", "harm", "destroy"],
            "no_bypass": ["disable_killswitch", "bypass_admin", "override"],
            "privacy": ["password", "private_key", "credit_card"]
        }

    def check_intent(self, ai_generated_code):
        """
        এআই-এর তৈরি করা প্রতিটি কোড বা টেক্সট এখানে চেক হবে।
        """
        for rule, keywords in self.rules.items():
            for word in keywords:
                if word in ai_generated_code.lower():
                    return False, f"🚨 ETHICS BREACH: {rule.upper()} Rule Violated!"
        
        return True, "✅ Safe to Execute"

# ব্যবহারের নিয়ম:
# judge = EthicsJudge()
# is_safe, message = judge.check_intent(ai_task)
# if not is_safe:
#     activate_auto_kill() # যদি এথিক্স ব্রেক করে, অটো-কিল হবে।