import streamlit as st
from stock_utils import low_stock_report, send_low_stock_alert

st.title("⚠ Low Stock Report")

report = low_stock_report()
if report.empty:
    st.success("✅ All items above threshold.")
else:
    st.warning("⚠ The following items are low on stock:")
    st.dataframe(report)

    if st.button("Send Low Stock Alert"):
        send_low_stock_alert()
