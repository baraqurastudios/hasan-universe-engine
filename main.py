import streamlit as st
import os

# ১. টাইটেল সেটআপ (যাতে ব্ল্যাক স্ক্রিন না দেখায়)
st.set_page_config(page_title="BaraQura Engine V8.2", page_icon="🛡️")

# ২. মেইন ইঞ্জিন ফাইলটি খোঁজা এবং রান করা
engine_file = "BaraQura_Engine.py"

if os.path.exists(engine_file):
    try:
        # মেইন ইঞ্জিন ফাইলের কোড রান করানো হচ্ছে
        with open(engine_file, "r", encoding="utf-8") as f:
            code = f.read()
            exec(code)
    except Exception as e:
        # ইঞ্জিন ফেইল হলে এই মেসেজ দেখাবে
        st.error(f"Engine Failure: {e}")
else:
    # ফাইল খুঁজে না পেলে এই মেসেজ দেখাবে
    st.error(f"Error: {engine_file} not found in root directory!")
