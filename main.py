import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. কোর সেটআপ
load_dotenv()
db = DBManager()

# সেশন স্টেট (Strict Security)
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"
if 'start_time' not in st.session_state: st.session_state.start_time = time.time()

# --- ২. সিকিউরিটি গেটওয়ে (One Key - 3 Life) ---
def check_access():
    # ক. ব্ল্যাক হোল কন্ডিশন
    if st.session_state.system_status == "BLACK_HOLE":
        st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE.")
        st.markdown("<h1 style='color:red; text-align:center;'>🚨 ACCESS REVOKED 🚨</h1>", unsafe_allow_html=True)
        # রিকভারি অপশন
        with st.expander("Emergency Recovery"):
            revive_key = st.text_input("Enter Magic Code", type="password")
            if st.button("Revive System"):
                if revive_key == "V8_UNIVERSE_GOD_2026":
                    st.session_state.system_status = "ACTIVE"
                    st.session_state.wrong_attempts = 0
                    st.rerun()
        st.stop()

    # খ. মাস্টার কি ভেরিফিকেশন
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Universe Access")
        
        # ভুল চেষ্টার ওয়ার্নিং
        lives_left = 3 - st.session_state.wrong_attempts
        if st.session_state.wrong_attempts > 0:
            st.warning(f"⚠️ Warning: {lives_left} attempts remaining before Black Hole!")

        with st.form("master_gate"):
            # শুধু একটি লং মাস্টার কি
            master_key = st.text_input("Enter Long Master Key", type="password")
            submitted = st.form_submit_button("Verify Identity")

            if submitted:
                # সঠিক কি চেক (Long Master Key)
                if master_key.strip() == "V8_UNIVERSE_GOD_2026":
                    st.session_state.authenticated = True
                    st.balloons()
                    st.rerun()
                else:
                    st.session_state.wrong_attempts += 1
                    # ৩ বার ভুলের পর ৪ নম্বর বারে ব্ল্যাক হোল
                    if st.session_state.wrong_attempts >= 3:
                        st.session_state.system_status = "BLACK_HOLE"
                    st.error("Invalid Key!")
                    st.rerun()
        st.stop()

check_access()

# --- ৩. মেইন ড্যাশবোর্ড (Old + New Combined) ---
st.set_page_config(page_title="BaraQura Master", layout="wide")
engine = BaraQuraEngine(db, os.getenv("GEMINI_API_KEY"))

# ড্যাশবোর্ড ডেটা
elapsed = int(time.time() - st.session_state.start_time)
mins, secs = divmod(elapsed, 60)
db.cursor.execute("SELECT COUNT(*) FROM users")
lead_count = db.cursor.fetchone()[0]

# সাইডবার
st.sidebar.title("🛡️ Command Center")
st.sidebar.success("Status: SECURE")
st.sidebar.metric("Active Time", f"{mins}m {secs}s")
st.sidebar.metric("Leads Collected", lead_count)

if st.sidebar.button("Logout"):
    st.session_state.authenticated = False
    st.session_state.wrong_attempts = 0
    st.rerun()

# অ্যাপ কন্টেন্ট
st.header("Welcome, Master.")
menu = st.sidebar.radio("Menu", ["🤖 AI Engine", "📊 Leads"])

if menu == "🤖 AI Engine":
    msg = st.text_input("Test AI Message")
    if st.button("Execute"):
        res = engine.generate_response("admin", "Master", msg)
        st.info(f"AI: {res}")
