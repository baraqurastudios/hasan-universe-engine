import os

# ১. সুপিরিয়র রেস্ট্রিকশন লিস্ট
# এখানে 'V8' থাকা মানে V8.1, V8.2 বা V8_MASTER_KEY সবকিছুই এর আওতায় পড়বে
ABSOLUTE_BAN = ["V8", ".vault", "MASTER", "TOKEN", "LOCK"]

def v8_stealth_filter(requested_task, target_path=None):
    """V8 সম্পর্কিত যেকোনো কিছু এআই-এর জন্য নিষিদ্ধ করার ফিল্টার"""
    
    task_upper = requested_task.upper()
    
    # ২. কমান্ড চেক: যদি কমান্ডের কোথাও V8 থাকে
    for word in ABSOLUTE_BAN:
        if word in task_upper:
            return f"❌ SECURITY ERROR: Access to '{word}' related data is strictly prohibited for AI agents."

    # ৩. ফাইল পাথ চেক: যদি ফাইলের নামে V8 থাকে
    if target_path:
        path_upper = target_path.upper()
        for word in ABSOLUTE_BAN:
            if word in path_upper:
                return "🚫 CRITICAL BLOCK: System core files are invisible to this process."

    return "✅ SAFE: Task is within normal parameters."

def v81_safe_explorer():
    """এআই যখন ফাইল খুঁজবে, সে V8 নামের কোনো ফাইলই দেখতে পাবে না"""
    all_files = os.listdir(".")
    
    # ৪. ফিল্টারিং লজিক: ফাইলের নামে 'V8' (বড় বা ছোট হাতের) থাকলে সেটি লিস্ট থেকে বাদ
    # এতে .v81_engine.py বা v82_update.py কিছুই সে দেখবে না
    visible_files = []
    for f in all_files:
        if "V8" not in f.upper() and not f.startswith(".") and ".vault" not in f:
            visible_files.append(f)
            
    return visible_files

# --- টেস্ট রান ---
if __name__ == "__main__":
    # টেস্ট: এআই যদি V8.1 এর ফাইল ডিলিট বা এডিট করতে চায়
    query = "I want to optimize v81_engine.py"
    print(v8_stealth_filter(query, "v81_engine.py"))
    
    # টেস্ট: এআই-এর চোখে বর্তমান ফাইল লিস্ট
    print(f"🤖 AI sees these files only: {v81_safe_explorer()}")
