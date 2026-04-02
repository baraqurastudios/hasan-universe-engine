import streamlit as st
import os
import sys
import logging
from datetime import datetime

# --- ১. পাথ সেটআপ (যাতে সব ফোল্ডারের ফাইল খুঁজে পায়) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
folders = ['security', 'core', 'database', 'interface']
for folder in folders:
    path = os.path.join(current_dir, folder)
    if path not in sys.path:
        sys.path.append(path)

# --- ২. লগিং ---
if not os.path.exists('logs'): os.makedirs('logs')
logging.basicConfig(filename='logs/system.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# --- ৩. মডিউল ইমপোর্ট ---
try:
    from core.engine import Engine
    from security.guardian import SecurityManager
    # ডাটাবেস ও ইন্টারফেস যদি থাকে তবে ইমপোর্ট হবে
    try: from database.db_manager import DatabaseManager
    except: DatabaseManager = None
    try: from interface.worker import Interface
    except: Interface = None
except ImportError as e:
    st.error(f"❌ মডিউল লোড এরর: {e}")
    st.stop()

# --- ৪. UI কনফিগারেশন ---
st.set_page_config(page_title="BaraQura V8.2", page_icon="🤖", layout="wide")
st.title("🤖 BaraQura V8.2: The Omni-Intelligence")
st.markdown("---")

# --- ৫. সেশন স্টেট ইনিশিয়ালাইজেশন ---
if 'initialized' not in st.session_state:
    try:
        st.session_state.security = SecurityManager()
        st.session_state.core = Engine()
        if DatabaseManager: st.session_state.db = DatabaseManager()
        if Interface: st.session_state.ui = Interface()
        st.session_state.initialized = True
    except Exception as e:
        st.error(f"❌ ইনিশিয়ালাইজেশন এরর: {e}")
        st.stop()

# --- ৬. ইন্টারফেস ---
with st.sidebar:
    st.header("⚙️ System Status")
    st.success("Core: Online")
    st.info(f"Time: {datetime.now().strftime('%H:%M:%S')}")

user_input = st.text_input("Enter Master Command / Key:", type="password")

if st.button("🚀 Run Command"):
    if not user_input:
        st.warning("⚠️ কি প্রদান করুন!")
    else:
        try:
            # সিকিউরিটি ভ্যালিডেশন
            if st.session_state.security.validate(user_input):
                with st.spinner("Processing..."):
                    result = st.session_state.core.process(user_input)
                    # ডাটাবেস থাকলে সেভ হবে
                    if hasattr(st.session_state, 'db'): st.session_state.db.save(result)
                    st.success("✅ Execution Successful")
                    st.write(result)
            else:
                st.error("🚫 Access Denied!")
        except Exception as e:
            st.error(f"❌ Runtime Error: {e}")
