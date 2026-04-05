import re
from core.brain import BaraQuraBrain

class BaraQuraEngine:
    def __init__(self, db_manager, api_key):
        self.db = db_manager
        # ১. জেমিনি ব্রেন সেটআপ (নতুন)
        self.brain = BaraQuraBrain(api_key, db_manager)
        
        # তোর পুরাতন কি-ওয়ার্ড লিস্ট
        self.greetings = ['hi', 'hello', 'hey', 'সালাম', 'আদাব', 'কেউ আছেন']
        self.order_keywords = ['দাম', 'প্রাইস', 'price', 'কত', 'order', 'অর্ডার', 'কিনতে চাই']
        
        # তোর সেই বিখ্যাত Sales Scoring Logic
        self.intent_scores = {
            "greeting": 5,
            "pricing": 20,
            "buy_intent": 50,
            "phone_shared": 100
        }

    # নাম ফরম্যাটিং (তোর ২-ওয়ার্ড রিকোয়ারমেন্ট)
    def format_name(self, full_name):
        if not full_name: return "বন্ধু"
        parts = full_name.strip().split()
        if len(parts) >= 2:
            return f"{parts[0].capitalize()} {parts[1].capitalize()}"
        return parts[0].capitalize()

    # স্মার্ট ইনটেন্ট ডিটেকশন (Level 1)
    def detect_intent(self, msg):
        msg = msg.lower()
        if any(x in msg for x in self.order_keywords): return "pricing"
        if any(x in msg for x in ["কিনব", "অর্ডার", "buy"]): return "buy_intent"
        if any(x in msg for x in self.greetings): return "greeting"
        return "unknown"

    # ফোন নম্বর ডিটেকশন
    def extract_phone(self, msg):
        phone_pattern = r'(?:\+88|88)?(01[3-9]\d{8})'
        match = re.search(phone_pattern, msg)
        return match.group(0) if match else None

    # মেইন রেসপন্স জেনারেটর (The Nucleus)
    def generate_response(self, user_id, raw_name, user_message):
        msg = user_message.lower()
        user_name = self.format_name(raw_name)
        
        # ডাটাবেস থেকে ইউজার ডাটা চেক
        user_data = self.db.get_user(user_id)
        current_score = user_data.get('score', 0)
        
        # ফোন নম্বর ডিটেক্ট হলে সরাসরি Hot Lead
        phone = self.extract_phone(msg)
        if phone:
            self.db.save_lead(user_id, raw_name, phone)
            return f"🔥 ধন্যবাদ {user_name}! আপনার নম্বর ({phone}) পেয়েছি। আমাদের সেলস টিম দ্রুত কল দিবে।"

        # --- ইনটেন্ট এবং স্কোরিং লজিক ---
        intent = self.detect_intent(msg)
        score_to_add = self.intent_scores.get(intent, 0)
        new_score = current_score + score_to_add
        
        # স্টেজ নির্ধারণ
        stage = "Cold"
        if new_score >= 80: stage = "Hot"
        elif new_score >= 30: stage = "Warm"
        
        # ডাটাবেস স্কোর আপডেট
        self.db.update_user_score(user_id, new_score, stage, intent)

        # --- ৫. ৩-লেভেল স্মার্ট রিপ্লাই লজিক ---

        # Level 1: লোকাল রিপ্লাই (তোর সেট করা নির্দিষ্ট উত্তর)
        if intent == "greeting":
            return f"হ্যালো {user_name}! 😊 BaraQura AI-তে স্বাগতম। আপনি কি আমাদের প্রোডাক্টের প্রাইস বা অফার সম্পর্কে জানতে চান?"
        
        if intent == "pricing":
            return f"💰 {user_name}, আপনি সঠিক জিনিস পছন্দ করেছেন! বিস্তারিত প্রাইস লিস্ট পেতে আপনার ফোন নম্বরটি দিন।"

        # Level 2: ভেরিফাইড মেমোরি চেক (আগে যা শিখিয়েছিস)
        verified_ans = self.db.get_verified_answer(user_message)
        if verified_ans:
            return verified_ans

        # Level 3: জেমিনি এআই ব্রেন (শিখবে এবং উত্তর দিবে)
        ai_response = self.brain.get_smart_answer(user_message)
        
        # যদি এআই রিপ্লাই দেয়, নামটা যুক্ত করে দেওয়া (পার্সোনালাইজেশন)
        return f"{user_name}, {ai_response}"
