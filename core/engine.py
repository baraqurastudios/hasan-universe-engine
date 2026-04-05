import random
import re

class BaraQuraEngine:
    def __init__(self, db_manager, brain_instance):
        self.db = db_manager
        self.brain = brain_instance
        self.base_price = 1200
        self.floor_price = 900 # এর নিচে দাম নামবে না

    def format_name(self, name):
        parts = (name or "বন্ধু").strip().split()
        return f"{parts[0].capitalize()} {parts[1].capitalize()}" if len(parts) >= 2 else parts[0].capitalize()

    def get_negotiated_price(self, user_id, ai_data):
        # ১. আগে অফার করা দাম চেক করা (Price Integrity)
        previous_offer = self.db.get_offered_price(user_id)
        
        mood = ai_data.get("mood", "curious")
        intent = ai_data.get("intent", "unknown")
        buyer_type = ai_data.get("type", "unknown")
        
        # ২. বার্টার লজিক (The Negotiation Matrix)
        calculated_price = self.base_price
        
        if buyer_type == "cheap":
            calculated_price -= 100
        
        if mood == "angry":
            calculated_price -= 150
        elif intent == "objection":
            calculated_price -= 50

        # ৩. ফ্লোর প্রাইস চেক
        final_price = max(self.floor_price, calculated_price)
        
        # ৪. ইন্টিগ্রিটি চেক: আগের চেয়ে বেশি দাম বলা যাবে না
        if previous_offer and final_price > previous_offer:
            final_price = previous_offer
        
        # ৫. ডাটাবেজে নতুন অফার সেভ করা
        self.db.save_offered_price(user_id, final_price)
        return final_price

    def generate_response(self, user_id, raw_name, message):
        user_name = self.format_name(raw_name)
        
        # ১. এআই থেকে জেসন ও রেসপন্স আনা
        raw_res = self.brain.get_smart_answer(message)
        ai_data, ai_text = self.brain.parse_ai_response(raw_res)
        
        if not ai_data:
            return f"{user_name}, {ai_text}"

        # ২. ডাইনামিক প্রাইসিং ও নেগোসিয়েশন
        current_price = self.get_negotiated_price(user_id, ai_data)
        
        # ৩. স্কোর ও স্টেজ আপডেট
        score_map = {"greeting": 5, "pricing": 25, "buy": 60, "objection": 10}
        points = score_map.get(ai_data.get("intent"), 0)
        self.db.update_score(user_id, points)

        # ৪. ফাইনাল রেসপন্স বিল্ড (Pricing + AI Text)
        price_msg = ""
        if ai_data.get("intent") == "pricing":
            price_msg = f"💰 বিশেষ অফারে এটার দাম মাত্র {current_price} টাকা।\n"
        
        return f"{price_msg}{user_name}, {ai_text}"
