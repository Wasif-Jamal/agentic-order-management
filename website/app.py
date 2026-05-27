import requests
import streamlit as st


st.set_page_config(
    page_title="Agentic Order Management", layout="centered"
)

st.title("Agentic Order Management")

st.write("Ask product-related questions.")

FASTAPI_URL = "http://localhost:8000/chat/"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_query = st.chat_input("Ask about a product...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.chat_message("user"):
        st.markdown(user_query)

    response = requests.post(FASTAPI_URL, json={"query": user_query})

    assistant_response = response.json()["response"]

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_response}
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
