import streamlit as st
import os
import sys
import logging
from datetime import datetime

# --- ১. পাথ সেটআপ (যাতে ইমপোর্ট এরর না হয়) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
# সাব-ফোল্ডারগুলোকে সিস্টেম পাথে যুক্ত করা
for folder in ['security', 'core', 'database', 'interface']:
    path = os.path.join(current_dir, folder)
    if path not in sys.path:
        sys.path.append(path)

# --- ২. মডিউল ইমপোর্ট (সুরক্ষিত পদ্ধতি) ---
try:
    # সরাসরি ক্লাস ইমপোর্ট করার চেষ্টা
    from engine import Engine
    from guardian import SecurityManager
    
    # অপশনাল মডিউল
    try: from db_manager import DatabaseManager
    except: DatabaseManager = None
    try: from worker import Interface
    except: Interface = None
except ImportError:
    # যদি সরাসরি না পায়, তবে ফোল্ডার পাথ সহ ট্রাই করবে
    from core.engine import Engine
    from security.guardian import SecurityManager
    DatabaseManager = None
    Interface = None

# --- ৩. UI কনফিগারেশন ---
st.set_page_config(page_title="BaraQura V8.2", page_icon="🤖", layout="wide")
st.title("🤖 BaraQura V8.2: The Omni-Intelligence")
st.markdown("---")

# --- ৪. সেশন স্টেট ---
if 'initialized' not in st.session_state:
    try:
        st.session_state.security = SecurityManager()
        st.session_state.core = Engine()
        if DatabaseManager: st.session_state.db = DatabaseManager()
        st.session_state.initialized = True
    except Exception as e:
        st.error(f"❌ সিস্টেম লোড এরর: {e}")
        st.stop()

# --- ৫. ইন্টারফেস ---
with st.sidebar:
    st.header("⚙️ System Status")
    if os.path.exists(".hidden_vault_locked"):
        st.error("Status: BLACK HOLE")
    else:
        st.success("Core: Online")
    st.info(f"Time: {datetime.now().strftime('%H:%M:%S')}")

user_input = st.text_input("Enter Master Command / Key:", type="password")

if st.button("🚀 Run Command"):
    if not user_input:
        st.warning("⚠️ কি প্রদান করুন!")
    else:
        try:
            # ১. সিকিউরিটি ভ্যালিডেশন (Guardian)
            if st.session_state.security.validate(user_input):
                with st.spinner("Processing..."):
                    # ২. কোর প্রসেসিং (Engine)
                    result = st.session_state.core.process(user_input)
                    st.write(result)
                    
                    if "🔓" in result:
                        st.success("✅ Access Granted")
                    elif "🚨" in result or "🌌" in result:
                        st.error("⛔ System Lockdown")
            else:
                st.error("🚫 Access Denied!")
        except Exception as e:
            st.error(f"❌ Runtime Error: {e}")
