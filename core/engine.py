import re
import random

class BaraQuraEngine:
    def __init__(self, db_manager):
        self.db = db_manager
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

    # ১. নাম ফরম্যাটিং (তোর নতুন রিকোয়ারমেন্ট অনুযায়ী ২টা ওয়ার্ড নেবে)
    def format_name(self, full_name):
        if not full_name: return "বন্ধু"
        
        # নামকে স্পেস দিয়ে ভাগ করা
        parts = full_name.strip().split()
        
        if len(parts) >= 2:
            # প্রথম দুইটা অংশ নিয়ে বড় হাতের অক্ষরে সাজানো (e.g., Md. Shakibul)
            name_to_call = f"{parts[0].capitalize()} {parts[1].capitalize()}"
        else:
            # যদি নাম ১ শব্দের হয়
            name_to_call = parts[0].capitalize()
            
        return name_to_call

    # ২. স্মার্ট ইনটেন্ট ডিটেকশন (অপরিবর্তিত)
    def detect_intent(self, msg):
        msg = msg.lower()
        if any(x in msg for x in self.order_keywords): return "pricing"
        if any(x in msg for x in ["কিনব", "অর্ডার", "buy"]): return "buy_intent"
        if any(x in msg for x in self.greetings): return "greeting"
        return "unknown"

    # ৩. ফোন নম্বর ডিটেকশন (অপরিবর্তিত)
    def extract_phone(self, msg):
        phone_pattern = r'(?:\+88|88)?(01[3-9]\d{8})'
        match = re.search(phone_pattern, msg)
        return match.group(0) if match else None

    # ৪. মেইন রেসপন্স জেনারেটর (The Nucleus)
    def generate_response(self, user_id, raw_name, user_message):
        msg = user_message.lower()
        # এখানে এখন থেকে "Md. Shakibul" ফরম্যাটে নাম যাবে
        user_name = self.format_name(raw_name)
        
        user_data = self.db.get_user(user_id) 
        current_score = user_data['score'] if user_data else 0

        phone = self.extract_phone(msg)
        if phone:
            self.db.save_lead(user_id, raw_name, phone)
            return f"🔥 ধন্যবাদ {user_name}! আপনার নম্বর ({phone}) পেয়েছি। আমাদের সেলস টিম দ্রুত কল দিবে।"

        intent = self.detect_intent(msg)
        score_to_add = self.intent_scores.get(intent, 0)
        new_score = current_score + score_to_add
        
        stage = "Cold"
        if new_score >= 30: stage = "Warm"
        if new_score >= 80: stage = "Hot"
        
        self.db.update_user_score(user_id, new_score, stage)

        if intent == "greeting":
            return f"হ্যালো {user_name}! 😊 BaraQura AI-তে স্বাগতম। আপনি কি আমাদের প্রোডাক্টের প্রাইস বা অফার সম্পর্কে জানতে চান?"

        if intent == "pricing":
            return f"💰 {user_name}, আপনি সঠিক জিনিস পছন্দ করেছেন! বিস্তারিত প্রাইস লিস্ট এবং আজকের ডিসকাউন্ট পেতে আপনার ফোন নম্বরটি দিন।"

        if stage == "Warm":
            return f"{user_name}, আপনি কি অর্ডারটি কনফার্ম করতে চান? নম্বর দিলে আমরা প্রসেস শুরু করতে পারি।"

        return f"ধন্যবাদ {user_name}। আমি আপনার কথাটি ঠিক বুঝতে পারিনি। আপনি কি অর্ডার বা দাম সম্পর্কে জানতে চাচ্ছেন?"
