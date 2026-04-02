import streamlit as st
import os
import sys
import logging
from datetime import datetime

# --- ১. ডিরেক্টরি পাথ সেটআপ (যাতে মডিউলগুলো খুঁজে পায়) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
folders = ['security', 'core', 'database', 'interface', 'config']
for folder in folders:
    folder_path = os.path.join(current_dir, folder)
    if folder_path not in sys.path:
        sys.path.append(folder_path)

# --- ২. লগিং সিস্টেম সেটআপ ---
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

# --- ৩. মডিউল ইমপোর্ট (Try-Except সহ) ---
try:
    from core.engine import Engine
    from database.db_manager import DatabaseManager
    from security.guardian import SecurityManager
    from interface.worker import Interface
except ImportError as e:
    st.error(f"❌ Critical Module Missing: {e}")
    logging.error(f"Import Error: {e}")
    st.stop()

# --- ৪. Streamlit UI কনফিগারেশন ---
st.set_page_config(
    page_title="BaraQura Jarvis V9",
    page_icon="🤖",
    layout="wide"
)

# --- ৫. সেশন স্টেট (Infinite Loading বন্ধ করার জন্য) ---
if 'initialized' not in st.session_state:
    try:
        st.session_state.security = SecurityManager()
        st.session_state.db = DatabaseManager()
        st.session_state.core = Engine()
        st.session_state.ui = Interface()
        st.session_state.initialized = True
        logging.info("Jarvis Modules Initialized in Session State")
    except Exception as e:
        st.error(f"❌ System initialization failed: {e}")
        st.stop()

# --- ৬. মেইন ইন্টারফেস ---
st.title("🤖 BaraQura Jarvis Engine V9")
st.markdown("---")

# সাইডবারে সিস্টেম স্ট্যাটাস দেখা যাবে
with st.sidebar:
    st.header("⚙️ System Status")
    st.success("Core: Online")
    st.success("Security: Active")
    st.info(f"Time: {datetime.now().strftime('%H:%M:%S')}")

# ইউজার ইনপুট (পাসওয়ার্ড টাইপ ইনপুট বক্সে সিকিউরিটি বেশি থাকে)
user_input = st.text_input("Enter Master Command / Key:", type="password", placeholder="Type here...")

if st.button("🚀 Run Command"):
    if not user_input:
        st.warning("⚠️ Please provide a command or key first!")
    else:
        try:
            # ১. সিকিউরিটি ভ্যালিডেশন
            if st.session_state.security.validate(user_input):
                with st.spinner("Processing..."):
                    # ২. ইঞ্জিন প্রসেসিং
                    result = st.session_state.core.core_process(user_input) if hasattr(st.session_state.core, 'core_process') else st.session_state.core.process(user_input)
                    
                    # ৩. ডাটাবেসে সেভ
                    st.session_state.db.save(result)
                    
                    # ৪. আউটপুট দেখানো
                    st.success("✅ Execution Successful")
                    st.write(result)
                    logging.info(f"Command executed successfully: {user_input[:3]}***")
            else:
                st.error("🚫 Access Denied! Security Lockdown may trigger.")
                logging.warning(f"Unauthorized access attempt blocked.")
                
        except Exception as e:
            st.error(f"❌ Runtime Error: {e}")
            logging.error(f"Execution Error: {str(e)}")

# --- চ্যাট হিস্ট্রি বা লগ দেখার অপশন (ঐচ্ছিক) ---
if st.checkbox("Show System Activity Log"):
    if os.path.exists('logs/system.log'):
        with open('logs/system.log', 'r') as f:
            st.code(f.readlines()[-10:]) # শেষ ১০টি লগ দেখাবে
