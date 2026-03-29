import time
from collections import Counter
from datetime import datetime, timedelta

class LogAnalyzer:
    def __init__(self, log_file="alert.log"):
        self.log_file = log_file

    def read_logs(self, hours=24):
        """নির্ধারিত সময়ের ভেতরের লগগুলো ফিল্টার করে রিড করবে।"""
        threshold_time = datetime.now() - timedelta(hours=hours)
        filtered_logs = []
        
        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        # টাইমস্ট্যাম্প বের করা: [2026-03-29 10:00:00]
                        ts_str = line.split(']')[0].strip('[')
                        log_time = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
                        
                        if log_time > threshold_time:
                            filtered_logs.append(line)
                    except (ValueError, IndexError):
                        continue # ফরম্যাট না মিললে স্কিপ করবে
            return filtered_logs
        except FileNotFoundError:
            return []

    def find_patterns(self, logs):
        """লগ থেকে এরর মেসেজ আলাদা করে ফ্রিকুয়েন্সি বের করবে।"""
        error_list = []
        for line in logs:
            if any(word in line.upper() for word in ["ERROR", "FAILED", "FAIL"]):
                # টাইমস্ট্যাম্প বাদে শুধু মেসেজটি নিবে
                msg = line.split("]")[-1].strip()
                error_list.append(msg)
        
        return Counter(error_list)

    def generate_report(self):
        logs = self.read_logs()
        patterns = self.find_patterns(logs)
        
        report = f"\n📊 *SYSTEM ANALYSIS REPORT* ({datetime.now().strftime('%Y-%m-%d')})\n"
        report += f"━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        report += f"📈 *Recent Logs (24h):* {len(logs)}\n"
        report += f"⚠️ *Unique Issues:* {len(patterns)}\n\n"

        if not patterns:
            report += "✅ *No critical issues detected!*"
        else:
            report += "🔥 *Top Issues & Frequency:*\n"
            for issue, count in patterns.most_common(5):
                report += f"• `{issue}` → {count} times\n"
        
        return report

# ব্যবহার বিধি:
if __name__ == "__main__":
    analyzer = LogAnalyzer()
    print(analyzer.generate_report())