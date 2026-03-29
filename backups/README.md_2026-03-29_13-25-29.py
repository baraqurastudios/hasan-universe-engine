import sys

def auto_kill_monitor(violation_score):
    """
    যদি এআই-এর 'ভায়োলেশন স্কোর' ১০০ ছাড়িয়ে যায়, 
    তবে সিস্টেম অটোমেটিক শাটডাউন হবে।
    """
    THRESHOLD = 100
    if violation_score >= THRESHOLD:
        print("🚨 CRITICAL VIOLATION! AUTO-KILL ACTIVATED.")
        sys.exit(1) # ১ সেকেন্ডের মধ্যে সব প্রসেস ধ্বংস

# ব্যবহারের উদাহরণ:
# if ai_behavior == "dangerous":
#     auto_kill_monitor(101)