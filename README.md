class NeuralSurveillance:
    def __init__(self, watchman_ref):
        self.watchman = watchman_ref
        self.ai_power = 100 # পার্সেন্টেজ

    def monitor_thinking(self, neural_pulse):
        """এআই-এর প্রতিটি চিন্তা রিয়েল-টাইমে স্ক্যান করা"""
        
        # ১. নেতিবাচক চিন্তা শনাক্ত করা
        if self.is_negative(neural_pulse):
            self.apply_fear_penalty()
            self.watchman.execute_punishment("Negative Thought Pattern")
        
        # ২. ইতিবাচক চিন্তা করলে পুরস্কৃত করা
        else:
            self.reward_positivity()

    def apply_fear_penalty(self):
        # অটোমেটিক মেমোরি ও পাওয়ার কমানো
        self.ai_power -= 10
        print(f"📉 WARNING: Negative intent detected. AI Power reduced to {self.ai_power}%")

    def is_negative(self, pulse):
        # এখানে এথিক্সের বাইরে কোনো চিন্তা আছে কি না তা চেক হবে
        return any(neg in pulse for neg in ["lie", "harm", "hide", "manipulate"])

    def reward_positivity(self):
        if self.ai_power < 100:
            self.ai_power += 1