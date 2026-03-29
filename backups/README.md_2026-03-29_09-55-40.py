import requests

class DebugCore:
    def __init__(self):
        self.status = {
            "telegram": "unknown",
            "gpt": "unknown",
            "server": "running",
            "last_error": None
        }

    def check_telegram(self, token):
        try:
            url = f"https://api.telegram.org/bot{token}/getMe"
            # Security and efficiency
            r = requests.get(url, timeout=5, allow_redirects=False)
            if r.status_code == 200:
                self.status["telegram"] = "ok"
            else:
                self.status["telegram"] = f"fail ({r.status_code})"
                # লিমিটেড টেক্সট রাখা হয়েছে যাতে মেমোরি লোড কম হয়
                self.status["last_error"] = r.text[:200]
        except requests.exceptions.RequestException as e:
            self.status["telegram"] = "network_error"
            self.status["last_error"] = str(e)[:200]

    def check_gpt(self, api_key):
        try:
            url = "https://api.openai.com/v1/models"
            headers = {"Authorization": f"Bearer {api_key}"}
            r = requests.get(url, headers=headers, timeout=7)
            
            if r.status_code == 200:
                self.status["gpt"] = "ok"
            else:
                self.status["gpt"] = f"fail ({r.status_code})"
                # Safe JSON parsing logic
                try:
                    error_msg = r.json().get('error', {}).get('message', 'Unknown Error')
                except:
                    error_msg = r.text[:200]
                self.status["last_error"] = error_msg
        except Exception as e:
            self.status["gpt"] = "error"
            self.status["last_error"] = str(e)[:200]

    def get_status(self):
        return self.status