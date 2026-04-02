import streamlit as st
import os
import sys
import json

# --- ১. প্রাথমিক পাথ সেটআপ (নিশ্চিত করা যে পাইথন ফাইলগুলো খুঁজে পাবে) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, 'core'))
sys.path.append(os.path.join(BASE_DIR, 'security'))

# --- ২. মডিউল লোড করার নিরাপদ পদ্ধতি ---
try:
    from engine import Engine
    from guardian import SecurityManager
except Exception as e:
    st.error(f"❌ কোড ফাইল লোড করতে সমস্যা হচ্ছে! এরর: {e}")
    st.info("আপনার core/engine.py এবং security/guardian.py ফাইলগুলো ঠিক জায়গায় আছে কি না নিশ্চিত হোন।")
    st.stop()

# --- ৩. সেশন স্টেট (লগইন তথ্য মনে রাখার জন্য) ---
if 'auth_done' not in st.session_state:
    st.session_state.auth_done = False

st.set_page_config(page_title="BaraQura V8.2", layout="wide")

# --- ৪. ইউজার ইন্টারফেস (লগইন এবং ড্যাশবোর্ড) ---
if not st.session_state.auth_done:
    st.title("🤖 BaraQura V8.2: Omni-Intelligence")
    st.markdown("---")
    
    user_key = st.text_input("Enter Master Command / Key:", type="password", help="আপনার গোপন চাবিটি দিন")
    
    if st.button("🚀 Run Command"):
        if user_key:
            guardian = SecurityManager()
            engine = Engine()
            
            # কিল-সুইচ চেক (আপনার আগের লজিক)
            if guardian.validate(user_key):
                result = engine.process(user_key)
                if "🔓" in result:
                    st.session_state.auth_done = True
                    st.rerun() # সেশন আপডেট করে পেজ রিফ্রেশ করবে
                else:
                    st.error(result)
            else:
                st.error("🚫 Access Denied!")
        else:
            st.warning("⚠️ চাবি ছাড়া প্রবেশ নিষেধ।")

else:
    # লগইন সফল হলে যা দেখাবে
    st.success("🔓 স্বাগতম মাস্টার! BaraQura সিস্টেম এখন অনলাইন।")
    
    try:
        # সরাসরি আপনার config/v82_config.json থেকে তথ্য পড়া
        config_path = os.path.join(BASE_DIR, "config", "v82_config.json")
        with open(config_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # ড্যাশবোর্ড ডাটা ডিসপ্লে
        st.subheader("📊 Empire Analytics")
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Profit", f"${data['empire_assets']['total_profit']}")
        c2.metric("Active Nodes", data['empire_assets']['active_nodes'])
        c3.metric("System Tag", data['system_info']['system_tag'])
        
        st.markdown("---")
        if st.button("🔴 Logout / Secure"):
            st.session_state.auth_done = False
            st.rerun()
            
    except Exception as e:
        st.error(f"⚠️ ড্যাশবোর্ড ডাটা লোড করতে সমস্যা: {e}")
