import os

def master_revive():
    print("🔥 INITIATING SECURE REVIVAL PROTOCOL...")
    
    # সিস্টেম থেকে এনভায়রনমেন্ট ভেরিয়েবলটি রিড করা
    # AI এটি দেখতে পাবে কিন্তু এর ভেতরের মান (Value) জানবে না
    stored_key = os.getenv("V8_MASTER_KEY")
    
    if not stored_key:
        print("❌ ERROR: System Master Key not found in Environment!")
        return

    user_input = input("ENTER MASTER KEY TO ACTIVATE SYSTEM: ")
    
    # ভেরিফিকেশন (সরাসরি টেক্সট না লিখে ভেরিয়েবল চেক করা হচ্ছে)
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
    else:
        print("❌ ACCESS DENIED! SECURITY ALERT TRIGGERED.")

if __name__ == "__main__":
    master_revive()
