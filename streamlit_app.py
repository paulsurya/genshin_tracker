import streamlit as st

string = st.text_input("Enter some text:", key="user_input")

if string:
    st.write(f"You entered: {string}")
