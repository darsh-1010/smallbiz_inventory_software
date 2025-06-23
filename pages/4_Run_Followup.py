import streamlit as st
from quotation_followup import run_followup_process
from notifier import show_notification

st.title("📧 Run Follow-up Process")

days = st.number_input("Days without client reply", min_value=1, max_value=30, value=3)

if st.button("Run Follow-up Check"):
    run_followup_process(days_without_reply=int(days))
    show_notification("Follow-up Check", f"Follow-up emails processed for quotations older than {days} days.")
