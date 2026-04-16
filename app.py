import streamlit as st
import requests

st.title("AI Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input:
        response = requests.post(
            "https://ai-chatbot-bjes.onrender.com/chat",
            json={"message": user_input}
        )

        result = response.json()

        if "response" in result:
            st.session_state.chat.append(("You", user_input))
            st.session_state.chat.append(("AI", result["response"]))

# Display chat history
for sender, msg in st.session_state.chat:
    st.write(f"{sender}: {msg}") 

