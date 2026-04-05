import streamlit as st
import os
import time
from dotenv import load_dotenv
from database.db_manager import DBManager
from core.engine import BaraQuraEngine

# ১. এনভায়রনমেন্ট লোড করা
load_dotenv()

# --- ২. ব্ল্যাক হোল সিকিউরিটি (V8 Universe God Edition) ---
def check_access():
    # কিল সুইচ চেক
    if 'system_status' not in st.session_state:
        st.session_state.session_status = "ACTIVE"

    if st.session_state.get('system_status') == "KILLED":
        st.error("⚠️ SYSTEM TERMINATED BY MASTER.")
        revive_key = st.text_input("Enter Emergency Master Key to Revive", type="password")
        if revive_key == "Meen#8.10":
            st.session_state.system_status = "ACTIVE"
            st.success("Engine Revived!")
            st.rerun()
        st.stop()

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.title("🛡️ BaraQura Universe Access")
        
        if 'press_times' not in st.session_state:
            st.session_state.press_times = []

        # ধাপ ১: রিদমিক বায়োমেট্রিক (ট্যাপ)
        st.subheader("Step 1: Rhythm Check")
        if st.button("🔴 TAP RHYTHM HERE"):
            st.session_state.press_times.append(time.time())
            st.toast(f"Input {len(st.session_state.press_times)} recorded")

        # ধাপ ২: মাস্টার অথরাইজেশন
        st.subheader("Step 2: Authorization")
        master_key_input = st.text_input("Master Key", type="password")
        
        # আইডেন্টিটি কনফার্মেশন লজিক (সন্দেহ হলে ম্যাজিক ওয়ার্ড চাবে)
        count = len(st.session_state.press_times)
        is_suspicious = count > 0 and count != 3 and count != 6
        
        if is_suspicious:
            st.warning("⚠️ Identity Suspicion! Confirmation Required.")
            magic_confirm = st.text_input("Confirm Magic Word (Identity Check)")
        else:
            # সন্দেহ না থাকলেও প্রোটেকশন হিসেবে ফিল্ডটি রাখা হলো (তোর রিকোয়ারমেন্ট অনুযায়ী)
            magic_confirm = st.text_input("Magic Word Confirmation")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Verify & Unlock God Mode"):
                # কন্ডিশন: মেইন কি অথবা ইমারজেন্সি কি মিলতে হবে + ম্যাজিক ওয়ার্ড কনফার্ম হতে হবে
                valid_key = (master_key_input == "V8_UNIVERSE_GOD_2026" or master_key_input == "Meen#8.10")
                if valid_key and magic_confirm.lower() == "meem":
                    if count == 3 or count
