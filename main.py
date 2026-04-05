import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine
from core.brain import BaraQuraBrain

# ১. সিস্টেম সেটআপ
load_dotenv()
db = DBManager()
brain = BaraQuraBrain(os.getenv("GEMINI_API_KEY"))
engine = BaraQuraEngine(db, brain)

# সেশন স্টেট
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"
if 'login_time' not in st.session_state: st.session_state.login_time = time.time()

# ২. সিকিউরিটি গেটওয়ে (Black Hole)
if st.session_state.system_status == "BLACK_HOLE":
    st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE")
    if st.button("Emergency Revive"):
        st.session_state.system_status = "ACTIVE"
        st.session_state.wrong_attempts = 0
        st.rerun()
    st.stop()

if not st.session_state.authenticated:
    st.title("🛡️ BaraQura Universe Access")
    with st.form("gate"):
        key = st.text_input("Master Key", type="password")
        if st.form_submit_button("Verify"):
            if key == "V8_UNIVERSE_GOD_2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.session_state.wrong_attempts += 1
                if st.session_state.wrong_attempts >= 3:
                    st.session_state.system_status = "BLACK_HOLE"
                st.rerun()
    st.stop()

# ৩. ইন্টারফেস ও মনিটর
st.set_page_config(page_title="BaraQura V10", layout="wide")
with st.sidebar:
    st.title("🛡️ Command Center")
    st.markdown(f"### 🕒 {datetime.now().strftime('%I:%M %p')}")
    st.info(f"⌛ Active: {int(time.time() - st.session_state.login_time) // 60} mins")
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

# ৪. মেইন কন্টেন্ট
menu = st.tabs(["🤖 AI Sales Engine", "💻 Dev Console"])

with menu[0]:
    st.header("BaraQura Selling Machine")
    u_msg = st.text_input("Client Message", key="user_input_box")
    if st.button("Send", key="send_btn"):
        res = engine.generate_response("admin", "Master", u_msg)
        st.info(f"AI: {res}")

with menu[1]:
    st.header("Developer Tools")
    st.code("# System Optimized\n# All cores active")

time.sleep(1)
st.rerun()
