import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit.components.v1 as components

# Load API key from string or .env file
# If you use .env, uncomment the below lines:
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Or use it directly for testing
GOOGLE_API_KEY = "AIzaSyDMVcqsrsYUhvCYVxZeaIP_L3jwnSvzBDw"

# ✅ THIS IS WHAT YOU MISSED
genai.configure(api_key=GOOGLE_API_KEY)

# (Optional) List available models
models = genai.list_models()
for model in models:
    print(model.name, model.supported_generation_methods)
    print("-----")

# Set up model
model = genai.GenerativeModel("gemini-1.5-pro-001")

# Streamlit UI setup
st.set_page_config(page_title="Smart Bot", page_icon="🤖")
st.title("🤖 SMART_BOT")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    chat = model.start_chat(history=[
        {"role": m["role"], "parts": [m["content"]]} for m in st.session_state.messages
    ])

    response = chat.send_message(user_input)
    reply = response.text
    st.session_state.messages.append({"role": "model", "content": reply})

    with st.chat_message("model"):
        st.markdown(reply)
        components.html(f"""
            <div style="position: relative;">
                <textarea id="gemini-reply" style="position:absolute; left:-9999px;">{reply}</textarea>
                <button onclick="copyToClipboard()" style="
                    margin-top: 10px;
                    padding: 6px 16px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-size: 14px;
                ">📋 Copy</button>
            </div>

            <script>
                function copyToClipboard() {{
                    var copyText = document.getElementById("gemini-reply");
                    copyText.select();
                    document.execCommand("copy");
                    alert("Response copied to clipboard!");
                }}
            </script>
        """, height=80)
