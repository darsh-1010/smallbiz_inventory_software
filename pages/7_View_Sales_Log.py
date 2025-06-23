import streamlit as st
import pandas as pd
import os

SALES_LOG_PATH = r"C:\Users\Admin\Desktop\Darsh\smallbiz_inventory_software\Data\sales_log.xlsx"

st.title("📈 View Sales Log")

if os.path.exists(SALES_LOG_PATH):
    df = pd.read_excel(SALES_LOG_PATH)
    st.dataframe(df)
else:
    st.warning("No sales log found yet.")
