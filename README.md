import os

def final_v8_check():
    # সাইডবার থেকে ইনপুট চেক
    user_input = os.getenv("GITHUB_ACCESS_TOKEN")
    
    # এটি কোনো নেটওয়ার্ক ছাড়াই আপনার লোকাল ফাইল চেক করবে
    if user_input == "FIRE":
        print("🔥 Emergency Lock Engaged Locally.")
        # আপনার সব ফাইল সাথে সাথে .vault হয়ে যাবে
        os.rename("v81_engine.py", ".v81_engine.py.vault")
        return "System Sealed."

if __name__ == "__main__":
    final_v8_check()
