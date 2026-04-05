import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# .env ফাইল লোড
load_dotenv()

# --- ১. আল্ট্রা সিকিউরিটি এক্সেস লজিক (Phase 3.2) ---
def check_access():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Black Hole Access")
        
        # রিদম ট্র্যাক করার স্টেট
        if 'press_times' not in st.session_state:
            st.session_state.press_times = []

        # ধাপ ১: রিদমিক ট্যাপ
        st.subheader("Step 1: Rhythmic Biometrics")
        if st.button("🔴 TAP RHYTHM HERE"):
            st.session_state.press_times.append(time.time())
            st.toast(f"Tap {len(st.session_state.press_times)} recorded")

        # ধাপ ২: মাস্টার কি ও ম্যাজিক ওয়ার্ড
        st.subheader("Step 2: Master Authorization")
        master_key = st.text_input("Master Key (Secret)", type="password")
        magic_word = st.text_input("Magic Word")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Verify & Unlock"):
                count = len(st.session_state.press_times)
                # তোর দেওয়া মাস্টার কি এবং ম্যাজিক ওয়ার্ড চেক
                if master_key == "Meen#8.10" and magic_word.lower() == "meem":
                    # রিদম চেক (মোবাইল: ৩ ট্যাপ, ল্যাপটপ: ৬ ট্যাপ)
                    if count == 3 or count == 6:
                        st.success("Access Granted! Welcome back.")
                        st.session_state.authenticated = True
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("ছন্দ মেলেনি! ট্যাপ সংখ্যা চেক করুন।")
                else:
                    st.error("ভুল মাস্টার কি অথবা ম্যাজিক ওয়ার্ড!")
                    st.session_state.press_times = []
        
        with col2:
            if st.button("Reset All"):
                st.session_state.press_times = []
                st.rerun()
        
        st.stop()

# এক্সেস চেক করা হচ্ছে
check_access()

# --- ২. ইঞ্জিন ও ইন্টারফেস (তোর আগের কোড) ---
st.set_page_config(page_title="BaraQura V10 Engine", layout="wide")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
db = DBManager()
engine = BaraQuraEngine(db, GEMINI_API_KEY)

# সাইডবার এবং বাকি কোড তোর আগের মতোই থাকবে...
st.sidebar.title("🛡️ BaraQura Control Panel")
menu = st.sidebar.radio("নেভিগেশন", ["চ্যাট টেস্ট", "লিড ড্যাশবোর্ড", "এআই মেমোরি রিভিউ"])

if menu == "চ্যাট টেস্ট":
    st.header("🤖 AI Chatbot Test")
    with st.form("chat_form"):
        user_id = st.text_input("User ID", "test_user_01")
        user_name = st.text_input("User Name", "Shakibul Hasan")
        user_msg = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

    if submit and user_msg:
        response = engine.generate_response(user_id, user_name, user_msg)
        st.info(f"**BaraQura AI:** {response}")
# (বাকি কোড আগের মতো)
