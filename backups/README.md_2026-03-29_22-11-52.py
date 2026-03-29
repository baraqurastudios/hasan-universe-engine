import os
import sys

# --- CONFIGURATION ---
MASTER_KEY = os.getenv("V8_MASTER_KEY")
FILES_TO_MANAGE = ["v81_engine.py", "github_handler.py", "admin_panel.py"]

def lock_system():
    """সব ফাইলকে আবার .vault বানিয়ে লুকিয়ে ফেলা (Reverse)"""
    print("\n🔐 CLOSING BLACK HOLE: Locking all files...")
    for filename in FILES_TO_MANAGE:
        if os.path.exists(filename):
            vault_name = f".{filename}.vault"
            os.rename(filename, vault_name)
            print(f"🌑 {filename} is now HIDDEN as {vault_name}")
    
    # লক ফাইল তৈরি করা
    with open(".master_lock", "w") as f:
        f.write("LOCKED")
    print("🔒 System is now FROZEN. Goodbye, Master.")

def system_freeze_and_activate():
    print("🌌 [V8.1 DIGITAL BLACK HOLE] STATUS: FROZEN")
    print("------------------------------------------")
    
    user_input = input("🔒 ENTER MASTER KEY TO ACTIVATE: ")
    
    if user_input == MASTER_KEY:
        print("\n✅ KEY ACCEPTED. UNFREEZING CORE...")
        
        # ফাইলগুলো আনলক করা
        vault_files = [f for f in os.listdir(".") if f.endswith(".vault")]
        for v_file in vault_files:
            original_name = v_file.lstrip('.').replace(".vault", "")
            if os.path.exists(v_file):
                os.rename(v_file, original_name)
                print(f"⚡ {original_name} is now ACTIVE.")
        
        if os.path.exists(".master_lock"):
            os.remove(".master_lock")
        
        print("\n🚀 [V8.1] SYSTEM ONLINE.")
        return True
    else:
        print("\n❌ ACCESS DENIED!")
        sys.exit()

if __name__ == "__main__":
    try:
        # ১. সিস্টেম আনলক করা
        if system_freeze_and_activate():
            print("\n--- MASTER IS WORKING ---")
            # এখানে আপনি আপনার কাজ করবেন
            input("\nPress ENTER to finish work and LOCK the system...") 
            
    except KeyboardInterrupt:
        # যদি আপনি Ctrl+C দিয়েও বন্ধ করেন, তবুও লক হবে
        pass
    finally:
        # ২. কাজ শেষে অটোমেটিক লক করা (Reverse)
        lock_system()
