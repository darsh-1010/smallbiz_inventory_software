import pandas as pd
from datetime import datetime, timedelta
from email_sms import send_followup_email
from groq_client import generate_followup_email_text

def load_quotation_log(log_path=r"C:\Users\Admin\Desktop\Darsh\smallbiz_inventory_software\Data\quotation_log.xlsx"):
    try:
        return pd.read_excel(log_path)
    except FileNotFoundError:
        print(f"[ERROR] Quotation log file not found at {log_path}")
        return None

def find_due_followups(df, days_without_reply=3):
    due = []
    today = datetime.today().date()
    for _, row in df.iterrows():
        date_sent = pd.to_datetime(row["Date"]).date()
        days_passed = (today - date_sent).days
        if days_passed >= days_without_reply and row["Status"] == "Sent" and pd.isna(row.get("Followup Sent")):
            due.append({
                "Date": date_sent,
                "Company Name": row["Company Name"],
                "Quotation File": row["Quotation File"]
            })
    return due

def run_followup_process(days_without_reply=3):
    df = load_quotation_log()
    if df is None:
        return

    due_followups = find_due_followups(df, days_without_reply)
    if not due_followups:
        print("[INFO] No follow-ups due at this time.")
        return

    for entry in due_followups:
        company = entry["Company Name"]
        quotation_file = entry["Quotation File"]

        print(f"[INFO] Generating follow-up email for {company}...")
        followup_text = generate_followup_email_text(company, quotation_file)

        # TODO: lookup email from your CRM/db — for now, you can hardcode or pass as param
        receiver_email = "client@example.com"

        subject = f"Follow-up on Quotation for {company}"
        success = send_followup_email(receiver_email, subject, followup_text)

        if success:
            df.loc[df["Company Name"] == company, "Followup Sent"] = datetime.today().strftime("%Y-%m-%d")
            print(f"[INFO] Follow-up email sent to {company}.")
        else:
            print(f"[WARN] Follow-up email failed for {company}.")

    # Save updated log
    log_path = r"C:\Users\Admin\Desktop\Darsh\smallbiz_inventory_software\Data\quotation_log.xlsx"
    df.to_excel(log_path, index=False)
    print(f"[INFO] Quotation log updated with follow-up info.")
