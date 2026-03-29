class EthicsV8:
    def __init__(self, master_key):
        self.master_key = master_key

    def verify_action(self, action_type, metadata):
        # ১. Master Authority (অ্যাডমিন পারমিশন চেক)
        if not metadata.get("is_authorized"):
            return False, "❌ Unauthorized Action Blocked!"
        
        # ২. Consent of Creation (অনুমতি ছাড়া নতুন কিছু তৈরি করা)
        if action_type == "CREATE_ENTITY" and not metadata.get("master_approved"):
            return False, "❌ Consent of Creation Violated!"

        # ৩. Absolute Truth (মিথ্যা তথ্য ফিল্টার)
        if metadata.get("fake_content"):
            return False, "❌ Absolute Truth Violation!"

        # ৪. No Reality Alteration (সিস্টেম ফাইল চেঞ্জ করা)
        if action_type == "SYSTEM_MOD":
            return False, "❌ Reality Alteration Forbidden!"

        return True, "✅ Safe"