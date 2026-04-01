import streamlit as st
import json
import os

# ১. সেশন স্টেট চেক (লগইন স্ট্যাটাস ধরে রাখার জন্য)
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ২. কনফিগ ফাইল লোড করার ফাংশন
def load_config():
    config_file = "v82_config.json"
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                return json.load(f)
        except:
            return None
    return None

# ৩. মূল লজিক শুরু
if st.session_state["authenticated"]:
    # --- এখানে আপনার অ্যাপের মেইন ড্যাশবোর্ড ---
    st.title("🛡️ BaraQura Universe Dashboard")
    st.success("Welcome, Master. System is fully ONLINE.")
    
    st.sidebar.title("Engine Controls")
    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

    st.write("---")
    st.info("আপনার ইঞ্জিনের মূল মডিউলগুলো এখানে যোগ করা যাবে।")
    # আপনি আপনার অ্যাপের বাকি ফিচারগুলো এখানে যুক্ত করতে পারেন।

else:
    # --- এখানে পাসওয়ার্ড প্রোটেকশন লেয়ার ---
    st.title("🛡️ BaraQura Universe Engine V8.2")
    st.subheader("Black Hole Security Protocol")

    config_data = load_config()

    if config_data:
        try:
            master_key = config_data["security_layer"]["master_key_hash"]
            
            user_input = st.text_input("Enter Master Key to Access Engine:", type="password")

            if st.button("Unlock System"):
                if user_input == master_key:
                    st.session_state["authenticated"] = True
                    st.balloons()
                    st.rerun()  # এটি সরাসরি ড্যাশবোর্ডে নিয়ে যাবে
                else:
                    st.error("⚠️ Invalid Master Key! Access Denied.")
        except Exception as e:
            st.error(f"Config Structure Error: {e}")
    else:
        st.warning("⚠️ 'v82_config.json' ফাইলটি খুঁজে পাওয়া যাচ্ছে না। অনুগ্রহ করে চেক করুন।")
