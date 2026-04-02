import streamlit as st
import os
import sys
import json

# ১. পাথ সেটআপ (সরাসরি এবং নিখুঁত)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'core'))
sys.path.append(os.path.join(BASE_DIR, 'security'))

# ২. মডিউল ইমপোর্ট
try:
    from engine import Engine
    from guardian import SecurityManager
except ImportError:
    st.error("❌ মডিউল খুঁজে পাওয়া যাচ্ছে না! আপনার core এবং security ফোল্ডার চেক করুন।")
    st.stop()

# ৩. সেশন স্টেট (লগইন স্ট্যাটাস ধরে রাখা)
if 'auth' not in st.session_state:
    st.session_state.auth = False

# ৪. ইন্টারফেস ডিজাইন
st.set_page_config(page_title="BaraQura V8.2", layout="wide")

# লগইন করা না থাকলে
if not st.session_state.auth:
    st.title("🤖 BaraQura V8.2: Omni-Intelligence")
    
    key_input = st.text_input("Enter Master Command / Key:", type="password")
    
    if st.button("🚀 Run Command"):
        guardian = SecurityManager()
        engine = Engine()
        
        # কিল-সুইচ চেক
        if not guardian.validate(key_input):
            st.error("🚫 Access Denied!")
        else:
            # পাসওয়ার্ড চেক
            result = engine.process(key_input)
            if "🔓" in result:
                st.session_state.auth = True
                st.rerun() # পেজ রিফ্রেশ করে ড্যাশবোর্ড দেখাবে
            else:
                st.error(result)

# লগইন করা থাকলে (ড্যাশবোর্ড)
else:
    st.success("🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম অনলাইন।")
    
    try:
        # সরাসরি আপনার config/v82_config.json থেকে ডাটা রিড
        config_path = os.path.join(BASE_DIR, "config", "v82_config.json")
        with open(config_path, 'r') as f:
            data = json.load(f)
        
        # ডাটা ডিসপ্লে
        st.subheader("📊 Assets Overview")
        col1, col2 = st.columns(2)
        col1.metric("Total Profit", f"${data['empire_assets']['total_profit']}")
        col2.metric("Active Nodes", data['empire_assets']['active_nodes'])
        
        st.markdown("---")
        if st.button("🔴 Logout"):
            st.session_state.auth = False
            st.rerun()
            
    except Exception as e:
        st.error(f"Error loading dashboard: {e}")
