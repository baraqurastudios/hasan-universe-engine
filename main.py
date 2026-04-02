import streamlit as st
import os
import sys
import logging
from datetime import datetime

# --- ১. পাথ সেটআপ (নিশ্চিত করে যে মডিউলগুলো খুঁজে পাওয়া যাবে) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# সাব-ফোল্ডারগুলোকে যুক্ত করা (এটি আপনার দেওয়া নতুন পার্ট)
folders = ['core', 'security', 'database', 'interface']
for folder in folders:
    folder_path = os.path.join(BASE_DIR, folder)
    if folder_path not in sys.path:
        sys.path.insert(0, folder_path)

# --- ২. মডিউল ইমপোর্ট (সুরক্ষিত পদ্ধতি) ---
try:
    from engine import Engine
    from guardian import SecurityManager
    
    # অপশনাল মডিউল
    try: from db_manager import DatabaseManager
    except: DatabaseManager = None
    try: from worker import Interface
    except: Interface = None
except ImportError as e:
    # ব্যাকআপ ইমপোর্ট মেথড
    try:
        from core.engine import Engine
        from security.guardian import SecurityManager
    except Exception as inner_e:
        st.error(f"❌ Critical Import Error: {inner_e}")
        st.stop()
    DatabaseManager = None
    Interface = None

# --- ৩. UI কনফিগারেশন ---
st.set_page_config(page_title="BaraQura V8.2", page_icon="🤖", layout="wide")
st.title("🤖 BaraQura V8.2: The Omni-Intelligence")
st.markdown("---")

# --- ৪. সেশন স্টেট (সিস্টেম মেমোরি) ---
if 'initialized' not in st.session_state:
    try:
        st.session_state.security = SecurityManager()
        st.session_state.core = Engine()
        if DatabaseManager: st.session_state.db = DatabaseManager()
        st.session_state.initialized = True
    except Exception as e:
        st.error(f"❌ সিস্টেম ইনিশিয়ালাইজেশন এরর: {e}")
        st.stop()

# --- ৫. সাইডবার স্ট্যাটাস (ব্ল্যাক হোল চেক) ---
with st.sidebar:
    st.header("⚙️ System Status")
    # ব্ল্যাক হোল ফাইল আছে কি না চেক করা
    is_locked = os.path.exists(".hidden_vault_locked") or os.path.exists(".black_hole_vault")
    
    if is_locked:
        st.error("Status: BLACK HOLE ACTIVATED")
        st.warning("Recovery: Rename vault file on GitHub.")
    else:
        st.success("Core: Online")
    
    st.info(f"Time: {datetime.now().strftime('%H:%M:%S')}")

# --- ৬. মেইন ইন্টারফেস (কমান্ড ইনপুট) ---
user_input = st.text_input("Enter Master Command / Key:", type="password")

if st.button("🚀 Run Command"):
    if not user_input:
        st.warning("⚠️ কি প্রদান করুন!")
    else:
        try:
            # ১. Guardian ভ্যালিডেশন (PROTOCOL_ZERO_V8 চেক)
            if st.session_state.security.validate(user_input):
                with st.spinner("Processing..."):
                    # ২. Engine প্রসেসিং (পাসওয়ার্ড এবং ব্ল্যাক হোল প্রোটোকল)
                    result = st.session_state.core.process(user_input)
                    
                    if "🔓" in result:
                        st.success("✅ Access Granted")
                        st.write(result)
                    elif "🚨" in result or "🌌" in result:
                        st.error("⛔ System Lockdown")
                        st.write(result)
                        # লকডাউন হলে ইউজারকে রিফ্রেশ করতে বলা
                        st.button("Reload System")
                    else:
                        st.info(result)
            else:
                st.error("🚫 Access Denied or Kill-Switch Triggered!")
        except Exception as e:
            st.error(f"❌ Runtime Error: {e}")
