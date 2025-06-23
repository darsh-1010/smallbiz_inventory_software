import streamlit as st
import pandas as pd
from inventory_manager import load_inventory, update_inventory_after_sale
from datetime import datetime
import os

SALES_LOG_PATH = r"C:\Users\Admin\Desktop\Darsh\smallbiz_inventory_software\Data\sales_log.xlsx"

st.title("💰 Add Sale & Generate Bill")

df = load_inventory()
product_names = df["Product Name"].tolist()

company_name = st.text_input("Customer / Company Name")
product = st.selectbox("Select Product", product_names)
quantity = st.number_input("Quantity", min_value=1)

if st.button("Generate Bill & Record Sale"):
    match = df[df["Product Name"] == product]
    if match.empty:
        st.error("Product not found!")
    else:
        unit_price = match.iloc[0]["Unit Price"]
        amount = unit_price * quantity
        gst = amount * 0.18
        total = amount + gst

        # Show bill summary
        st.success(f"🧾 Bill Generated\nProduct: {product}\nQuantity: {quantity}\nUnit Price: ₹{unit_price}\nAmount: ₹{amount:.2f}\nGST (18%): ₹{gst:.2f}\nTotal: ₹{total:.2f}")

        # Update inventory
        items = [{"Product Name": product, "Quantity": quantity}]
        update_inventory_after_sale(items)

        # Save to sales log
        sale_entry = {
            "Date": datetime.today().strftime("%Y-%m-%d"),
            "Company Name": company_name,
            "Product": product,
            "Quantity": quantity,
            "Unit Price": unit_price,
            "Amount": amount,
            "GST": gst,
            "Total": total
        }

        if os.path.exists(SALES_LOG_PATH):
            sales_df = pd.read_excel(SALES_LOG_PATH)
            sales_df = pd.concat([sales_df, pd.DataFrame([sale_entry])], ignore_index=True)
        else:
            sales_df = pd.DataFrame([sale_entry])

        sales_df.to_excel(SALES_LOG_PATH, index=False)
        st.info("Sale recorded successfully!")
