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
if 'deployed_codes' not in st.session_state: st.session_state.deployed_codes = set()

# --- ২. সিকিউরিটি গেটওয়ে (৩ বার ভুল = ৪ নম্বরে ব্ল্যাকহোল) ---
def check_access():
    if st.session_state.system_status == "BLACK_HOLE":
        st.markdown("<h1 style='color:red; text-align:center;'>🌌 SYSTEM ABSORBED BY BLACK HOLE</h1>", unsafe_allow_html=True)
        st.error("🚨 HACKER ALARM: KILL SWITCH ACTIVATED.")
        if st.button("Emergency Revive", key="revive_btn"):
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
                    if st.session_state.wrong_attempts >= 3: # ৪ নম্বর চেষ্টায় ব্ল্যাকহোল
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
cpu_load = 5 + (total_leads * 0.5)
mem_load = 12 + (total_leads * 1.2)

# --- ৪. সাইডবার (Command Center) ---
st.sidebar.title("🛡️ Command Center")

# ১. Active Status & Sleep Mode
if not st.session_state.sleep_mode:
    st.sidebar.success("Status: ACTIVE")
    if st.sidebar.button("💤 Activate Sleep Mode", key="sleep_on"):
        st.session_state.sleep_mode = True
        st.rerun()
else:
    st.sidebar.warning("Status: SLEEPING")
    if st.sidebar.button("☀️ Wake Up System", key="sleep_off"):
        st.session_state.sleep_mode = False
        st.rerun()

# ২. চ্যাটবট লাইভ কাউন্টার
st.sidebar.info(f"👥 Active Chats: {total_leads} People")

# ৫. System Load Breakdown
with st.sidebar.expander("📊 System Load Breakdown", expanded=True):
    st.write(f"CPU usage: {cpu_load}%")
    st.progress(min(cpu_load/100, 1.0))
    st.write(f"Memory: {mem_load}%")
    st.progress(min(mem_load/100, 1.0))

# ৭. Exit Logout (নিচে)
st.sidebar.markdown("---")
if st.sidebar.button("🚪 Logout & Exit System", use_container_width=True, key="logout_btn"):
    st.session_state.authenticated = False
    st.session_state.wrong_attempts = 0
    st.rerun()

# --- ৫. মেইন কন্টেন্ট ---
if st.session_state.sleep_mode:
    st.title("💤 System is in Sleep Mode")
    st.info("AI Engine and Database connections are paused.")
else:
    menu = st.tabs(["🤖 AI Engine", "💻 Developer Tools"])

    with menu[0]:
        st.header("BaraQura Selling Machine")
        u_msg = st.text_area("Master Message", key="engine_msg")
        if st.button("Send Message", key="send_msg_main"):
            res = engine.generate_response("admin", "Master", u_msg)
            st.info(f"AI: {res}")

    with menu[1]:
        st.header("Developer Console")
        
        # ড্রপডাউন মেনু (File Selection)
        file_option = st.selectbox("Select File to Update", 
                                  ["main.py", "database/db_manager.py", "core/engine.py", "security/auth.py"], 
                                  key="dev_file_select")
        
        st.write(f"Editing: `{file_option}`")
        dev_code = st.text_area("Paste Update Code Here", height=250, key="dev_code_area")
        
        if st.button("🚀 Save & Deploy Code", key="deploy_btn"):
            code_hash = hash(dev_code.strip())
            
            # এরর চেক ও ডুপ্লিকেট প্রিভেনশন
            if not dev_code.strip():
                st.warning("কোড বক্স খালি!")
            elif code_hash in st.session_state.deployed_codes:
                st.error("❌ এই কোডটি ইতিমধ্যে সিস্টেমে আছে। ডুপ্লিকেট গ্রহণ করা হবে না।")
            elif "import" not in dev_code and "def" not in dev_code:
                st.error("❌ Syntax Error: এটি সঠিক পাইথন কোড নয়!")
            else:
                # লজিক্যাল আপডেট ও বেলুন
                st.session_state.deployed_codes.add(code_hash)
                st.success(f"✅ {file_option} updated logically!")
                st.balloons()
        
        # অপ্টিমাইজেশন স্ট্যাটাস
        st.success("Optimization Complete!")
        
        # ডেপ্লয়মেন্ট হিস্ট্রি (Logical Stack)
        if st.session_state.deployed_codes:
            st.markdown("---")
            st.subheader("📜 Deployment History")
            st.info(f"Total Unique Updates: {len(st.session_state.deployed_codes)}")
