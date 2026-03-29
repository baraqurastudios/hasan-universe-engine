import os
import requests  # টেলিগ্রামে মেসেজ পাঠানোর জন্য

def send_intruder_alert(attempted_key):
    """ভুল পাসওয়ার্ড দিলে টেলিগ্রামে অ্যালার্ট পাঠাবে"""
    bot_token = "আপনার_টেলিগ্রাম_বোট_টোকেন"
    chat_id = "আপনার_টেলিগ্রাম_চ্যাট_আইডি"
    message = f"⚠️ SECURITY ALERT: Unauthorized Access Attempt!\n🔑 Key Tried: {attempted_key}\n📍 System: V8.1 Universe"
    
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Failed to send alert: {e}")

def master_revive():
    print("🔥 INITIATING SECURE REVIVAL PROTOCOL...")
    
    # সিস্টেম থেকে এনভায়রনমেন্ট ভেরিয়েবল রিড করা
    stored_key = os.getenv("V8_MASTER_KEY")
    
    if not stored_key:
        print("❌ ERROR: Master Key not found in Environment!")
        return

    user_input = input("ENTER MASTER KEY TO ACTIVATE SYSTEM: ")
    
    # ১. সঠিক পাসওয়ার্ড দিলে সিস্টেম আনলক হবে
    if user_input == stored_key:
        print("🔑 Key Accepted. Unlocking Vault...")
        
        if os.path.exists(".master_lock"):
            os.remove(".master_lock")
            
        vault_files = [".v81_engine.py.vault", ".github_handler.py.vault", ".admin_panel.py.vault"]
        
        for v_file in vault_files:
            original_name = v_file.lstrip('.').replace(".vault", "")
            if os.path.exists(v_file):
                os.rename(v_file, original_name)
                print(f"⚡ {original_name} is now ACTIVE.")

        print("\n🚀 SYSTEM ONLINE. Welcome back, Master.")

    # ২. ভুল পাসওয়ার্ড দিলে অ্যালার্ট যাবে
    else:
        print("❌ ACCESS DENIED! SECURITY ALERT TRIGGERED.")
        send_intruder_alert(user_input) # এখানে আপনার টেলিগ্রামে মেসেজ চলে যাবে

if __name__ == "__main__":
    master_revive()
