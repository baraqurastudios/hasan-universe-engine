# ==========================================
# 🛰️ BARAQURA MASTER ENGINE v128.0 (GOD MODE)
# Features: AI Agent, Multi-File Control, Cloud Sync
# ==========================================

import streamlit as st
import openai
import os
import datetime
import base64

# --- ১. মেমোরি ও কনফিগারেশন ---
if "analytics" not in st.session_state:
    st.session_state.analytics = {"deploys": 0, "ai_tasks": 0}

st.set_page_config(page_title="BaraQura Cloud OS", layout="wide")
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- ২. অটোনোমাস এজেন্ট লজিক ---
def ai_agent_executor(task, file_path):
    """এটি আপনার ফাইল রিড করবে এবং AI দিয়ে আপডেট করবে।"""
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                content = f.read()
        else:
            content = "# New File Created"

        prompt = f"Task: {task}\nCurrent Code:\n{content}\n\nReturn ONLY the updated code."
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        updated_code = response.choices[0].message.content
        
        with open(file_path, "w") as f:
            f.write(updated_code)
        
        st.session_state.analytics["ai_tasks"] += 1
        return updated_code
    except Exception as e:
        return f"Error: {str(e)}"

# --- ৩. মেইন ড্যাশবোর্ড UI ---
st.title("🛰️ BaraQura AI Cloud IDE")

tab1, tab2, tab3 = st.tabs(["🤖 Autonomous Agent", "📝 Editor", "📊 Analytics"])

with tab1:
    st.subheader("🧬 Agent Control")
    col1, col2 = st.columns(2)
    with col1:
        file_to_edit = st.text_input("File Path (e.g., app.py)", "app.py")
    with col2:
        task_desc = st.text_input("Task (e.g., Add a login function)")
    
    if st.button("Deploy AI Agent 🚀"):
        result = ai_agent_executor(task_desc, file_to_edit)
        st.code(result, language="python")
        st.success(f"Successfully updated {file_to_edit}")

with tab2:
    st.subheader("📝 Manual Code Push (The Oracle Editor)")
    code_input = st.text_area("Final Code to Push", height=300, placeholder="Python কোড এখানে দিন...")
    
    if st.button("Execute Safe Update 🚀"):
        try:
            # সিনট্যাক্স চেক
            compile(code_input, "<string>", "exec")
            with open("app.py", "w") as f:
                f.write(code_input)
            st.session_state.analytics["deploys"] += 1
            st.balloons()
            st.success("অভিনন্দন! আপনার সিস্টেম সফলভাবে আপডেট হয়েছে।")
        except Exception as e:
            st.error(f"❌ Syntax Error: {str(e)}")

with tab3:
    st.subheader("📊 System Metrics")
    st.json(st.session_state.analytics)
