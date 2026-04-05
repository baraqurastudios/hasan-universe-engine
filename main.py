import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine
from core.brain import BaraQuraBrain

# ১. পেজ কনফিগ (এটি সবার উপরে থাকতে হবে)
st.set_page_config(page_title="BaraQura V10", layout="wide")

# ২. সিস্টেম লোড
load_dotenv()
db = DBManager()
brain = BaraQuraBrain(os.getenv("GEMINI_API_KEY"))
engine = BaraQuraEngine(db, brain)

# সেশন স্টেট
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"

# --- ৩. সিকিউরিটি লেয়ার (The Firewall) ---
if st.session_state.system_status == "BLACK_HOLE":
    st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE")
    if st.button("Emergency Revive"):
        st.session_state.system_status = "ACTIVE"
        st.session_state.wrong_attempts = 0
        st.rerun()
    st.stop()

# লগইন না করা পর্যন্ত নিচের কোড রান হবে না
if not st.session_state.authenticated:
    st.title("🛡️ BaraQura Master Access")
    # কন্টেইনার ব্যবহার করছি যাতে UI ক্লিন থাকে
    with st.container():
        with st.form("security_gate"):
            key = st.text_input("Master Key", type="password")
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
    st.stop() # পাসওয়ার্ড না দিলে এই লাইনের নিচে কোড যাবে না (Solved Mix-up)

# --- ৪. মেইন ড্যাশবোর্ড (পাসওয়ার্ড দিলেই কেবল এখানে আসবে) ---
with st.sidebar:
    st.title("🛡️ Command Center")
    st.success("Status: ACTIVE")
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

menu = st.tabs(["🤖 AI Sales Engine", "💻 Dev Console"])

with menu[0]:
    st.header("BaraQura Selling Machine")
    u_msg = st.text_input("Client Message", key="main_chat_input")
    if st.button("Send", key="main_send_btn"):
        if u_msg:
            res = engine.generate_response("admin", "Master", u_msg)
            st.info(f"AI: {res}")
        else:
            st.warning("Please type a message!")

with menu[1]:
    st.header("Developer Tools")
    st.code("# System: Connected\n# Engine: V10\n# All Cores: Stable")

time.sleep(1)
st.rerun()
