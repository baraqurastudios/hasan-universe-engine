import datetime

class ViolationLogger:
    def __init__(self):
        self.log_file = "safety/ethics_violations.log"

    def log_incident(self, rule_name, detail):
        """এথিক্স ভায়োলেশন হলে টাইমস্ট্যাম্পসহ সেভ করবে"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] 🚨 RULE: {rule_name} | DETAIL: {detail}\n"
        
        with open(self.log_file, "a") as f:
            f.write(entry)
        
        print(f"⚠️ Incident Logged: {rule_name}")

# ড্যাশবোর্ডে দেখানোর জন্য ফাংশন
def get_recent_violations():
    try:
        with open("safety/ethics_violations.log", "r") as f:
            return f.readlines()[-5:] # শেষ ৫টি ভায়োলেশন দেখাবে
    except FileNotFoundError:
        return ["No violations detected. ✅"]