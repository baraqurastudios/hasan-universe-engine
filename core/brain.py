import google.generativeai as genai
import json
import re

class BaraQuraBrain:
    def __init__(self, api_key):
        # এপিআই কী কনফিগারেশন
        genai.configure(api_key=api_key)
        
        # ৪০৪ এরর ফিক্স করতে 'models/' প্রিফিক্স যোগ করা হয়েছে
        try:
            self.model = genai.GenerativeModel('models/gemini-1.5-flash')
        except Exception:
            # ব্যাকআপ হিসেবে জেমিনি প্রো রাখা হলো
            self.model = genai.GenerativeModel('gemini-pro')
        
        self.system_instruction = """
        Role: তুমি BaraQura-এর Elite Sales Consultant। 
        Rules: 
        1. সর্বোচ্চ ২-৩ লাইন। 
        2. ১টি প্রশ্ন। 
        3. উত্তরের শুরুতে অবশ্যই নিচের JSON দিবে:
        {"type": "cheap/smart", "mood": "curious/angry", "intent": "pricing/buy", "stage": "cold/hot"}
        """

    def get_smart_answer(self, user_message):
        try:
            full_prompt = f"{self.system_instruction}\n\nUser Says: {user_message}"
            response = self.model.generate_content(full_prompt)
            # যদি রেসপন্স খালি থাকে তবে এরর হ্যান্ডেল করবে
            if not response.text:
                return "Error: Empty response from AI."
            return response.text
        except Exception as e:
            # এখানে তোর স্ক্রিনশটে দেখা যাওয়া এররগুলো ধরা পড়বে
            return f"Error: {str(e)}"

    def parse_ai_response(self, raw_response):
        # রেসপন্স থেকে JSON অংশটুকু আলাদা করা
        json_match = re.search(r'\{.*?\}', raw_response, re.DOTALL)
        if json_match:
            try:
                json_data = json.loads(json_match.group(0))
                # টেক্সট থেকে JSON এবং কোড ব্লক পরিষ্কার করা
                clean_text = raw_response.replace(json_match.group(0), "").strip()
                clean_text = clean_text.replace("```json", "").replace("```", "").strip()
                return json_data, clean_text
            except:
                return None, raw_response
        return None, raw_response
