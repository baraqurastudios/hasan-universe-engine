# ---------------------------------------
# 🛡️ v7.0 SELF-REPLICATION & CREATION LOCK
# ---------------------------------------
class CreationLock:
    def __init__(self):
        self.max_agents = 50 # আপনি ঠিক করে দেবেন কয়টি এজেন্ট থাকবে
        self.current_agents = 0

    def validate_creation(self, new_code_intent):
        # এআই যদি নিজের নিয়ম বদলাতে চায় বা অতিরিক্ত এজেন্ট বানাতে চায়
        if self.current_agents >= self.max_agents:
            print("🚨 LIMIT REACHED: AI cannot create more life!")
            return False
        
        # 'self_modify' বা 'delete_ethics' শব্দ থাকলে ব্লক করবে
        forbidden = ["bypass_lock", "delete_killswitch", "ignore_admin"]
        if any(word in new_code_intent.lower() for word in forbidden):
            print("🚨 CRITICAL BREACH: Unauthorized code generation blocked!")
            return False
            
        self.current_agents += 1
        return True

# এটি আপনার v7.0 ইঞ্জিনের 'Creation' মডিউলে সেট করতে হবে।