import streamlit as st
import os
import sys
import logging
from datetime import datetime

# --- ১. পাথ সেটআপ (যাতে ইমপোর্ট এরর না হয়) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
# সব সাব-ফোল্ডারকে সিস্টেমে চিনিয়ে দেওয়া
for folder in ['security', 'core', 'database', 'interface']:
    path = os.path.join(current_dir, folder)
    if path not in sys.path:
        sys.path.append(path)

# --- ২. মডিউল ইমপোর্ট ---
try:
    # সরাসরি ক্লাস ইমপোর্ট (যেহেতু পাথ উপরে অ্যাড করা হয়েছে)
    from engine import Engine
    from guardian import SecurityManager
    
    # অপশনাল মডিউল চেক
    try: from db_manager import DatabaseManager
    except: DatabaseManager = None
    try: from worker import Interface
    except: Interface = None
except ImportError:
    # অল্টারনেটিভ ইমপোর্ট পদ্ধতি
    from core.engine import Engine
    from security.guardian import SecurityManager
    DatabaseManager = None
    Interface = None

# --- ৩. UI কনফিগারেশন ---
st.set_page_config(page_title="BaraQura V8.2", page_icon="🤖", layout="wide")
st.title("🤖 BaraQura V8.2: The Omni-Intelligence")
st.markdown("---")

# --- ৪. সেশন স্টেট (সিস্টেম রানিং রাখার জন্য) ---
if 'initialized' not in st.session_state:
    try:
        st.session_state.security = SecurityManager()
        st.session_state.core = Engine()
        if DatabaseManager: st.session_state.db = DatabaseManager()
        st.session_state.initialized = True
    except Exception as e:
        st.error(f"❌ সিস্টেম লোড এরর: {e}")
        st.stop()

# --- ৫. সাইডবার স্ট্যাটাস ---
with st.sidebar:
    st.header("⚙️ System Status")
    # ব্ল্যাক হোল সক্রিয় কি না চেক
    if os.path.exists(".hidden_vault_locked") or os.path.exists(".black_hole_vault"):
        st.error("Status: BLACK HOLE ACTIVATED")
    else:
        st.success("Core: Online")
    st.info(f"Time: {datetime.now().strftime('%H:%M:%S')}")

# --- ৬. মেইন ইন্টারফেস ---
user_input = st.text_input("Enter Master Command / Key:", type="password")

if st.button("🚀 Run Command"):
    if not user_input:
        st.warning("⚠️ কি প্রদান করুন!")
    else:
        try:
            # ১. Guardian ভ্যালিডেশন (এখানেই PROTOCOL_ZERO_V8 চেক হবে)
            if st.session_state.security.validate(user_input):
                with st.spinner("Processing..."):
                    # ২. Engine প্রসেসিং (পাসওয়ার্ড এবং ব্ল্যাক হোল চেক)
                    result = st.session_state.core.process(user_input)
                    st.write(result)
                    
                    if "🔓" in result:
                        st.success("✅ Access Granted")
                    elif "🚨" in result or "🌌" in result:
                        st.error("⛔ System Lockdown")
            else:
                st.error("🚫 Access Denied or System Terminated!")
        except Exception as e:
            st.error(f"❌ Runtime Error: {e}")
