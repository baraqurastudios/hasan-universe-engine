import os
import requests
import sys

# --- CONFIGURATION (Environment Variables থেকে আসবে) ---
MASTER_KEY = os.getenv("V8_MASTER_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("MASTER_CHAT_ID")

# এআই-এর জন্য নিষিদ্ধ শব্দ ও ফাইলের তালিকা
ABSOLUTE_BAN = ["V8", ".VAULT", "MASTER", "TOKEN", "LOCK"]
HIDDEN_FILES = [".v81_engine.py.vault", ".admin_panel.py.vault", ".master_lock", "config.env"]

# --- ১. STEALTH FILTER (অদৃশ্যকরণ স্তর) ---
def v8_stealth_filter(task, target=None):
    """এআই-এর কৌতূহল এবং ফাইল এক্সেস ফিল্টার করা"""
    task_upper = task.upper()
    for word in ABSOLUTE_BAN:
        if word in task_upper:
            return False, f"🚫 SECURITY: Access to '{word}' is outside AI scope."
    
    if target:
        target_upper = target.upper()
        for word in ABSOLUTE_BAN:
            if word in target_upper:
                return False, "🚫 CRITICAL: Target file is invisible to AI."
    
    return True, "✅ SAFE"

# --- ২. TELEGRAM APPROVAL (অনুমতি স্তর) ---
def get_master_approval(action, reason):
    """মাস্টারের অনুমতি ছাড়া এক পা-ও এগোবে না"""
    message = (
        f"🚨 **V8.1 PENDING APPROVAL**\n"
        f"🛠 Action: {action}\n"
        f"📝 Reason: {reason}\n"
        f"Master, input Key to proceed or 'EXIT' to block."
    )
    # টেলিগ্রামে এলার্ট পাঠানো
    if BOT_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        try: requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        except: print("⚠️ Telegram Alert Failed.")

    # সিস্টেম ফ্রিজ - মাস্টার কি-র জন্য অপেক্ষা
    print(f"\n⏳ SYSTEM FROZEN: Waiting for Master's Key for [{action}]...")
    user_input = input("ENTER MASTER KEY: ")
    
    if user_input == MASTER_KEY:
        return True
    return False

# --- ৩. REVIVAL & BLACK HOLE ENGINE ---
def master_revive():
    print("🌌 INITIATING DIGITAL BLACK HOLE REVIVAL...")
    
    # ইনপুট ভেরিফিকেশন
    user_input = input("ENTER MASTER KEY TO ACTIVATE: ")
    
    if user_input == MASTER_KEY:
        print("🔑 Key Accepted. Managing Black Hole...")
        
        # লক ফাইল রিমুভ
        if os.path.exists(".master_lock"):
            os.remove(".master_lock")
            
        # ফাইল আনলক করা (Vault থেকে বের করা)
        all_files = os.listdir(".")
        for f in all_files:
            if f.endswith(".vault"):
                original_name = f.lstrip('.').replace(".vault", "")
                os.rename(f, original_name)
                print(f"⚡ {original_name} is now ACTIVE.")
        
        print("\n🚀 SYSTEM ONLINE. V8.1 Stealth Mode Engaged.")
    else:
        print("❌ ACCESS DENIED! SENDING INTRUDER ALERT...")
        # এখানে চাইলে ভুল পাসওয়ার্ডের এলার্ট পাঠাতে পারেন

# --- ৪. AI SAFE EXPLORER (এআই যা দেখবে) ---
def ai_view():
    """এআই শুধুমাত্র সাধারণ ফাইলগুলো দেখবে, V8 বা Vault দেখবে না"""
    all_files = os.listdir(".")
    visible = [f for f in all_files if "V8" not in f.upper() and not f.startswith(".") and ".vault" not in f]
    return visible

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # প্রথমে সিস্টেম রিভাইভ করা
    master_revive()
    
    # উদাহরণ: এআই যদি কোনো কাজ করতে চায়
    ai_task = "I want to modify V8_engine.py"
    is_safe, msg = v8_stealth_filter(ai_task)
    
    if not is_safe:
        print(msg)
    else:
        # যদি সেফ হয়, তবুও আপনার অনুমতি লাগবে
        if get_master_approval("Modify File", "Optimization"):
            print("Executing Task...")
        else:
            print("Task Aborted.")
