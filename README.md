# ==============================
# TELEGRAM CONTROL MODULE
# ==============================
import requests

class TelegramControl:
    TOKEN = "আপনার_বট_টোকেন_এখানে_দিন"
    URL = f"https://api.telegram.org/bot{TOKEN}/"

    @staticmethod
    def send_to_owner(message):
        """মালিকের কাছে এপ্রুভাল বা মেসেজ পাঠানো"""
        chat_id = "আপনার_চ্যাট_আইডি"
        payload = {"chat_id": chat_id, "text": message}
        requests.post(TelegramControl.URL + "sendMessage", data=payload)

# উদাহরণ: এআই স্ক্রিপ্ট তৈরি করলে তা সরাসরি টেলিগ্রামে চলে যাবে
def on_script_generated(script):
    message = f"🚀 নতুন স্ক্রিপ্ট রেডি!\nটপিক: {script['title']}\n\nএপ্রুভ করতে /approve লিখুন।"
    TelegramControl.send_to_owner(message)
