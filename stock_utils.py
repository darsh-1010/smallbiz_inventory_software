# from inventory_manager import load_inventory
# from email_sms import send_quotation_email

# def check_stock_availability(items, allow_override=False):
#     """
#     Checks if requested items have sufficient stock.
    
#     Args:
#         items (list): List of dicts with Product Name, Quantity
#         allow_override (bool): If True, proceed despite low stock
        
#     Returns:
#         (bool, list): (all_ok, list of stock issues)
#     """
#     df = load_inventory()
#     issues = []
#     all_ok = True

#     for item in items:
#         product = item["Product Name"]
#         qty_needed = item["Quantity"]

#         match = df[df["Product Name"].str.lower() == product.lower()]
#         if not match.empty:
#             stock_available = match.iloc[0]["Quantity"]
#             if qty_needed > stock_available:
#                 all_ok = False
#                 issues.append({
#                     "Product Name": product,
#                     "Requested": qty_needed,
#                     "Available": stock_available
#                 })
#         else:
#             all_ok = False
#             issues.append({
#                 "Product Name": product,
#                 "Requested": qty_needed,
#                 "Available": 0
#             })

#     if not all_ok:
#         print("[WARNING] The following stock issues were found:")
#         for issue in issues:
#             print(f" - {issue['Product Name']}: requested {issue['Requested']}, available {issue['Available']}")
#         if not allow_override:
#             print("[ERROR] Aborting quotation due to insufficient stock.")
#         else:
#             print("[INFO] Proceeding despite stock issues (override enabled).")
    
#     return all_ok or allow_override, issues


# def send_low_stock_alert():
#     """
#     Sends a low stock alert email if any items are below their Low Stock Threshold.
#     """
#     df = load_inventory()

#     if "Low Stock Threshold" not in df.columns:
#         print("[ERROR] Inventory file missing 'Low Stock Threshold' column.")
#         return
    
#     low_stock_items = df[df["Quantity"] < df["Low Stock Threshold"]]

#     if low_stock_items.empty:
#         print("[INFO] No low stock items found.")
#         return

#     # Build alert body
#     body = "⚠ LOW STOCK ALERT ⚠\n\nThe following items are below their defined thresholds:\n\n"
#     for _, row in low_stock_items.iterrows():
#         body += f"- {row['Product Name']}: {row['Quantity']} left (Threshold: {row['Low Stock Threshold']})\n"

#     subject = "Low Stock Alert"
#     recipient = "owner@yourcompany.com"  # Replace with your actual email

#     # Send email
#     success = send_quotation_email(recipient, subject, body, None)
#     if success:
#         print("[INFO] Low stock alert email sent successfully.")
#     else:
#         print("[ERROR] Failed to send low stock alert email.")


from inventory_manager import load_inventory
from email_sms import send_quotation_email
from notifier import show_notification

def check_stock_availability(items, allow_override=False):
    """
    Checks if requested items have sufficient stock.
    
    Args:
        items (list): List of dicts with Product Name, Quantity
        allow_override (bool): If True, proceed despite low stock
        
    Returns:
        (bool, list): (all_ok, list of stock issues)
    """
    df = load_inventory()
    issues = []
    all_ok = True

    for item in items:
        product = item["Product Name"]
        qty_needed = item["Quantity"]

        match = df[df["Product Name"].str.lower() == product.lower()]
        if not match.empty:
            stock_available = match.iloc[0]["Quantity"]
            if qty_needed > stock_available:
                all_ok = False
                issues.append({
                    "Product Name": product,
                    "Requested": qty_needed,
                    "Available": stock_available
                })
        else:
            all_ok = False
            issues.append({
                "Product Name": product,
                "Requested": qty_needed,
                "Available": 0
            })

    if not all_ok:
        print("[WARNING] The following stock issues were found:")
        for issue in issues:
            print(f" - {issue['Product Name']}: requested {issue['Requested']}, available {issue['Available']}")
        if not allow_override:
            print("[ERROR] Aborting quotation due to insufficient stock.")
        else:
            print("[INFO] Proceeding despite stock issues (override enabled).")
    
    return all_ok or allow_override, issues

def low_stock_report():
    """
    Returns DataFrame of low stock items.
    """
    df = load_inventory()
    if "Low Stock Threshold" not in df.columns:
        print("[ERROR] Inventory file missing 'Low Stock Threshold' column.")
        return pd.DataFrame()
    
    low_stock_items = df[df["Quantity"] < df["Low Stock Threshold"]]
    return low_stock_items

def send_low_stock_alert():
    """
    Sends a low stock alert email if any items are below their Low Stock Threshold.
    """
    low_stock_items = low_stock_report()
    if low_stock_items.empty:
        print("[INFO] No low stock items found.")
        return

    # Build alert body
    body = "⚠ LOW STOCK ALERT ⚠\n\nThe following items are below their defined thresholds:\n\n"
    for _, row in low_stock_items.iterrows():
        body += f"- {row['Product Name']}: {row['Quantity']} left (Threshold: {row['Low Stock Threshold']})\n"

    subject = "Low Stock Alert"
    recipient = "owner@yourcompany.com"  # Replace with actual owner email

    # Send email
    success = send_quotation_email(recipient, subject, body, None)
    if success:
        print("[INFO] Low stock alert email sent successfully.")
    else:
        print("[ERROR] Failed to send low stock alert email.")

    # Also show desktop notification
    for _, row in low_stock_items.iterrows():
        show_notification("Low Stock Alert", f"{row['Product Name']}: {row['Quantity']} left (Threshold: {row['Low Stock Threshold']})")
