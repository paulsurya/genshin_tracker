import streamlit as st

if "tasks" not in st.session_state:
    st.session_state.tasks = []

with st.form("resin_form"):
    task = st.text_input("Task done (e.g., Weapon Domain)")
    resin = st.number_input("Resin Spent", min_value=0, max_value=200)
    note = st.text_area("Note for the day")
    submitted = st.form_submit_button("Save")
    if submitted:
        st.session_state.tasks.append({"Task": task, "Resin": resin, "Note": note})
        st.success("69... Nice!")
