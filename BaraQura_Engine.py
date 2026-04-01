import streamlit as st
import json
import os

# ১. টাইটেল এবং UI সেটআপ
st.set_page_config(page_title="BaraQura Engine V8.2", page_icon="🛡️")
st.title("🛡️ BaraQura Universe Engine V8.2")
st.subheader("Black Hole Security Protocol")

# ২. কনফিগ ফাইল লোড করার স্মার্ট ফাংশন
def load_config():
    # ফাইলটি যেখানেই থাকুক খুঁজে বের করার চেষ্টা
    config_file = "v82_config.json"
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                return json.load(f)
        except:
            return None
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
                st.balloons()
                st.write("---")
                st.info("System Status: ONLINE")
                st.write("Master, your V8.2 Core is now fully functional.")
            else:
                st.error("⚠️ Invalid Master Key! Black Hole Mode Active.")
    except Exception as e:
        st.error(f"Config Structure Error: {e}")
else:
    st.warning("⚠️ Waiting for Vault... Please ensure 'v82_config.json' is present.")
