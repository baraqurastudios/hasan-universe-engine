import streamlit as st
import os
import sys
from datetime import datetime

# ১. সঠিক পাথ সেটআপ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
for folder in ['core', 'security', 'database', 'interface']:
    path = os.path.join(BASE_DIR, folder)
    if path not in sys.path:
        sys.path.insert(0, path)

# ২. মডিউল ইমপোর্ট
try:
    from engine import Engine
    from guardian import SecurityManager
except ImportError:
    from core.engine import Engine
    from security.guardian import SecurityManager

# ৩. UI কনফিগারেশন
st.set_page_config(page_title="BaraQura V8.2", page_icon="🤖", layout="wide")
st.title("🤖 BaraQura V8.2: The Omni-Intelligence")

# ৪. সেশন স্টেট
if 'initialized' not in st.session_state:
    st.session_state.security = SecurityManager()
    st.session_state.core = Engine()
    st.session_state.initialized = True

# ৫. সাইডবার স্ট্যাটাস
with st.sidebar:
    st.header("⚙️ System Status")
    # কনফিগ ফোল্ডারের ভেতরে ব্ল্যাক হোল চেক
    is_locked = os.path.exists(os.path.join("config", ".black_hole_vault")) or os.path.exists(".hidden_vault_locked")
    if is_locked:
        st.error("Status: BLACK HOLE")
    else:
        st.success("Core: Online")

# ৬. ইন্টারফেস
user_input = st.text_input("Enter Master Command / Key:", type="password")

if st.button("🚀 Run Command"):
    if not user_input:
        st.warning("⚠️ কি প্রদান করুন!")
    else:
        if st.session_state.security.validate(user_input):
            result = st.session_state.core.process(user_input)
            st.write(result)
            if "🔓" in result: st.success("✅ Access Granted")
            elif "🚨" in result: st.error("⛔ System Lockdown")
        else:
            st.error("🚫 Access Denied!")
