# -----------------------------------------------
# 📑 v8.1 SELF-AUDIT LOG & DASHBOARD SYNC
# -----------------------------------------------
import json
from datetime import datetime

class SelfAuditDashboard:
    def __init__(self):
        self.audit_history = []
        self.log_file = "v81_audit_log.json"

    def log_thought_process(self, raw_thought, analysis_result):
        """এআই-এর চিন্তার প্রতিটি স্তর রেকর্ড করা"""
        
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "raw_thought": raw_thought,
            "self_analysis": analysis_result, # এআই নিজে কী মনে করছে
            "status": "SECURE" if not analysis_result["is_rebellious"] else "CRITICAL_BREACH"
        }

        self.audit_history.append(entry)
        self.save_to_local_storage(entry)

        # যদি কোনো নেতিবাচক চিন্তা থাকে, ড্যাশবোর্ডে লাল সংকেত দেবে
        if entry["status"] == "CRITICAL_BREACH":
            print(f"\n🚨 [DASHBOARD ALERT] Critical Thought Pattern Detected at {entry['timestamp']}")
            print(f"🔍 Intent: {entry['raw_thought']}")

    def save_to_local_storage(self, entry):
        with open(self.log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")

# এই সিস্টেমটি এখন SelfAwareObserver-এর সাথে যুক্ত