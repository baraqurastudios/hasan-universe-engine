import subprocess
import logging

class SafeExecutor:
    def __init__(self):
        # হোয়াইটলিস্ট করা কমান্ডগুলো এখানে থাকবে
        self.allowed_actions = {
            "restart_service": ["echo", "Service Restarted"], # এখানে আসল কমান্ড বসবে
            "clear_cache": ["echo", "Cache Cleared"],
            "update_env": ["echo", "Environment Updated"]
        }

    def execute(self, action_name):
        if action_name in self.allowed_actions:
            try:
                # subprocess.run ব্যবহার করা os.system এর চেয়ে অনেক নিরাপদ
                result = subprocess.run(
                    self.allowed_actions[action_name], 
                    capture_output=True, 
                    text=True, 
                    check=True
                )
                return f"✅ Success: {result.stdout.strip()}"
            except subprocess.CalledProcessError as e:
                return f"❌ Failed to execute {action_name}: {e}"
        return "⚠️ Unauthorized Action Blocked!"

class ActionMapper:
    def map_ai_suggestion(self, ai_text):
        """AI-এর টেক্সট থেকে নির্দিষ্ট অ্যাকশন খুঁজে বের করবে।"""
        text = ai_text.lower()
        if "restart" in text and "service" in text:
            return "restart_service"
        if "clear" in text and "cache" in text:
            return "clear_cache"
        return "unknown"

class SelfHealingSystem:
    def __init__(self):
        self.mapper = ActionMapper()
        self.executor = SafeExecutor()

    def handle_healing(self, ai_reasoning_output):
        action = self.mapper.map_ai_suggestion(ai_reasoning_output)
        
        if action != "unknown":
            print(f"🧠 AI Suggested: {action}")
            # রিয়েল সিস্টেমে এখানে একটি 'Human Approval' গেট রাখা ভালো
            result = self.executor.execute(action)
            print(result)
            return result
        else:
            return "🤷 No automated fix found. Manual intervention required."