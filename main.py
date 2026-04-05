import streamlit as st
import os
import time
from datetime import datetime
from core.engine import BaraQuraEngine
from core.brain import BaraQuraBrain
from database.db_manager import DBManager

# ১. পেজ কনফিগ (সবার আগে)
st.set_page_config(page_title="BaraQura V10 Master", layout="wide")

# ২. স্ট্রিমলিট সিক্রেটস থেকে এপিআই কী লোড (Fixes 400 Error)
try:
    api_key = st.secrets["GEMINI_API_KEY"] #
except KeyError:
    st.error("Secrets-এ GEMINI_API_KEY পাওয়া যায়নি!")
    st.stop()

# ৩. সিস্টেম ইনিশিয়ালাইজ
db = DBManager()
brain = BaraQuraBrain(api_key) 
engine = BaraQuraEngine(db, brain)

# ৪. সেশন স্টেট (Old Security Logic)
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"

# --- ৫. ওল্ড সিকিউরিটি: BLACK HOLE ---
if st.session_state.system_status == "BLACK_HOLE":
    st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE")
    if st.button("Emergency Revive"):
        st.session_state.system_status = "ACTIVE"
        st.session_state.wrong_attempts = 0
        st.rerun()
    st.stop()

# --- ৬. ওল্ড সিকিউরিটি: লগইন গেট (Fixes 1000013713.jpg) ---
if not st.session_state.authenticated:
    st.title("🛡️ BaraQura Universe Access")
    with st.form("security_gate"):
        key = st.text_input("Enter Master Key", type="password")
        if st.form_submit_button("Verify Identity"):
            if key == "V8_UNIVERSE_GOD_2026":
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.session_state.wrong_attempts += 1
                if st.session_state.wrong_attempts >= 3:
                    st.session_state.system_status = "BLACK_HOLE"
                st.error(f"Access Denied! Attempt: {st.session_state.wrong_attempts}/3")
                st.rerun()
    st.stop() # পাসওয়ার্ড ছাড়া নিচে যাবে না

# --- ৭. নিউ ড্যাশবোর্ড (পাসওয়ার্ড দিলেই কেবল এখানে আসবে) ---
with st.sidebar:
    st.title("🛡️ Command Center")
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

menu = st.tabs(["🤖 AI Sales Engine", "💻 Dev Console"])

with menu[0]:
    st.header("BaraQura Selling Machine")
    u_msg = st.text_input("Client Message", key="main_chat")
    if st.button("Send"):
        if u_msg:
            # এখন জেমিনি কথা বলবে যেহেতু এপিআই কী সিক্রেটস থেকে লোড হয়েছে
            res = engine.generate_response("admin", "Master", u_msg) 
            st.info(f"AI: {res}")
        else:
            st.warning("মেসেজ লেখ দোস্ত!")

with menu[1]:
    st.header("Developer Console")
    st.success("System optimized and API key connected via Secrets.")
