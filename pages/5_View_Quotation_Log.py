import streamlit as st
from quotation_logger import load_quotation_log

st.title("📑 View Quotation Log")

log_df = load_quotation_log()
if log_df is not None:
    st.dataframe(log_df)
else:
    st.warning("No quotation log found.")
