import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine
from core.brain import BaraQuraBrain

# ১. পেজ কনফিগ (সবার আগে থাকতে হবে নতুবা এরর দিবে)
st.set_page_config(page_title="BaraQura V10 Master", layout="wide")

# ২. কোর সিস্টেম লোড
load_dotenv()
db = DBManager()
brain = BaraQuraBrain(os.getenv("GEMINI_API_KEY"))
engine = BaraQuraEngine(db, brain)

# ৩. সেশন স্টেট (Old + New Logic)
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"

# --- ৪. ওল্ড সিকিউরিটি: BLACK HOLE PROTOCOL ---
if st.session_state.system_status == "BLACK_HOLE":
    st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE")
    if st.button("Emergency Revive"):
        st.session_state.system_status = "ACTIVE"
        st.session_state.wrong_attempts = 0
        st.rerun()
    st.stop()

# --- ৫. ওল্ড সিকিউরিটি: লগইন গেট (Fixes 1000013713.jpg) ---
if not st.session_state.authenticated:
    st.title("🛡️ BaraQura Universe Access")
    with st.form("security_gate"):
        key = st.text_input("Enter Master Key", type="password")
        if st.form_submit_button("Verify Identity"):
            if key == "V8_UNIVERSE_GOD_2026":
                st.session_state.authenticated = True
                st.balloons()
                st.rerun()
            else:
                st.session_state.wrong_attempts += 1
                if st.session_state.wrong_attempts >= 3:
                    st.session_state.system_status = "BLACK_HOLE"
                st.error(f"Access Denied! Attempt: {st.session_state.wrong_attempts}/3")
                st.rerun()
    st.stop() # এই লাইনটিই নিশ্চিত করবে যে নিচে আর কিছু যাবে না

# --- ৬. নিউ ড্যাশবোর্ড (পাসওয়ার্ড দিলেই কেবল এগুলো দেখাবে) ---
with st.sidebar:
    st.title("🛡️ Command Center")
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

# ট্যাবগুলো এখন নিচে, তাই আগের মতো মিক্স হবে না
menu = st.tabs(["🤖 AI Sales Engine", "💻 Dev Console"])

with menu[0]:
    st.header("BaraQura Selling Machine")
    u_msg = st.text_input("Client Message", key="main_chat")
    if st.button("Send", key="send_btn"):
        res = engine.generate_response("admin", "Master", u_msg)
        st.info(f"AI: {res}")

with menu[1]:
    st.header("Developer Console")
    st.success("System optimized and ready.")
