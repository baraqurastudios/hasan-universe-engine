import streamlit as st
import os
import json

# --- ১. পেজ সেটআপ ---
st.set_page_config(page_title="BaraQura V8.2 Dashboard", layout="wide", initial_sidebar_state="collapsed")

# স্টাইল সেট করা (ডার্ক থিম লুকের জন্য)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; }
    </style>
    """, unsafe_allow_status_code=True)

# --- ২. সেশন ম্যানেজমেন্ট ---
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- ৩. ইন্টারফেস লজিক ---
if not st.session_state.authenticated:
    st.title("🤖 BaraQura V8.2: Omni-Intelligence")
    st.info("সিস্টেমটি সচল করতে আপনার মাস্টার কি (Master Key) ব্যবহার করুন।")
    
    # ইনপুট ফিল্ড
    master_key_input = st.text_input("Enter Master Command / Key:", type="password")
    
    if st.button("🚀 Unlock System"):
        # কনফিগ ফাইল থেকে সরাসরি যাচাই করা
        config_path = os.path.join(os.getcwd(), "config", "v82_config.json")
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                correct_key = config_data['security_layer']['master_key_hash']
            
            if master_key_input == correct_key:
                st.session_state.authenticated = True
                st.success("✅ Access Granted!")
                st.rerun()
            else:
                st.error("❌ ভুল চাবি! আপনার চেষ্টা বাকি আছে: ৩ বার") #
        except Exception as e:
            st.error(f"⚠️ সিস্টেম এরর: কনফিগ ফাইল লোড করা যাচ্ছে না। ({e})")

else:
    # লগইন সফল হলে যা দেখাবে (ড্যাশবোর্ড)
    st.title("🔓 BaraQura System Online")
    st.markdown("---")
    
    try:
        # ডাটা পড়া
        config_path = os.path.join(os.getcwd(), "config", "v82_config.json")
        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # ড্যাশবোর্ড ম্যাট্রিক্স
        st.subheader("📊 Empire Analytics Summary")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="Total Profit", value=f"${data['empire_assets']['total_profit']:,}")
        with col2:
            st.metric(label="Active Nodes", value=data['empire_assets']['active_nodes'])
        with col3:
            st.metric(label="System Tag", value=data['system_info']['system_tag'])
            
        st.markdown("---")
        st.success(f"ইঞ্জিন ভার্সন: {data['system_info']['engine_version']} | কোডনেম: {data['system_info']['codename']}")
        
        # লগআউট বাটন
        if st.button("🔴 Secure Logout"):
            st.session_state.authenticated = False
            st.rerun()
            
    except Exception as e:
        st.error(f"❌ ড্যাশবোর্ড ডাটা লোড করতে সমস্যা: {e}")
