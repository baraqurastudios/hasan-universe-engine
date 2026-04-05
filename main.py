import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine
from core.brain import BaraQuraBrain

# ১. কোর সিস্টেম সেটআপ
load_dotenv()
db = DBManager()
brain = BaraQuraBrain(os.getenv("GEMINI_API_KEY"))
engine = BaraQuraEngine(db, brain)

# সেশন স্টেট কনফিগারেশন (একদম বাম দিক থেকে শুরু হবে)
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state:
    st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state:
    st.session_state.system_status = "ACTIVE"
if 'login_timestamp' not in st.session_state:
    st.session_state.login_timestamp = time.time()
if 'sleep_mode' not in st.session_state:
    st.session_state.sleep_mode = False

# --- ২. সিকিউরিটি গেটওয়ে ---
def check_access():
    if st.session_state.system_status == "BLACK_HOLE":
        st.markdown("<h1 style='color:red; text-align:center;'>🌌 SYSTEM ABSORBED BY BLACK HOLE</h1>", unsafe_allow_html=True)
        st.error("🚨 HACKER ALARM: KILL SWITCH ACTIVATED.")
        if st.button("Emergency Revive"):
            st.session_state.system_status = "ACTIVE"
            st.session_state.wrong_attempts = 0
            st.rerun()
        st.stop()

    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Universe Access")
        with st.form("security_gate"):
            master_key = st.text_input("Enter Master Key", type="password")
            if st.form_submit_button("Verify Identity"):
                if master_key.strip() == "V8_UNIVERSE_GOD_2026":
                    st.session_state.authenticated = True
                    st.session_state.login_timestamp = time.time()
                    st.balloons()
                    st.rerun()
                else:
                    st.session_state.wrong_attempts += 1
                    if st.session_state.wrong_attempts >= 3:
                        st.session_state.system_status = "BLACK_HOLE"
                    st.rerun()
        st.stop()

check_access()

# --- ৩. মেইন ইন্টারফেস ---
st.set_page_config(page_title="BaraQura Master V10", layout="wide")

# ড্যাশবোর্ড ডেটা
db.cursor.execute("SELECT COUNT(*) FROM users")
total_leads = db.cursor.fetchone()[0]

# --- ৪. সাইডবার ---
with st.sidebar:
    st.title("🛡️ Command Center")
    st.success(f"Status: {st.session_state.system_status}")
    
    current_time = datetime.now().strftime("%I:%M:%S %p")
    st.markdown(f"### 🕒 {current_time}")
    
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

# --- ৫. মেইন কন্টেন্ট ---
menu = st.tabs(["🤖 AI Engine", "💻 Dev Console"])

with menu[0]:
    st.header("BaraQura Selling Machine")
    u_msg = st.text_input("Master Message", key="user_msg_input")
    if st.button("Send Message"):
        res = engine.generate_response("admin", "Master", u_msg)
        st.info(f"AI: {res}")

with menu[1]:
    st.header("Developer Tools")
    st.write("System status: Optimized")

# অটো রিফ্রেশ
time.sleep(1)
st.rerun()
