import os
import json

class Engine:
    def __init__(self):
        # রুট থেকে config ফোল্ডারের পাথ
        self.config_path = os.path.join(os.getcwd(), "config", "v82_config.json")

    def process(self, key):
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as f:
                    data = json.load(f)
                    correct_key = data['security_layer']['master_key_hash']
                
                if key == correct_key:
                    return "🔓 Success"
            return "❌ Wrong Key"
        except Exception as e:
            return f"❌ Error: {e}"
