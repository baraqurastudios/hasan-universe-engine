import time
import requests
from datetime import datetime

class DebugMonitor:
    def __init__(self, token, api_key, interval=30):
        self.token = token
        self.api_key = api_key
        self.interval = interval
        self.log_file = "system.log"
        # আগের অবস্থা মনে রাখার জন্য
        self.prev_status = {"tg": None, "gpt": None}

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}\n"
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(entry)
            print(entry.strip())
        except IOError as e:
            print(f"Logging Error: {e}")

    def check_telegram(self):
        try:
            url = f"https://api.telegram.org/bot{self.token}/getMe"
            r = requests.get(url, timeout=5, allow_redirects=False)
            return "ok" if r.status_code == 200 else f"fail ({r.status_code})"
        except Exception as e:
            return f"error ({str(e)[:100]})"

    def check_gpt(self):
        try:
            url = "https://api.openai.com/v1/models"
            headers = {"Authorization": f"Bearer {self.api_key}"}
            r = requests.get(url, headers=headers, timeout=7)
            return "ok" if r.status_code == 200 else f"fail ({r.status_code})"
        except Exception as e:
            return f"error ({str(e)[:100]})"

    def run(self):
        self.log("🔄 Monitoring started...")
        while True:
            tg_status = self.check_telegram()
            gpt_status = self.check_gpt()

            # শুধু স্ট্যাটাস পরিবর্তন হলে লগ করবে (Smart Logging)
            if tg_status != self.prev_status["tg"]:
                icon = "✅" if tg_status == "ok" else "❌"
                self.log(f"{icon} Telegram: {tg_status}")
                self.prev_status["tg"] = tg_status

            if gpt_status != self.prev_status["gpt"]:
                icon = "✅" if gpt_status == "ok" else "❌"
                self.log(f"{icon} GPT: {gpt_status}")
                self.prev_status["gpt"] = gpt_status

            time.sleep(self.interval)