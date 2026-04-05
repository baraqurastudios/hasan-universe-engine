class BaraQuraEngine:
    def __init__(self, db_manager, brain_instance):
        self.db = db_manager
        self.brain = brain_instance
        self.base_price = 1200

    def generate_response(self, user_id, raw_name, message):
        raw_res = self.brain.get_smart_answer(message)
        ai_data, ai_text = self.brain.parse_ai_response(raw_res)
        
        price_msg = ""
        if ai_data and ai_data.get("intent") == "pricing":
            # ডাটাবেজ থেকে দাম চেক করার লজিক এখানে আসবে
            price_msg = f"💰 আমাদের বর্তমান অফার {self.base_price} টাকা।\n"
            
        return f"{price_msg}{raw_name}, {ai_text}"
