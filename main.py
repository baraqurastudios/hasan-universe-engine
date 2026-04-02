import streamlit as st
import os
import sys
import json

# ১. পাথ সেটআপ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'core'))
sys.path.append(os.path.join(BASE_DIR, 'security'))

# ২. মডিউল ইমপোর্ট
try:
    from engine import Engine
    from guardian import SecurityManager
except Exception as e:
    st.error(f"Error loading modules: {e}")
    st.stop()

# ৩. সেশন স্টেট
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

st.set_page_config(page_title="BaraQura V8.2", layout="wide")

# ৪. ইন্টারফেস
if not st.session_state.authenticated:
    st.title("🤖 BaraQura V8.2: Omni-Intelligence")
    user_key = st.text_input("Enter Master Key:", type="password")
    
    if st.button("🚀 Login"):
        guardian = SecurityManager()
        engine = Engine()
        if guardian.validate(user_key):
            result = engine.process(user_key)
            if "🔓" in result:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error(result)
        else:
            st.error("🚫 Access Denied!")
else:
    # লগইন সফল হলে ড্যাশবোর্ড দেখাবে
    st.success("🔓 স্বাগতম মাস্টার!")
    try:
        config_path = os.path.join(BASE_DIR, "config", "v82_config.json")
        with open(config_path, 'r') as f:
            data = json.load(f)
        
        st.subheader("📊 Empire Analytics")
        col1, col2 = st.columns(2)
        col1.metric("Total Profit", f"${data['empire_assets']['total_profit']}")
        col2.metric("Active Nodes", data['empire_assets']['active_nodes'])
        
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()
    except Exception as e:
        st.error(f"Dashboard Error: {e}")
