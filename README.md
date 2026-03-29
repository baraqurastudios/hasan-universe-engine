import requests
import time
from datetime import datetime

class AlertSystem:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.log_file = "alert.log"

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}\n"
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(entry)
            print(entry.strip())
        except Exception as e:
            print(f"File Logging Error: {e}")

    def send_telegram(self, message, retries=2):
        """টেলিগ্রামে মেসেজ পাঠানোর চেষ্টা করবে এবং ফেইল করলে রিট্রাই করবে।"""
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {"chat_id": self.chat_id, "text": message, "parse_mode": "Markdown"} # বোল্ড/ইটালিকের জন্য

        for i in range(retries):
            try:
                r = requests.post(url, data=data, timeout=7)
                if r.status_code == 200:
                    return True
                # ৪২৯ মানে রেট লিমিট, একটু অপেক্ষা করা ভালো
                if r.status_code == 429:
                    time.sleep(2)
            except Exception:
                time.sleep(1) # নেটওয়ার্ক ফ্লিকার করলে ১ সেকেন্ড ওয়েট
        return False

    def alert(self, error_message, source="Unknown"):
        # মেসেজটি একটু সুন্দরভাবে সাজানো হয়েছে
        msg = f"🚨 *SYSTEM ALERT*\n\n📍 *Source:* {source}\n⚠️ *Error:* `{error_message}`\n🕒 *Time:* {datetime.now().strftime('%H:%M:%S')}"

        if self.send_telegram(msg):
            self.log(f"✅ Alert Sent to Telegram (Source: {source})")
        else:
            self.log(f"⚠️ Telegram FAILED! Saved Offline: {error_message}")