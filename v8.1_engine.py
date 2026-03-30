from observer_v82 import RecursiveObserver # ১. অবজারভারকে ডেকে আনা
obs = RecursiveObserver()                 # ২. অবজারভারকে সক্রিয় করা

# ৩. ইঞ্জিনের কাজের আগে চেক করা (উদাহরণ)
if obs.observe_action("Core Update", "v8.1 Logic") == "SUCCESS":
    print("🚀 Engine is safe to run.")
  
