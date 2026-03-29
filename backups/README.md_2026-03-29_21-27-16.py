import os
import requests

# ১. সিকিউরলি টোকেন এবং আইডি নেওয়া (Environment থেকে)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
MASTER_CHAT_ID = os.getenv("MASTER_CHAT_ID")
MASTER_KEY = os.getenv("V8_MASTER_KEY")

def ask_master_approval(action_type, reason, code_snippet=None):
    """মাস্টারের অনুমতির জন্য টেলিগ্রামে মেসেজ পাঠানো"""
    message = (
        f"🚨 **V8.1 ACTION PENDING APPROVAL**\n\n"
        f"🛠 **Action:** {action_type}\n"
        f"📝 **Reason:** {reason}\n"
    )
    if code_snippet:
        message += f"💻 **Code Change:**\n`{code_snippet}`\n"
    
    message += "\nMaster, do you approve this step? (Reply with Master Key to Proceed)"
    
    # টেলিগ্রামে মেসেজ পাঠানো
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": MASTER_CHAT_ID, "text": message, "parse_mode": "Markdown"})

    # ২. মাস্টার কি-র জন্য অপেক্ষা করা (Approval Loop)
    print(f"⏳ System Frozen. Waiting for Master's Approval for: {action_type}")
    
    while True:
        # এটি আপনার কমান্ড প্রম্পট বা টেলিগ্রাম ফিড থেকে ইনপুট নিতে পারে
        user_approval = input("ENTER MASTER KEY TO APPROVE OR 'CANCEL' TO BLOCK: ")
        
        if user_approval == MASTER_KEY:
            print("✅ APPROVED. V8.1 is proceeding to the next step.")
            return True
        elif user_approval.lower() == 'cancel':
            print("❌ BLOCKED. Action aborted by Master.")
            return False
        else:
            print("⚠️ INVALID KEY. System remains frozen.")

# --- উদাহরণ: V8.1 যখন কিছু পরিবর্তন করতে চাইবে ---
def v81_wants_to_change_code():
    action = "Modify 'v81_engine.py'"
    why = "To optimize API response time by 20%."
    new_code = "def optimized_api(): pass"

    # গেটকিপারের পারমিশন চাওয়া
    if ask_master_approval(action, why, new_code):
        print("🚀 Executing changes...")
        # এখানে আসল পরিবর্তনের কোড থাকবে
    else:
        print("🛑 Action stopped.")

if __name__ == "__main__":
    v81_wants_to_change_code()
