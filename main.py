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

# --- ২. সিকিউরিটি লেয়ার (এটি সবার আগে থাকবে) ---
if st.session_state.system_status == "BLACK_HOLE":
    st.markdown("<h1 style='color:red; text-align:center;'>🌌 BLACK HOLE ACTIVATED</h1>", unsafe_allow_html=True)
    if st.button("Emergency Revive"):
        st.session_state.system_status = "ACTIVE"
        st.session_state.wrong_attempts = 0
        st.rerun()
    st.stop()

if not st.session_state.authenticated:
    st.title("🛡️ BaraQura Universe Access")
    # কন্টেইনার ব্যবহার করছি যাতে UI ক্লিন থাকে
    with st.container():
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
                    st.warning(f"Wrong Key! Attempt: {st.session_state.wrong_attempts}/3")
                    st.rerun()
    st.stop() # পাসওয়ার্ড না দিলে নিচের কোনো কোড রান হবে না

# --- ৩. মেইন চ্যাটবট ইন্টারফেস (পাসওয়ার্ড সফল হলেই এখানে আসবে) ---
st.set_page_config(page_title="BaraQura Master V10", layout="wide")

# সাইডবার
with st.sidebar:
    st.title("🛡️ Command Center")
    st.success("Status: ACTIVE") #
    if st.button("🚪 Logout & Exit"):
        st.session_state.authenticated = False
        st.rerun()

# মেইন ট্যাব
menu = st.tabs(["🤖 AI Engine", "💻 Dev Console"]) #

with menu[0]:
    st.header("BaraQura Selling Machine")
    u_msg = st.text_area("Master Message", key="chatbot_msg_area")
    if st.button("Send Message"):
        if u_msg:
            res = engine.generate_response("admin", "Master", u_msg)
            st.info(f"AI: {res}")
        else:
            st.warning("মেসেজ খালি!")

with menu[1]:
    st.header("Developer Console")
    st.write("System optimized and ready.")

# অটো রিফ্রেশ (ঘড়ির জন্য)
time.sleep(1)
st.rerun()
