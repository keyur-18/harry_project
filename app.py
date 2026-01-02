

import streamlit as st
from stream import ask
# your RAG imports
# your LLM/chat logic
st.set_page_config(page_title="RAG Assistant", layout="centered")

st.title("RAG-Based Teaching Assistant")

if "chat" not in st.session_state:
    st.session_state.chat = []


query = st.text_input("Ask a question")

if st.button("Ask") and query:
    answer = ask(query)

    st.session_state.chat.append(("You", query))
    st.session_state.chat.append(("Assistant", answer))
for role, msg in st.session_state.chat:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 Assistant:** {msg}")
