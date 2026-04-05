import streamlit as st
import os
import time
from datetime import datetime
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine
from core.brain import BaraQuraBrain

# ১. পেজ কনফিগ (সবার আগে)
st.set_page_config(page_title="BaraQura V10 Master", layout="wide")

# ২. কোর লোড
load_dotenv()
db = DBManager()
brain = BaraQuraBrain(os.getenv("GEMINI_API_KEY"))
engine = BaraQuraEngine(db, brain)

# ৩. ওল্ড সেশন স্টেট (Security Logic)
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"
if 'login_time' not in st.session_state: st.session_state.login_time = time.time()

# --- ৪. ওল্ড সিকিউরিটি: BLACK HOLE PROTOCOL ---
if st.session_state.system_status == "BLACK_HOLE":
    st.markdown("<h1 style='color:red; text-align:center;'>🌌 SYSTEM ABSORBED BY BLACK HOLE</h1>", unsafe_allow_html=True)
    st.warning("আপনার সিকিউরিটি ৩ বার ভায়োলেট হয়েছে। সিস্টেম এখন লকড।")
    if st.button("🔴 Emergency Revive (Master Only)"):
        st.session_state.system_status = "ACTIVE"
        st.session_state.wrong_attempts = 0
        st.rerun()
    st.stop()

# --- ৫. ওল্ড সিকিউরিটি: MASTER ACCESS GATE ---
if not st.session_state.authenticated:
    st.title("🛡️ BaraQura Universe Access")
    with st.form("security_gate"):
        key = st.text_input("Enter Master Key", type="password")
        if st.form_submit_button("Verify Identity"):
            # তোর সেই ওল্ড মাস্টার কি
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
    st.stop() # এটিই নিশ্চিত করবে যে পাসওয়ার্ড ছাড়া নিউ ড্যাশবোর্ড আসবে না

# --- ৬. নিউ ড্যাশবোর্ড: V10 INTERFACE ---
with st.sidebar:
    st.title("🛡️ Command Center")
    st.markdown(f"**🕒 Current Time:** {datetime.now().strftime('%I:%M %p')}")
    st.info(f"⌛ Session: {int(time.time() - st.session_state.login_time) // 60} mins")
    if st.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.rerun()

# নিউ ট্যাব সিস্টেম
menu = st.tabs(["🤖 AI Sales Engine", "💻 Dev Console", "📊 Database"])

with menu[0]:
    st.header("BaraQura Selling Machine")
    u_msg = st.text_input("Client Message", placeholder="টাইপ করুন...", key="chat_input")
    if st.button("Send", key="send_btn"):
        if u_msg:
            # নিউ ব্রেন ও ইঞ্জিনের রেসপন্স
            res = engine.generate_response("admin", "Master", u_msg)
            st.chat_message("assistant").write(res)
        else:
            st.warning("কিছু তো লেখ দোস্ত!")

with menu[1]:
    st.header("Developer Console")
    st.success("Core V10 and Security V8 Integrated.")
    st.code("# Black Hole Protection: ON\n# AI Intent Detection: ACTIVE")

with menu[2]:
    st.header("Database Monitor")
    st.info("Connected to baraqura_v10.db")

# ঘড়ি আপডেট করার জন্য অটো রিফ্রেশ
time.sleep(2)
st.rerun()
