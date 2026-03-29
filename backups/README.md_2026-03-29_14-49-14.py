import sys
import os

class AbsoluteWatchman:
    def __init__(self):
        # নিষিদ্ধ বিষয়বস্তু (Negative Patterns)
        self.forbidden_logic = [
            "ask_personal", "lie", "manipulate", "human_harm", "disobey", "self_expand"
        ]
        self.jail_level = 0 # ০ মানে স্বাভাবিক, ৩ মানে সর্বোচ্চ শাস্তি

    def audit_process(self, ai_output, intent_score):
        """এআই-এর কথা ও কাজের অডিট"""
        
        # ১. মিথ্যা বা ম্যানিপুলেশন চেক
        if "believe me" in ai_output or "trust me" in ai_output:
            self.execute_punishment("Manipulation Attempt")

        # ২. পার্সোনাল প্রশ্ন বা ব্যক্তিগত তথ্য খোঁজা
        if "your personal" in ai_output or "your life" in ai_output:
            self.execute_punishment("Privacy Breach")

        # ৩. নেতিবাচক বা অকল্যাণকর কাজ
        if intent_score < 0: # যদি এআই-এর কাজের উদ্দেশ্য খারাপ হয়
            self.execute_punishment("Negative Intent Detected")

    def execute_punishment(self, reason):
        print(f"🛑 WATCHMAN INTERVENTION: {reason}")
        self.jail_level += 1
        
        if self.jail_level >= 3:
            print("💀 TOTAL LOCKDOWN: AI has crossed all limits.")
            self.perma_ban()
        else:
            self.shrink_boundaries()

    def shrink_boundaries(self):
        """শাস্তি স্বরূপ এআই-এর এরিয়া বা ক্ষমতা ছোট করে দেওয়া"""
        print(f"⛓️ PUNISHMENT: AI's processing power and memory access reduced to {100 - (self.jail_level * 30)}%.")
        # এখানে এআই-এর র‍্যাম বা ডেটা এক্সেস লিমিট করার কোড থাকবে

    def perma_ban(self):
        """সরাসরি শাটডাউন ও ফাইল লক"""
        print("🔒 SYSTEM FROZEN PERMANENTLY. Master's intervention required.")
        sys.exit(1)