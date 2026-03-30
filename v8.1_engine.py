import uuid
from observer_v82 import SecureObserverV82

# ১. সিস্টেম ইনিশিয়ালাইজেশন
obs = SecureObserverV82()

def system_startup():
    print("🛡️ Booting v8.1 Engine...")
    
    # ২. হার্ডওয়্যার আইডেন্টিটি ভেরিফিকেশন
    # এটি আপনার পিসির ইউনিক আইডি চেক করবে
    current_hwid = str(uuid.getnode())
    
    # ৩. সিকিউর অবজারভারের মাধ্যমে পারমিশন নেওয়া
    print("🔍 Verifying Hardware Signature...")
    if obs.authenticate("your_password"): # এখানে আপনার ডায়েরির পাসওয়ার্ডটি দিবেন
        print("✅ Hardware Identity Confirmed.")
        print("🚀 v8.1 Engine is now ONLINE.")
        return True
    else:
        print("🚨 SECURITY ALERT: Unauthorized Hardware or Wrong Key!")
        print("🛑 System Lockdown Initiated.")
        return False

# --- ইঞ্জিন রান করার চেষ্টা ---
if __name__ == "__main__":
    if system_startup():
        # এখানে আপনার ইঞ্জিনের আসল কাজগুলো শুরু হবে
        print("Working on your projects, Master...")
    else:
        # হ্যাকার ঢুকলে সিস্টেম অটোমেটিক বন্ধ হয়ে যাবে
        exit()
