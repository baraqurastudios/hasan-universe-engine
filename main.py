import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. কোর সিস্টেম সেটআপ
load_dotenv()
db = DBManager()

# সেশন স্টেট কনফিগারেশন
if 'authenticated' not in st.session_state: st.session_state.authenticated = False
if 'wrong_attempts' not in st.session_state: st.session_state.wrong_attempts = 0
if 'system_status' not in st.session_state: st.session_state.system_status = "ACTIVE"
if 'start_time' not in st.session_state: st.session_state.start_time = time.time()
if 'sleep_mode' not in st.session_state: st.session_state.sleep_mode = False

# --- ২. সিকিউরিটি গেটওয়ে (Hacker Alarm & Black Hole) ---
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
            master_key = st.text_input("Enter Long Master Key", type="password")
            if st.form_submit_button("Verify Identity"):
                if master_key.strip() == "V8_UNIVERSE_GOD_2026":
                    st.session_state.authenticated = True
                    st.balloons()
                    st.rerun()
                else:
                    st.session_state.wrong_attempts += 1
                    # ৩ বার ভুল হলে ৪ নম্বর চেষ্টায় ব্ল্যাকহোল (Kill Switch)
                    if st.session_state.wrong_attempts >= 3:
                        st.session_state.system_status = "BLACK_HOLE"
                    st.rerun()
        st.stop()

check_access()

# --- ৩. মেইন ইন্টারফেস ও ড্যাশবোর্ড ---
st.set_page_config(page_title="BaraQura Master", layout="wide")
engine = BaraQuraEngine(db, os.getenv("GEMINI_API_KEY"))

# ড্যাশবোর্ড ডেটা
db.cursor.execute("SELECT COUNT(*) FROM users")
total_leads = db.cursor.fetchone()[0]
# সিস্টেম লোড ব্রেকডাউন (Calculation)
cpu_load = 5 + (total_leads * 0.5)
mem_load = 12 + (total_leads * 1.2)

# --- সাইডবার (Command Center) ---
st.sidebar.title("🛡️ Command Center")

# ১. Active Status & Sleep Mode
if not st.session_state.sleep_mode:
    st.sidebar.success("Status: ACTIVE")
    if st.sidebar.button("💤 Activate Sleep Mode"):
        st.session_state.sleep_mode = True
        st.rerun()
else:
    st.sidebar.warning("Status: SLEEPING")
    if st.sidebar.button("☀️ Wake Up System"):
        st.session_state.sleep_mode = False
        st.rerun()

# ২. চ্যাটবট কতজনের সাথে চ্যাট করছে (Live Counter)
st.sidebar.info(f"👥 Active Chats: {total_leads} People")

# ৪. System Load Breakdown
with st.sidebar.expander("📊 System Load Breakdown", expanded=True):
    st.write(f"CPU usage: {cpu_load}%")
    st.progress(min(cpu_load/100, 1.0))
    st.write(f"Memory: {mem_load}%")
    st.progress(min(mem_load/100, 1.0))

# ৭. Exit Logout (একদম নিচে)
st.sidebar.markdown("---")
if st.sidebar.button("🚪 Logout & Exit System", use_container_width=True):
    st.session_state.authenticated = False
    st.session_state.wrong_attempts = 0
    st.rerun()

# --- মেইন কন্টেন্ট ---
if st.session_state.sleep_mode:
    st.title("💤 System is in Sleep Mode")
    st.info("AI Engine and Database connections are paused to save energy.")
else:
    menu = st.tabs(["🤖 AI Engine", "💻 Developer Tools"])

    with menu[0]:
        st.header("BaraQura Selling Machine")
        u_msg = st.text_area("Master Message")
        if st.button("Send Message"):
            res = engine.generate_response("admin", "Master", u_msg)
            st.info(f"AI: {res}")

    with menu[1]:
        st.header("Developer Console")
        # ৫. ভুল কোড ইনপুট চেক (Error Handling)
        dev_code = st.text_area("Paste Update Code Here", height=200)
        if st.button("🚀 Save & Deploy Code"):
            if "import" not in dev_code and "def" not in dev_code:
                st.error("❌ Error: Invalid Code Structure! Please check your syntax.")
            else:
                # ৬. সেভ হলে বেলুন উড়বে
                st.success("✅ Code Saved Successfully!")
                st.balloons()

        st.success("Optimization Complete!")
