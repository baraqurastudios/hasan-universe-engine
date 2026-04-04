import os
from dotenv import load_dotenv

# .env ফাইল লোড করা
load_dotenv()

class Config:
    # ফেসবুক ক্রেডেনশিয়াল
    VERIFY_TOKEN = os.getenv("FB_VERIFY_TOKEN")
    PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")
    APP_SECRET = os.getenv("FB_APP_SECRET")
    
    # টেলিগ্রাম ক্রেডেনশিয়াল
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID")
    
    # ডাটাবেস পাথ
    DB_PATH = os.path.join(os.path.dirname(__file__), "data/database.sqlite")
