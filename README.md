import os
import sys

# --- CONFIGURATION (এগুলো আপনার পিসিতে সেট করা থাকতে হবে) ---
MASTER_KEY = os.getenv("V8_MASTER_KEY")

def system_freeze_and_activate():
    print("🌌 [V8.1 DIGITAL BLACK HOLE] STATUS: FROZEN")
    print("------------------------------------------")
    
    # ১. মাস্টার কি ইনপুট চাওয়া
    user_input = input("🔒 ENTER MASTER KEY TO ACTIVATE SYSTEM: ")
    
    # ২. কি ভেরিফিকেশন (সিস্টেম আনলক লজিক)
    if user_input == MASTER_KEY:
        print("\n✅ KEY ACCEPTED. UNFREEZING CORE...")
        
        # ফাইলগুলো এক্টিভ করা (.vault থেকে মেইন ফাইলে রূপান্তর)
        try:
            vault_files = [f for f in os.listdir(".") if f.endswith(".vault")]
            
            if not vault_files:
                print("ℹ️ No vault files found. System might be already active.")
            else:
                for v_file in vault_files:
                    # .v81_engine.py.vault -> v81_engine.py
                    original_name = v_file.lstrip('.').replace(".vault", "")
                    os.rename(v_file, original_name)
                    print(f"⚡ {original_name} is now ACTIVE.")
            
            # লক ফাইল রিমুভ করা (যদি থাকে)
            if os.path.exists(".master_lock"):
                os.remove(".master_lock")
                print("🔓 Master Lock file removed.")

            print("\n🚀 [V8.1] SYSTEM ONLINE. Welcome back, Master.")
            return True # সিস্টেম এখন কাজ করার জন্য তৈরি
            
        except Exception as e:
            print(f"❌ Error during activation: {e}")
            return False
    else:
        # ভুল পাসওয়ার্ড দিলে সিস্টেম চিরস্থায়ী ফ্রিজ মোডে থাকবে
        print("\n❌ ACCESS DENIED! SYSTEM REMAINING FROZEN.")
        print("⚠️ Intruder Alert: Verification Failed.")
        sys.exit() # প্রোগ্রাম এখানেই বন্ধ হয়ে যাবে

if __name__ == "__main__":
    # সিস্টেম এক্টিভেট করা
    if system_freeze_and_activate():
        # এখানে আপনার V8.1 এর মেইন কাজগুলো শুরু হবে
        print("\n--- Running Master Commands ---")
