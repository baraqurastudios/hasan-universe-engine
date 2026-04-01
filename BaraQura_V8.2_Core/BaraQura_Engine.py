import streamlit as st
import json
import os

# ১. টাইটেল এবং UI সেটআপ
st.set_page_config(page_title="BaraQura Engine V8.2", page_icon="🛡️")
st.title("🛡️ BaraQura Universe Engine V8.2")
st.subheader("Black Hole Security Protocol")

# ২. কনফিগ ফাইল লোড করা
def load_config():
    try:
        # ফাইলটি ডিরেক্টরি থেকে পড়ার চেষ্টা করছে
        with open("v82_config.json", "r") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Vault Missing! Error: {e}")
        return None

config_data = load_config()

if config_data:
    # ৩. ব্রাউজারে পাসওয়ার্ড ইনপুট বক্স তৈরি
    master_key = config_data["security_layer"]["master_key_hash"]
    
    # ইউজার ইনপুট নেওয়ার বক্স
    user_input = st.text_input("Enter Master Key to Access Engine:", type="password")

    # আনলক বাটন
    if st.button("Unlock System"):
        if user_input == master_key:
            st.success("🔓 Access Granted. Welcome, Operator.")
            st.write("---")
            st.info("System Status: ONLINE")
            st.write("Master, your V8.2 Core is now fully functional.")
            # ভবিষ্যতে এখানে আরও ফিচার যোগ হবে
        else:
            st.error("⚠️ Invalid Master Key! Black Hole Mode Active.")
