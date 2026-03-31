import os

def recover_vault():
    old_name = ".hidden_vault_locked"
    new_name = "v82_config.json"
    
    # বর্তমান ডিরেক্টরিতে আপনার ফোল্ডারের পাথ সেট করুন
    path = "BaraQura_V8.2_Core/" 
    
    if os.path.exists(path + old_name):
        os.rename(path + old_name, path + new_name)
        print("🔓 Success: Your Vault has been recovered and unlocked!")
    else:
        print("❌ Error: Locked vault not found. Maybe it's already open?")

if __name__ == "__main__":
    recover_vault()
  
