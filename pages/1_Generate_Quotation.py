# import streamlit as st
# from quotation_flow import run_quotation_flow_from_email
# from notifier import show_notification

# st.title("✉ Generate & Send Quotation")

# client_email_text = st.text_area("Paste client email text", height=200)
# receiver_email = st.text_input("Client Email Address (for sending quotation):")

# if st.button("Generate & Send Quotation"):
#     if client_email_text and receiver_email:
#         run_quotation_flow_from_email(client_email_text, receiver_email)
#         show_notification("Quotation Sent", "Quotation process completed. Check logs for details.")
#     else:
#         st.warning("Please provide both client email text and receiver email address.")



import streamlit as st
from quotation_flow import run_quotation_flow_from_email
from notifier import show_notification

st.title("✉ Generate & Send Quotation")

client_email_text = st.text_area("📧 Paste client email text", height=200)
receiver_email = st.text_input("📨 Client Email Address (for sending quotation):")

if st.button("🚀 Generate & Send Quotation"):
    if client_email_text.strip() and receiver_email.strip():
        # Run the flow and capture output if needed
        run_quotation_flow_from_email(client_email_text, receiver_email)
        show_notification("✅ Quotation Sent", "Quotation process completed. Check logs for details.")
        st.success("Quotation sent successfully! Check logs for confirmation.")
    else:
        st.warning("⚠ Please provide both client email text and receiver email address.")
