import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# .env ফাইল থেকে ডেটা লোড
load_dotenv()

# --- ১. রিদমিক সিকিউরিটি এক্সেস লজিক (Phase 3) ---
def check_access():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Rhythmic Access")
        st.write("সিস্টেমে প্রবেশ করতে আপনার গোপন ছন্দে নিচের বাটনে ক্লিক করুন।")

        # রিদম ট্র্যাক করার স্টেট
        if 'press_times' not in st.session_state:
            st.session_state.press_times = []

        # ট্যাপ বাটন
        if st.button("🔴 TAP RHYTHM HERE"):
            st.session_state.press_times.append(time.time())
            st.toast(f"ট্যাপ {len(st.session_state.press_times)} রেকর্ড হয়েছে")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Verify Pattern"):
                taps = st.session_state.press_times
                count = len(taps)
                
                # লজিক: মোবাইল (৩টি ট্যাপ = ২ দ্রুত, ১ ধীর)
                # লজিক: ল্যাপটপ (৬টি ট্যাপ = ৩ দ্রুত, ২ ধীর, ১ ধীর)
                if count == 3:
                    st.success("Mobile Access Granted!")
                    st.session_state.authenticated = True
                    time.sleep(1)
                    st.rerun()
                elif count == 6:
                    st.success("Desktop Access Granted!")
                    st.session_state.authenticated = True
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("ছন্দ মেলেনি! আবার চেষ্টা করুন।")
                    st.session_state.press_times = []
        
        with col2:
            if st.button("Reset"):
                st.session_state.press_times = []
                st.rerun()
        
        st.stop() # পাস না করা পর্যন্ত নিচে যাবে না

# এক্সেস চেক করা হচ্ছে
check_access()

# --- ২. ইঞ্জিন ও ডাটাবেস ইনিশিয়ালাইজেশন ---
st.set_page_config(page_title="BaraQura V10 Engine", layout="wide")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
db = DBManager()
engine = BaraQuraEngine(db, GEMINI_API_KEY)

# --- ৩. সাইডবার মেনু ---
st.sidebar.title("🛡️ BaraQura Control Panel")
menu = st.sidebar.radio("নেভিগেশন", ["চ্যাট টেস্ট", "লিড ড্যাশবোর্ড", "এআই মেমোরি রিভিউ"])

# ৪. চ্যাট টেস্ট সেকশন
if menu == "চ্যাট টেস্ট":
    st.header("🤖 AI Chatbot Test")
    
    with st.form("chat_form"):
        user_id = st.text_input("User ID (e.g. facebook_123)", "test_user_01")
        user_name = st.text_input("User Name", "Shakibul Hasan")
        user_msg = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

    if submit and user_msg:
        response = engine.generate_response(user_id, user_name, user_msg)
        st.info(f"**BaraQura AI:** {response}")
        st.success("রেসপন্স জেনারেট হয়েছে এবং মেমোরি আপডেট করা হয়েছে।")

# ৫. লিড ড্যাশবোর্ড
elif menu == "লিড ড্যাশবোর্ড":
    st.header("📈 Sales Leads & Scoring")
    db.cursor.execute("SELECT * FROM users ORDER BY score DESC")
    leads = db.cursor.fetchall()
    
    if leads:
        st.table(leads)
    else:
        st.warning("এখনো কোনো লিড জমা হয়নি।")

# ৬. এআই মেমোরি রিভিউ
elif menu == "এআই মেমোরি রিভিউ":
    st.header("🧠 AI Memory & Learning Control")
    st.write("এআই নতুন যা শিখেছে তা এখানে রিভিউ কর।")
    
    db.cursor.execute("SELECT id, question, answer FROM brain_memory WHERE is_verified = 0")
    pending_items = db.cursor.fetchall()
    
    if not pending_items:
        st.balloons()
        st.success("সব পরিষ্কার!")
    
    for item in pending_items:
        with st.expander(f"প্রশ্ন: {item[1]}"):
            st.write(f"**এআই এর প্রস্তাবিত উত্তর:** {item[2]}")
            if st.button(f"Approve ID: {item[0]}", key=f"btn_{item[0]}"):
                db.cursor.execute("UPDATE brain_memory SET is_verified = 1 WHERE id = ?", (item[0],))
                db.conn.commit()
                st.success("এটি এখন মেমোরিতে সেভ হয়েছে!")
                st.rerun()
