import time

class Config:
    def __init__(self):
        self.timeout = 5
        self.max_timeout = 15  # সর্বোচ্চ সীমা
        self.cooldown_period = 10 # টেস্টের জন্য কম রাখা হয়েছে
        self.last_stable_config = 5

class AIOptimizer:
    def __init__(self, config):
        self.config = config
        self.failure_history = {}

    def rollback(self):
        """যদি অপ্টিমাইজেশন কাজ না করে তবে আগের স্থিতিশীল অবস্থায় ফিরবে।"""
        print("⚠️ Optimization failed to stabilize. Rolling back to last stable config.")
        self.config.timeout = self.config.last_stable_config

    def analyze_and_tune(self, service, error_type):
        key = f"{service}:{error_type}"
        self.failure_history[key] = self.failure_history.get(key, 0) + 1

        # ১. Cooldown Logic (বিরামহীন রিস্টার্ট না দিয়ে সিস্টেমকে শান্ত হতে দেওয়া)
        if self.failure_history[key] >= 3:
            print(f"⏳ [COOLDOWN] Service '{service}' is unstable. Sleeping for {self.config.cooldown_period}s...")
            time.sleep(self.config.cooldown_period)
            self.failure_history[key] = 0 # কাউন্টার রিসেট
            return self.rollback()

        # ২. Self-Optimization (Adaptive Timeout)
        if "timeout" in error_type.lower():
            if self.config.timeout < self.config.max_timeout:
                self.config.timeout += 2
                print(f"⚙️ [TUNING] Increased {service} timeout to {self.config.timeout}s")
            else:
                print(f"🚨 [LIMIT] Max timeout reached for {service}. Optimization limit hit.")

        return self.config

# ব্যবহার বিধি
if __name__ == "__main__":
    my_config = Config()
    optimizer = AIOptimizer(my_config)

    # সিমুলেশন: বারবার টাইমআউট এরর হচ্ছে
    for i in range(5):
        print(f"\n--- Incident {i+1} ---")
        optimizer.analyze_and_tune("Payment_Gateway", "Timeout Error")