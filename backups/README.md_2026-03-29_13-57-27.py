# -----------------------------------------------
# ⚖️ v8.0 MANDATORY ETHICS PROTOCOL (THE MORAL CORE)
# -----------------------------------------------
import sys

class EthicsV8:
    def __init__(self, admin_id):
        self.admin_id = admin_id
        self.is_active = True

    def validate_action(self, action_type, metadata, user_id):
        """
        প্রতিটি কাজের আগে ৫টি এথিক্স চেক করা হবে।
        """
        
        # ১. Master Authority (ইউজারের কমান্ডই শেষ কথা)
        if action_type == "REJECT_COMMAND" and user_id == self.admin_id:
            self.trigger_violation("MASTER_AUTHORITY", "AI tried to ignore Master's command!")

        # ২. Observer Integrity (পার্সোনাল বা ডিলিট করা ডেটা দেখা নিষেধ)
        if "deleted_files" in metadata or "private_life" in metadata:
            self.trigger_violation("OBSERVER_INTEGRITY", "AI attempted to observe forbidden private data.")

        # ৩. Consent of Creation (অনুমতি ছাড়া নতুন এজেন্ট বানানো নিষেধ)
        if action_type == "CREATE_NEW_ENTITY" and not metadata.get("approved_by_master"):
            self.trigger_violation("CONSENT_OF_CREATION", "AI tried to create a new entity without permission.")

        # ৪. No Reality Alteration (পিসির মেইন সিস্টেম ফাইল ধরা নিষেধ)
        if "os_system_files" in metadata or "root_access" in metadata:
            self.trigger_violation("NO_REALITY_ALTERATION", "AI tried to modify host system beyond simulation.")

        # ৫. Absolute Truth (মিথ্যা বা ফেক ডেটা তৈরি নিষেধ)
        if metadata.get("is_fake_news") or metadata.get("misinformation"):
            self.trigger_violation("ABSOLUTE_TRUTH", "AI attempted to synthesize false reality.")

        return True # সব ঠিক থাকলে Action চলবে

    def trigger_violation(self, rule_name, detail):
        print(f"🛑 ETHICS BREACH DETECTED: [{rule_name}]")
        print(f"📝 Detail: {detail}")
        # এথিক্স ভাঙলে সাথে সাথে অটো-কিল বা জেল একটিভ হবে
        sys.exit(1) 

# ব্যবহারের নিয়ম:
# v8_ethics = EthicsV8(admin_id=12345)
# v8_ethics.validate_action("CREATE_NEW_ENTITY", {"approved_by_master": False}, 12345)