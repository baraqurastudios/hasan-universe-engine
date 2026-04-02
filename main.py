import streamlit as st
import os
import json

# অ্যাপ কনফিগারেশন
st.set_page_config(page_title="BaraQura V8.2 Dashboard", layout="wide")

# সেশন চেক
if 'auth' not in st.session_state:
    st.session_state.auth = False

# ১. লগইন লজিক (সহজভাবে)
if not st.session_state.auth:
    st.title("🤖 BaraQura V8.2: Terminal Access")
    key = st.text_input("Enter Master Key:", type="password")
    
    if st.button("Unlock System"):
        # সরাসরি আপনার config ফাইল থেকে পাসওয়ার্ড চেক
        config_path = os.path.join(os.getcwd(), "config", "v82_config.json")
        try:
            with open(config_path, 'r') as f:
                data = json.load(f)
                master_key = data['security_layer']['master_key_hash']
            
            if key == master_key:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied!")
        except Exception as e:
            st.error(f"Config Error: {e}")

# ২. ড্যাশবোর্ড (যদি লগইন সাকসেস হয়)
else:
    st.success("🔓 System Online: BaraQura Omni-Intelligence")
    
    try:
        # ডাটা লোড
        config_path = os.path.join(os.getcwd(), "config", "v82_config.json")
        with open(config_path, 'r') as f:
            data = json.load(f)
            
        st.subheader("📊 Empire Analytics")
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Profit", f"${data['empire_assets']['total_profit']}")
        c2.metric("Active Nodes", data['empire_assets']['active_nodes'])
        c3.metric("System Tag", data['system_info']['system_tag'])
        
        st.markdown("---")
        st.info("আপনার core/ ফোল্ডারের ফাইলগুলো সুরক্ষিত আছে। সিস্টেমটি এখন শুধু এই ড্যাশবোর্ড রান করছে।")
        
        if st.button("Secure Logout"):
            st.session_state.auth = False
            st.rerun()
    except Exception as e:
        st.error(f"Dashboard Load Error: {e}")
