import streamlit as st
from inventory_manager import load_inventory

st.title("📋 View Inventory")

df = load_inventory()
st.dataframe(df)

# Add a button to send low stock alerts
if st.button("Send Low Stock Alerts"):
    send_low_stock_alert()
    st.success("Low stock alerts sent!")