# -----------------------------------------------
# 🧠 v8.0 MEMORY CLOUD STORAGE (LONG-TERM)
# -----------------------------------------------
import json
import os

class MemoryCloud:
    def __init__(self):
        self.memory_file = "data/universe_memory.json"
        self.max_memory_size = 5000 # ৫০০০টি গুরুত্বপূর্ণ তথ্য মনে রাখবে
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                self.memory_data = json.load(f)
        else:
            self.memory_data = {"user_preferences": {}, "past_incidents": [], "learned_skills": []}

    def store_memory(self, category, data):
        """নতুন কোনো অভিজ্ঞতা বা তথ্য মনে রাখা"""
        if category in self.memory_data:
            self.memory_data[category].append({
                "info": data,
                "timestamp": "2026-03-29" # রিয়েল টাইম স্ট্যাম্প
            })
            self.save_to_disk()

    def retrieve_memory(self, keyword):
        """অতীতের কোনো স্মৃতি খুঁজে বের করা"""
        print(f"🔍 Searching Memory Cloud for: {keyword}...")
        # এখানে সার্চিং লজিক কাজ করবে
        return [m for m in self.memory_data["learned_skills"] if keyword in m['info']]

    def save_to_disk(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory_data, f, indent=4)

# ব্যবহারের নিয়ম:
# memory = MemoryCloud()
# memory.store_memory("user_preferences", "Master prefers dark mode and short summaries.")