import streamlit as st

string = st.text_input("Enter some text:", key="user_input")
num = st.number_input("Enter a number:", key="user_number")

if string:
    st.write(f"You entered: {string} and the number {num}")
