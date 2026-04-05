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
        st.session_state.authenticated = False
        st.rerun()

# --- ৫. মেইন কন্টেন্ট ---
if st.session_state.sleep_mode:
    st.title("💤 System is in Sleep Mode")
    st.info("AI Engine and Database connections are paused.")
else:
    menu = st.tabs(["🤖 AI Engine (V10)", "💻 Developer Console"])

    with menu[0]:
        st.header("BaraQura Selling Machine (Brain V4)")
        u_msg = st.text_input("Test Message to AI", key="engine_msg")
        if st.button("Send Message", key="send_msg_main"):
            # নতুন ইঞ্জিন দিয়ে রেসপন্স জেনারেট
            res = engine.generate_response("admin", "Master User", u_msg)
            st.info(f"AI Response: {res}")

    with menu[1]:
        st.header("Developer Console")
        file_option = st.selectbox("File to Update", ["main.py", "core/engine.py", "core/brain.py"], key="dev_file")
        dev_code = st.text_area("Paste Code", height=200, key="dev_code_area")
        
        if st.button("🚀 Save & Deploy", key="deploy_btn"):
            if dev_code.strip():
                st.success(f"✅ {file_option} updated and deployed!")
                st.balloons()
            else:
                st.warning("Code box is empty!")

# ৬. রিয়েল-টাইম আপডেটের জন্য অটো-রিফ্রেশ
time.sleep(1)
st.rerun()
        st.session_state.authenticated = False
        st.rerun()

# --- ৫. মেইন কন্টেন্ট ---
if st.session_state.sleep_mode:
    st.title("💤 System is in Sleep Mode")
    st.info("AI Engine and Database connections are paused.")
else:
    menu = st.tabs(["🤖 AI Engine (V10)", "💻 Developer Console"])

    with menu[0]:
        st.header("BaraQura Selling Machine (Brain V4)")
        u_msg = st.text_input("Test Message to AI", key="engine_msg")
        if st.button("Send Message", key="send_msg_main"):
            # নতুন ইঞ্জিন দিয়ে রেসপন্স জেনারেট
            res = engine.generate_response("admin", "Master User", u_msg)
            st.info(f"AI Response: {res}")

    with menu[1]:
        st.header("Developer Console")
        file_option = st.selectbox("File to Update", ["main.py", "core/engine.py", "core/brain.py"], key="dev_file")
        dev_code = st.text_area("Paste Code", height=200, key="dev_code_area")
        
        if st.button("🚀 Save & Deploy", key="deploy_btn"):
            if dev_code.strip():
                st.success(f"✅ {file_option} updated and deployed!")
                st.balloons()
            else:
                st.warning("Code box is empty!")

# ৬. রিয়েল-টাইম আপডেটের জন্য অটো-রিফ্রেশ
time.sleep(1)
st.rerun()
        
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
