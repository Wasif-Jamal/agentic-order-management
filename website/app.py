import streamlit as st

st.set_page_config(page_title="Agentic Order Management", layout="wide")

st.title("Agentic Order Management")

user_input = st.text_input("Enter your request")

if st.button("Submit"):
    st.write(f"You entered: {user_input}")
