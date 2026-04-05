import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. কোর সিস্টেম সেটআপ
load_dotenv()
db = DBManager()

# সেশন স্টেট (সব ফিচার সচল রাখার জন্য)
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"
if 'start_time' not in st.session_state: st.session_state.start_time = time.time()

# --- ২. সিকিউরিটি গেটওয়ে (৩ বার ভুল = ৪ নম্বরে ব্ল্যাকহোল) ---
def check_access():
    # ক. ব্ল্যাক হোল কন্ডিশন
    if st.session_state.system_status == "BLACK_HOLE":
        st.error("🌌 SYSTEM ABSORBED BY BLACK HOLE.")
        st.markdown("<h1 style='color:red; text-align:center;'>🚨 PERMANENT LOCK 🚨</h1>", unsafe_allow_html=True)
        # ইমারজেন্সি রিকভারি
        with st.expander("Recovery Console"):
            magic = st.text_input("Enter Magic Recovery Code", type="password")
            if st.button("Revive Universe"):
                if magic == "V8_UNIVERSE_GOD_2026":
                    st.session_state.system_status = "ACTIVE"
                    st.session_state.wrong_attempts = 0
                    st.rerun()
        st.stop()

    # খ. মাস্টার এক্সেস প্যানেল
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Universe Access")
        
        lives = 3 - st.session_state.wrong_attempts
        if st.session_state.wrong_attempts > 0:
            st.warning(f"⚠️ Warning: {lives} attempts left. Next failure triggers Black Hole!")

        with st.form("security_gate"):
            master_key = st.text_input("Enter Long Master Key", type="password")
            if st.form_submit_button("Verify Identity"):
                if master_key.strip() == "V8_UNIVERSE_GOD_2026":
                    st.session_state.authenticated = True
                    st.balloons()
                    st.rerun()
                else:
                    st.session_state.wrong_attempts += 1
                    if st.session_state.wrong_attempts >= 3:
                        st.session_state.system_status = "BLACK_HOLE"
                    st.rerun()
        st.stop()

check_access()

# --- ৩. মেইন ইউনিভার্স ইন্টারফেস (সব ওল্ড ফিচারসহ) ---
st.set_page_config(page_title="BaraQura Master Console", layout="wide")
engine = BaraQuraEngine(db, os.getenv("GEMINI_API_KEY"))

# ড্যাশবোর্ড ডেটা ক্যালকুলেশন
elapsed = int(time.time() - st.session_state.start_time)
mins, secs = divmod(elapsed, 60)
db.cursor.execute("SELECT COUNT(*) FROM users")
total_leads = db.cursor.fetchone()[0]

# --- সাইডবার (Command Center) ---
st.sidebar.title("🛡️ Command Center")
st.sidebar.success("Status: SECURE & ACTIVE")

with st.sidebar.expander("📡 System Pulse", expanded=True):
    st.write(f"**Active Time:** {mins}m {secs}s")
    st.write(f"**Leads Collected:** {total_leads}")
    load_val = 5 + (total_leads * 2)
    st.write(f"**System Load:** {load_val}%")
    st.progress(min(load_val, 100))

# লগআউট বাটন (তোর রিকোয়েস্ট মতো)
if st.sidebar.button("🚪 Logout & Lock System", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.wrong_attempts = 0
    st.rerun()

# নেভিগেশন মেনু
menu = st.sidebar.radio("Navigation", ["🤖 AI Engine", "📊 Lead Dashboard", "💻 Developer Tools"])

if menu == "🤖 AI Engine":
    st.header("BaraQura Selling Machine")
    target = st.text_input("Target User ID", "user_01")
    u_msg = st.text_area("Input Message")
    if st.button("Execute AI"):
        res = engine.generate_response(target, "Master", u_msg)
        st.info(f"Engine Response: {res}")

elif menu == "📊 Lead Dashboard":
    st.header("Database & Lead Management")
    st.write(f"Total Leads in Universe: **{total_leads}**")
    # এখানে তোর ডাটাবেজ টেবিল দেখানোর কোড থাকবে

elif menu == "💻 Developer Tools":
    st.header("Developer Advanced Console")
    st.code("System Path: /mount/src/hasan-universe-v10")
    st.write("Environment: Python 3.10 | Streamlit 1.32")
    if st.button("Clear Cache & Re-optimize"):
        st.cache_data.clear()
        st.success("Optimization Complete!")
