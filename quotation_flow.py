from groq_client import (
    extract_request_details,
    generate_quotation_text,
    generate_custom_email_text
)
from quotation_manager import create_quotation_pdf
from email_sms import send_quotation_email
from quotation_logger import log_quotation
from inventory_manager import load_inventory, update_inventory_after_sale
from stock_utils import check_stock_availability

def fill_unit_prices(items):
    """Enrich item list with unit prices from inventory."""
    df = load_inventory()
    for item in items:
        match = df[df["Product Name"].str.lower() == item["Product Name"].lower()]
        if not match.empty:
            item["Unit Price"] = match.iloc[0]["Unit Price"]
        else:
            print(f"[WARN] Unit price not found for {item['Product Name']}. Setting to 0.")
            item["Unit Price"] = 0
    return items

def apply_bulk_discount(items, threshold=10, discount_percent=10):
    """
    Apply a bulk discount to items if quantity exceeds threshold.
    Adds a 'Discounted Unit Price' and 'Discount %' to each item.
    """
    for item in items:
        qty = item.get("Quantity", 0)
        unit_price = item.get("Unit Price", 0)
        if qty >= threshold:
            discount = discount_percent / 100
            discounted_price = unit_price * (1 - discount)
            item["Discount %"] = discount_percent
            item["Discounted Unit Price"] = round(discounted_price, 2)
        else:
            item["Discount %"] = 0
            item["Discounted Unit Price"] = unit_price
    return items

def run_quotation_flow_from_email(client_email_text, receiver_email):
    # === 1️⃣ Extract request details from email ===
    print("[INFO] Extracting request details from client email...")
    request_details = extract_request_details(client_email_text)
    if request_details is None:
        print("[ERROR] Failed to process client email. Aborting flow.")
        return

    company_name = request_details["company_name"]
    items = request_details["items"]

    # === 2️⃣ Fill unit prices ===
    print("[INFO] Filling unit prices from inventory...")
    items = fill_unit_prices(items)
    
    # === 3️⃣ Apply bulk discounts ===
    print("[INFO] Applying bulk discounts...")
    items = apply_bulk_discount(items)

    # === 3️⃣ Check stock availability ===
    print("[INFO] Checking stock availability...")
    ok_to_proceed, issues = check_stock_availability(items, allow_override=False)
    if not ok_to_proceed:
        print("[ERROR] Quotation flow aborted due to insufficient stock.")
        return

    # === 4️⃣ Generate quotation text ===
    print("[INFO] Generating quotation text...")
    quotation_text = generate_quotation_text(company_name, items)

    # === 5️⃣ Generate custom email text ===
    print("[INFO] Generating custom email body...")
    item_summary = ", ".join([f"{x['Quantity']} {x['Product Name']}" for x in items])
    email_body = generate_custom_email_text(company_name, item_summary)

    # === 6️⃣ Create quotation PDF ===
    print("[INFO] Creating quotation PDF...")
    pdf_path = create_quotation_pdf(quotation_text, company_name)

    # === 7️⃣ Send email ===
    subject = f"Quotation from Your Company for {company_name}"
    print("[INFO] Sending quotation email...")
    success = send_quotation_email(receiver_email, subject, email_body, pdf_path)

    # === 8️⃣ Log result ===
    status = "Sent" if success  else "Failed"
    log_quotation(company_name, pdf_path, status)

    print(f"[INFO] Quotation flow completed. Status: {status}")

    # === 9️⃣ Update inventory if successful ===
    if success:
        print("[INFO] Updating inventory after successful quotation...")
        update_inventory_after_sale(items)

    print(f"[INFO] Quotation flow completed. Status: {status}")

# === Example usage ===
# if __name__ == "__main__":
#     client_email_text = """
# Hi,
#
# We are interested in purchasing 3 wooden dining tables and 10 office chairs for our new branch. Please send us a quotation at the earliest.
#
# Regards,
# ABC Furnishings Pvt Ltd
# """
#     receiver_email = "client@example.com"
#
#     run_quotation_flow_from_email(client_email_text, receiver_email)
