import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine
from core.brain import BaraQuraBrain

# ১. পেজ কনফিগ সবার আগে (যাতে এরর না দেয়)
st.set_page_config(page_title="BaraQura Master V10", layout="wide")

# ২. কোর সিস্টেম লোড
load_dotenv()
db = DBManager()
brain = BaraQuraBrain(os.getenv("GEMINI_API_KEY"))
engine = BaraQuraEngine(db, brain)

# ৩. সেশন স্টেট ইনিশিয়ালাইজ
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"

# --- ৪. সিকিউরিটি গেটওয়ে (The Firewall) ---
if st.session_state.system_status == "BLACK_HOLE":
    st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE")
    if st.button("Emergency Revive"):
        st.session_state.system_status = "ACTIVE"
        st.session_state.wrong_attempts = 0
        st.rerun()
    st.stop()

# যদি ইউজার লগইন না করে থাকে, তবে শুধু লগইন ফর্ম দেখাও
if not st.session_state.authenticated:
    st.title("🛡️ BaraQura Universe Access")
    with st.form("security_gate"):
        master_key = st.text_input("Enter Master Key", type="password")
        if st.form_submit_button("Verify Identity"):
            if master_key.strip() == "V8_UNIVERSE_GOD_2026":
                st.session_state.authenticated = True
                st.balloons()
                st.rerun()
            else:
                st.session_state.wrong_attempts += 1
                if st.session_state.wrong_attempts >= 3:
                    st.session_state.system_status = "BLACK_HOLE"
                st.error("Access Denied!")
                st.rerun()
    st.stop() # এই লাইনটিই নিশ্চিত করবে যে নিচে আর কিছু যাবে না

# --- ৫. মেইন সিস্টেম (পাসওয়ার্ড দিলেই কেবল এগুলো দেখাবে) ---
with st.sidebar:
    st.title("🛡️ Command Center")
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

menu = st.tabs(["🤖 AI Engine", "💻 Dev Console"])

with menu[0]:
    st.header("BaraQura Selling Machine")
    u_msg = st.text_input("Master Message", key="chatbot_input")
    if st.button("Send Message"):
        res = engine.generate_response("admin", "Master", u_msg)
        st.info(f"AI: {res}")

with menu[1]:
    st.header("Developer Console")
    st.success("System optimized and ready.")
