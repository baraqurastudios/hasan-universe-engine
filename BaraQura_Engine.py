import streamlit as st
import json
import os

# ১. টাইটেল এবং UI সেটআপ
st.set_page_config(page_title="BaraQura Engine V8.2", page_icon="🛡️")
st.title("🛡️ BaraQura Universe Engine V8.2")
st.subheader("Black Hole Security Protocol")

# ২. কনফিগ ফাইল লোড করার স্মার্ট ফাংশন
def load_config():
    # সম্ভাব্য সব পাথে ফাইলটি খোঁজা (মেইন ডিরেক্টরি এবং কোর ফোল্ডার)
    paths_to_check = ["v82_config.json", "BaraQura_V8.2_Core/v82_config.json"]
    
    for path in paths_to_check:
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    return json.load(f)
            except:
                continue
    return None

config_data = load_config()

# ৩. ভেরিফিকেশন লজিক
if config_data:
    try:
        master_key = config_data["security_layer"]["master_key_hash"]
        
        user_input = st.text_input("Enter Master Key to Access Engine:", type="password")

        if st.button("Unlock System"):
            if user_input == master_key:
                st.success("🔓 Access Granted. Welcome, Operator.")
                st.balloons() # সাকসেস সেলিব্রেশন
                st.write("---")
                st.info("System Status: ONLINE")
                st.write("Master, your V8.2 Core is now fully functional and verified.")
            else:
                st.error("⚠️ Invalid Master Key! Black Hole Mode Active.")
    except KeyError:
        st.error("Config File Error: Missing security keys inside JSON!")
else:
    st.warning("⚠️ Waiting for Vault... Please ensure 'v82_config.json' is in the main folder.")
