import os
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

def main():
    # ১. ডাটাবেস এবং ইঞ্জিন ইনিশিয়ালাইজ করা
    db = DBManager()
    engine = BaraQuraEngine(db)

    print("--- BaraQura V10 Sales Machine Active ---")
    print("Type 'exit' to stop the simulation.\n")

    # ২. সিমুলেশন লুপ (Local Test)
    user_id = "test_user_fb_001" # ফেসবুকে এটি হবে ইউজারের ইউনিক আইডি
    raw_name = "MD Hasan Ali"    # ফেসবুকে এটি হবে ইউজারের ফুল নেম

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'stop']:
            db.close()
            print("🛑 System Stopped.")
            break

        # ৩. ইঞ্জিন দিয়ে রেসপন্স জেনারেট করা
        response = engine.generate_response(user_id, raw_name, user_input)
        
        # ৪. আউটপুট দেখানো
        print(f"BaraQura AI: {response}")
        
        # ৫. ডাটাবেস থেকে বর্তমান অবস্থা চেক করা (সিমুলেশন ভিউ)
        status = db.get_user(user_id)
        print(f"[System Log] Current Score: {status['score']} | Status: {status['status']}\n")

if __name__ == "__main__":
    main()
