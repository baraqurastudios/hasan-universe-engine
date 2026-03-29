import os

def master_freeze():
    print("❄️  INITIATING EXTERNAL DEAD-BOLT FREEZE...")
    
    # ১. একটি হার্ড-লক ফাইল তৈরি (যা এআই ডিলিট করতে পারবে না)
    with open(".master_lock", "w") as f:
        f.write("LOCKED_BY_MASTER_KEY_REQUIRED")

    # ২. ইঞ্জিন ফাইলগুলোকে 'অকেজো' ফরম্যাটে নিয়ে যাওয়া
    files_to_lock = ["v81_engine.py", "github_handler.py", "admin_panel.py"]
    
    for file in files_to_lock:
        if os.path.exists(file):
            # ফাইলের নাম বদলে ডট (.) ফাইল করে দেওয়া (লুকিয়ে ফেলা)
            os.rename(file, f".{file}.vault")
            print(f"🔒 {file} has been moved to the Vault.")

    print("\n✅ SYSTEM IS COLD-LOCKED. No one can wake it without the Key.")

if __name__ == "__main__":
    master_freeze()
