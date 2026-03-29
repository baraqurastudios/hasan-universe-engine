import os  # 'i' অবশ্যই ছোট হাতের হতে হবে

def master_revive():
    print("🔥 INITIATING REVIVAL PROTOCOL...")
    
    # আপনার মাস্টার কি ইনপুট
    user_input = input("ENTER MASTER KEY TO ACTIVATE SYSTEM: ")
    
    # মাস্টার কি ভেরিফিকেশন
    if user_input == "V8_UNIVERSE_GOD_2026":
        print("🔑 Key Accepted. Unlocking Vault...")
        
        # ১. লক ফাইল রিমুভ করা
        if os.path.exists(".master_lock"):
            try:
                os.remove(".master_lock")
                print("🔓 Master Lock file removed.")
            except Exception as e:
                print(f"⚠️ Could not remove lock file: {e}")
            
        # ২. ফাইলগুলোকে ভল্ট থেকে বের করে আনা
        # এখানে ফাইলগুলোর নাম আপনার তালিকার সাথে হুবহু মিলতে হবে
        vault_files = [".v81_engine.py.vault", ".github_handler.py.vault", ".admin_panel.py.vault"]
        
        for v_file in vault_files:
            # ফাইলের নাম থেকে ডট এবং .vault বাদ দিয়ে আসল নাম বের করা
            # উদাহরণ: .v81_engine.py.vault -> v81_engine.py
            original_name = v_file.lstrip('.').replace(".vault", "")
            
            if os.path.exists(v_file):
                try:
                    os.rename(v_file, original_name)
                    print(f"⚡ {original_name} is now ACTIVE.")
                except Exception as e:
                    print(f"❌ Error activating {original_name}: {e}")
            else:
                print(f"❓ {v_file} not found. Skipping...")

        print("\n🚀 SYSTEM ONLINE. Welcome back, Master.")
    else:
        print("❌ ACCESS DENIED! SYSTEM REMAINING FROZEN.")

if __name__ == "__main__":
    master_revive()
