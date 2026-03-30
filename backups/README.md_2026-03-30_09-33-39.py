import os

def update_file_explorer():
    print("🔍 Refreshing Repository Explorer...")
    # হিডেন ডিরেক্টরি স্ক্যান করার লজিক
    hidden_path = ".github/workflows/v8_auto_run.yml"
    if os.path.exists(hidden_path):
        print(f"✅ Found hidden asset: {hidden_path}")
    else:
        print("❌ Asset not found in current view.")
    return True

if __name__ == "__main__":
    update_file_explorer()
