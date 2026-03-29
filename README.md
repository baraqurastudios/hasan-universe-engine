# -----------------------------
# 👑 HUMAN-IN-THE-LOOP (HITL) GATEWAY
# -----------------------------
def execute_safe_update_workflow(generated_code, user_approval=False):
    protector = SensitiveDataProtector()
    
    # ধাপ ১: সিকিউরিটি স্ক্যান (স্বয়ংক্রিয়)
    is_safe, message = protector.scan_generated_code(generated_code)
    
    if not is_safe:
        print(message)
        return "❌ Push Terminated: Safety Breach."

    # ধাপ ২: মাস্টারের অনুমতি (Manual Step)
    if not user_approval:
        print("⏳ Waiting for Master's approval in Oracle Editor...")
        return "PENDING_APPROVAL"

    # ধাপ ৩: চূড়ান্ত পুশ (শুধুমাত্র পারমিশন পেলে)
    print("🚀 Executing Safe Update to GitHub... Success!")
    return "PUSH_SUCCESS"