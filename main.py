import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# .env ফাইল লোড
load_dotenv()

# --- ১. আল্ট্রা সিকিউরিটি এক্সেস লজিক (Kill Switch + Rhythm + Master Keys) ---
def check_access():
    # কিল সুইচ স্ট্যাটাস চেক
    if 'system_status' not in st.session_state:
        st.session_state.system_status = "ACTIVE"

    if st.session_state.system_status == "KILLED":
        st.error("⚠️ SYSTEM TERMINATED BY MASTER KILL SWITCH.")
        revive_key = st.text_input("Enter Secret Revive Key (Meen#8.10)", type="password")
        if revive_key == "Meen#8.10":
            st.session_state.system_status = "ACTIVE"
            st.success("Engine Revived!")
            st.rerun()
        st.stop()

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Black Hole Access")
        
        # রিদম ট্র্যাক করার স্টেট
        if 'press_times' not in st.session_state:
            st.session_state.press_times = []

        # ধাপ ১: রিদমিক ট্যাপ (মোবাইল: ৩ বার / ল্যাপটপ: ৬ বার)
        st.subheader("Step 1: Rhythmic Biometrics")
        if st.button("🔴 TAP RHYTHM HERE"):
            st.session_state.press_times.append(time.time())
            st.toast(f"Tap {len(st.session_state.press_times)} recorded")

        # ধাপ ২: মাস্টার কি ও ম্যাজিক ওয়ার্ড
        st.subheader("Step 2: Master Authorization")
        master_key = st.text_input("Master Key (Meen#8.10)", type="password")
        magic_word = st.text_input("Magic Word (Meem)")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Verify & Unlock"):
                count = len(st.session_state.press_times)
                # তোর দেওয়া সিকিউরিটি চেক
                if master_key == "Meen#8.10" and magic_word.lower() == "meem":
                    if count == 3 or count == 6:
                        st.success("Access Granted! Welcome back, Master.")
                        st.session_state.authenticated = True
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("ছন্দ মেলেনি! ট্যাপ সংখ্যা ভুল।")
                else:
                    st.error("ভুল মাস্টার কি অথবা ম্যাজিক ওয়ার্ড!")
                    st.session_state.press_times = []
        
        with col2:
            if st.button("💀 ACTIVATE KILL SWITCH"):
                st.session_state.system_status = "KILLED"
                st.rerun()
        
        st.stop()

# সিকিউরিটি এক্সেস চেক রান
check_access()

# --- ২. ইঞ্জিন ও ইন্টারফেস সেটআপ (Old Features) ---
st.set_page_config(page_title="BaraQura V10 Engine", layout="wide")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
db = DBManager()
engine = BaraQuraEngine(db, GEMINI_API_KEY)

# সাইডবার মেনু
st.sidebar.title("🛡️ BaraQura Control Panel")
menu = st.sidebar.radio("নেভিগেশন", ["চ্যাট টেস্ট", "লিড ড্যাশবোর্ড", "এআই মেমোরি রিভিউ"])

# ৩. ফিচারের কাজ (চ্যাট, ড্যাশবোর্ড, মেমোরি)
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
        st.success("রেসপন্স জেনারেট হয়েছে এবং মেমোরি আপডেট হয়েছে।")

elif menu == "লিড ড্যাশবোর্ড":
    st.header("📈 Sales Leads & Scoring")
    db.cursor.execute("SELECT * FROM users ORDER BY score DESC")
    leads = db.cursor.fetchall()
    if leads:
        st.table(leads)
    else:
        st.warning("কোনো লিড ডেটা পাওয়া যায়নি।")

elif menu == "এআই মেমোরি রিভিউ":
    st.header("🧠 AI Learning Loop")
    db.cursor.execute("SELECT id, question, answer FROM brain_memory WHERE is_verified = 0")
    pending_items = db.cursor.fetchall()
    
    if not pending_items:
        st.success("সব ভেরিফাইড!")
    
    for item in pending_items:
        with st.expander(f"Q: {item[1]}"):
            st.write(f"Proposed A: {item[2]}")
            if st.button(f"Approve ID: {item[0]}", key=f"btn_{item[0]}"):
                db.cursor.execute("UPDATE brain_memory SET is_verified = 1 WHERE id = ?", (item[0],))
                db.conn.commit()
                st.rerun()
