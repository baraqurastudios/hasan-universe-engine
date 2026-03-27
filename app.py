import streamlit as st
import datetime

# --- ১. সিকিউরিটি গেট ---
def check_password():
    if "authenticated" not in st.session_state:
        st.markdown("<h2 style='text-align: center;'>👑 BaraQura Admin Gate</h2>", unsafe_allow_html=True)
        pwd = st.text_input("পাসওয়ার্ড দিন", type="password")
        if st.button("প্রবেশ করুন"):
            if pwd == "bq2026": 
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("ভুল পাসওয়ার্ড!")
        return False
    return True

if check_password():
    # --- ২. মেইন ড্যাশবোর্ড ---
    st.set_page_config(page_title="BaraQura Empire", page_icon="👑")
    st.title("🎬 BaraQura Empire: Command Center")
    st.write(f"**আজকের তারিখ:** {datetime.date.today()}")

    # ক্যারেক্টার ও শিডিউল আপডেট
    st.sidebar.header("👤 ক্যারেক্টার ডাটাবেজ")
    st.sidebar.info("**প্রধান চরিত্র:** হাসান (৭ বছর)")
    st.sidebar.info("**মা:** লিজা")
    
    st.subheader("📅 পাবলিশিং শিডিউল")
    st.info("সোমবার ও শুক্রবার: ৫:৩০ PM (Shorts) | মাসে ১টি বড় ভিডিও")

    # আপডেট গেট
    st.divider()
    st.subheader("🔮 ওরাকল গেট")
    user_input = st.text_area("নতুন আইডিয়া বা স্ক্রিপ্ট এখানে লিখুন...")
    if st.button("ইঞ্জিনে সেভ করুন"):
        st.balloons()
        st.success("সাকিবুল ভাই, আপনার আইডিয়া সেভ হয়েছে!")
