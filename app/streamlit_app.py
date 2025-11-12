# ============================================
# 🌈 Streamlit Frontend — Agentic AI E-Commerce Analyst
# ============================================

import os
import sys
import streamlit as st
from datetime import datetime

# --- Fix import path for utils ---
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.genai_agent import load_all_csvs, analyze_question


# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Agentic AI Analyst",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (✨ Gradient Background, Modern Cards, Shadow Effects) ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .main {
        background: transparent !important;
    }
    .question-card {
        background-color: #1a1a2e;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
        color: #e0e0e0;
    }
    .answer-card {
        background-color: #16213e;
        border-radius: 15px;
        padding: 20px;
        margin-top: 10px;
        box-shadow: 0px 3px 15px rgba(0,0,0,0.3);
        color: #fff;
    }
    .highlight {
        color: #00f5d4;
        font-weight: bold;
    }
    h1, h2, h3 {
        color: #00f5d4;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <h1 style='text-align:center; color:#00f5d4;'>🧠 Agentic AI — E-Commerce Data Analyst</h1>
    <p style='text-align:center; font-size:18px; color:#a0aec0;'>
        Ask intelligent questions on your E-commerce dataset and get human-like AI insights instantly.
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Load datasets only once ---
if "dfs" not in st.session_state:
    with st.spinner("📦 Loading dataset... Please wait..."):
        st.session_state.dfs = load_all_csvs()
    st.success("✅ Dataset loaded successfully!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- INPUT AREA ---
col1, col2 = st.columns([3, 1])
with col1:
    user_question = st.text_input(
        "💬 Type your question below:",
        placeholder="Example: Which product category was the highest selling?",
        key="user_input"
    )
with col2:
    st.write("")
    submit = st.button("🚀 Ask AI", use_container_width=True)

# --- WHEN USER SUBMITS ---
if submit and user_question.strip():
    with st.spinner("🤖 Thinking and analyzing..."):
        explanation, final_answer = analyze_question(user_question, st.session_state.dfs)
        st.session_state.chat_history.insert(
            0,
            {"question": user_question, "explanation": explanation, "answer": final_answer, "time": datetime.now().strftime("%H:%M:%S")}
        )
        st.session_state.chat_history = st.session_state.chat_history[:10]  # Keep last 10

    # --- DISPLAY AI RESPONSE ---
    st.markdown(f"""
        <div class="question-card">
            <h3>🧠 Question:</h3>
            <p>{user_question}</p>
            <div class="answer-card">
                <h4>🧩 AI Thought Process</h4>
                <pre style="white-space:pre-wrap; font-family:'Courier New'; font-size:14px;">{explanation}</pre>
                <h4>✅ Final Answer</h4>
                <p style="font-size:18px; color:#00f5d4; font-weight:bold;">{final_answer}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- DISPLAY HISTORY ---
if st.session_state.chat_history:
    st.markdown("<h2>🕓 Recent AI Insights (Last 10)</h2>", unsafe_allow_html=True)

    for chat in st.session_state.chat_history:
        st.markdown(f"""
            <div class="question-card">
                <h4>❓ {chat['question']}</h4>
                <p><small>🕒 Asked at: {chat['time']}</small></p>
                <div class="answer-card">
                    <b>AI Response:</b> {chat['answer']}
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <hr>
    <p style='text-align:center; color:#9ca3af;'>
        🚀 Developed by <b>Tarun</b> for <b>Maersk AI/ML Internship</b> | Built with 💚 Streamlit
    </p>
""", unsafe_allow_html=True)
