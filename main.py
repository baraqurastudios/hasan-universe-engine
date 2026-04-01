import streamlit as st
import os
import sys

# ১. টাইটেল সেটআপ (BaraQura Engine V8.2 UI)
st.set_page_config(page_title="BaraQura Engine V8.2", page_icon="🛡️", layout="wide")

# ২. সিস্টেম পাথ সেটআপ (যাতে পাইথন ফোল্ডারের ভেতরের ফাইলগুলো খুঁজে পায়)
# এই অংশটি আপনার নতুন তৈরি করা ৫টি ফোল্ডারকে পাইথনের সাথে কানেক্ট করবে
folders = ['security', 'core', 'database', 'interface', 'config']
for folder in folders:
    folder_path = os.path.join(os.getcwd(), folder)
    if folder_path not in sys.path:
        sys.path.append(folder_path)

# ৩. মেইন ইঞ্জিন ফাইল রান করার লজিক
engine_file = "BaraQura_Engine.py"

st.title("🛡️ BaraQura Engine V8.2")
st.info("System initializing with organized directory structure...")

if os.path.exists(engine_file):
    try:
        # মেইন ইঞ্জিন ফাইলের কোড রান করানো হচ্ছে
        with open(engine_file, "r", encoding="utf-8") as f:
            code = f.read()
            # ফোল্ডার পাথে ফাইলগুলো যুক্ত থাকায় এখন exec(code) দিলে ভেতরের ফাইলগুলোও কাজ করবে
            exec(code)
    except Exception as e:
        # ইঞ্জিন ফেইল হলে এই মেসেজ দেখাবে
        st.error(f"❌ Engine Failure: {e}")
        st.warning("পরামর্শ: নিশ্চিত করুন যে সব ফাইল সঠিক ফোল্ডারে আছে এবং কোনো ইমপোর্ট এরর নেই।")
else:
    # ফাইল খুঁজে না পেলে এই মেসেজ দেখাবে
    st.error(f"❌ Error: {engine_file} not found in root directory!")
