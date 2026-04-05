import google.generativeai as genai
from datetime import datetime

class BaraQuraBrain:
    def __init__(self, api_key, db_manager):
        # জেমিনি কনফিগারেশন
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.db = db_manager

    def get_smart_answer(self, user_msg):
        # ১. আগে ভেরিফাইড মেমোরি চেক কর (Level 2: Memory)
        self.db.cursor.execute("SELECT answer FROM brain_memory WHERE question = ? AND is_verified = 1", (user_msg,))
        row = self.db.cursor.fetchone()
        if row:
            return row[0] # সরাসরি নিজের মেমোরি থেকে উত্তর দিল

        # ২. না পেলে জেমিনির কাছে যাও (Level 3: LLM)
        try:
            # এআই-কে তোর সিস্টেমের রোল বুঝিয়ে দেওয়া
            prompt = f"You are the BaraQura Sales AI. Answer briefly in Bengali: {user_msg}"
            response = self.model.generate_content(prompt)
            ai_ans = response.text

            # ৩. নতুন তথ্য পেন্ডিং হিসেবে সেভ করা (Self-Learning Loop)
            self.learn_new_info(user_msg, ai_ans)
            return ai_ans
        except Exception as e:
            return "আমি বিষয়টি নিয়ে ভাবছি, কিছুক্ষণ পর আবার বলবেন কি?"

    def learn_new_info(self, q, a):
        """নতুন প্রশ্ন ও উত্তর ডাটাবেসে সেভ করা (অ্যাপ্রুভালের জন্য)"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            self.db.cursor.execute(
                "INSERT OR IGNORE INTO brain_memory (question, answer, created_at) VALUES (?, ?, ?)",
                (q, a, now)
            )
            self.db.conn.commit()
        except:
            pass
