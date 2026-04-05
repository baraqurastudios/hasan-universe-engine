class BaraQuraEngine:
    def __init__(self, db_manager, brain_instance):
        self.db = db_manager
        self.brain = brain_instance
        self.base_price = 1200
        self.floor_price = 900

    def get_negotiated_price(self, user_id, ai_data):
        # Price Integrity: আগের অফার চেক করা
        previous_offer = self.db.get_offered_price(user_id)
        
        mood = ai_data.get("mood", "curious")
        buyer_type = ai_data.get("type", "unknown")
        
        calculated_price = self.base_price
        if buyer_type == "cheap": calculated_price -= 100
        if mood == "angry": calculated_price -= 150
        
        final_price = max(self.floor_price, calculated_price)
        
        # দাম বাড়লে আগের দামটাই রাখা
        if previous_offer and final_price > previous_offer:
            final_price = previous_offer
            
        self.db.save_offered_price(user_id, final_price)
        return final_price

    def generate_response(self, user_id, raw_name, message):
        # এআই প্রসেসিং
        raw_res = self.brain.get_smart_answer(message)
        ai_data, ai_text = self.brain.parse_ai_response(raw_res)
        
        price_msg = ""
        if ai_data and ai_data.get("intent") == "pricing":
            current_price = self.get_negotiated_price(user_id, ai_data)
            price_msg = f"💰 বিশেষ অফারে দাম মাত্র {current_price} টাকা।\n"
            
        return f"{price_msg}{raw_name}, {ai_text}"
