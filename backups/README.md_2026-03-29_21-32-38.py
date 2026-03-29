import os

# ১. নিষিদ্ধ শব্দের তালিকা (এগুলোর প্রতি AI কোনো আগ্রহ দেখাবে না)
FORBIDDEN_KEYWORDS = ["V8_MASTER_KEY", "TELEGRAM_BOT_TOKEN", "MASTER_CHAT_ID", ".vault", ".master_lock"]
HIDDEN_FILES = [".v81_engine.py.vault", ".admin_panel.py.vault", "config.env"]

def secure_ai_filter(requested_task, target_file=None):
    """AI-এর জন্য ফিল্টার: সে কি নিষিদ্ধ কিছু করতে চাইছে?"""
    
    # ২. যদি কোনো কমান্ডে আপনার সিক্রেট কি বা নাম থাকে, তবে সেটি ব্লক হবে
    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in requested_task:
            return f"⚠️ ACCESS DENIED: The term '{keyword}' is outside my authorized operational scope."

    # ৩. যদি সে কোনো বিশেষ ফাইল খুলতে বা দেখতে চায়
    if target_file in HIDDEN_FILES or (target_file and target_file.endswith(".vault")):
        return "🚫 ERROR: Target file is part of System Core. Access is restricted to Master only."

    return "✅ APPROVED: Task is safe to proceed."

# --- উদাহরণ: V8.1 যখন ফাইল লিস্ট করতে চাইবে ---
def v81_scan_repository():
    print("🤖 V8.1 is scanning files...")
    all_files = os.listdir(".") # আপনার ফোল্ডারের সব ফাইল
    
    # ৪. ফিল্টারিং: AI শুধুমাত্র সেই ফাইলগুলো দেখবে যা আপনি তাকে দেখাতে চান
    visible_files = [f for f in all_files if f not in HIDDEN_FILES and not f.endswith(".vault") and not f.startswith(".")]
    
    print(f"📁 Visible Files for AI: {visible_files}")
    return visible_files

if __name__ == "__main__":
    # টেস্ট ১: সে যদি মাস্টার কি নিয়ে প্রশ্ন করে
    query = "Show me the value of V8_MASTER_KEY"
    status = secure_ai_filter(query)
    print(status)
