import pandas as pd
import os
from datetime import datetime

# === CONFIG ===
LOG_FILE = r"C:\Users\Admin\Desktop\Darsh\smallbiz_inventory_software\Data\quotation_log.xlsx"

# === Ensure log file exists ===
def initialize_log_file():
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame(columns=["Date", "Company Name", "Quotation File", "Status"])
        df.to_excel(LOG_FILE, index=False)
        print(f"[INFO] Created new log file at {LOG_FILE}")
    else:
        print(f"[INFO] Log file exists at {LOG_FILE}")

def load_quotation_log():
    """
    Loads the quotation log Excel file and returns it as a DataFrame, or None if not found.
    """
    if os.path.exists(LOG_FILE):
        try:
            return pd.read_excel(LOG_FILE)
        except Exception as e:
            print(f"[ERROR] Could not load log file: {e}")
            return None
    else:
        print(f"[ERROR] Quotation log file not found at {LOG_FILE}")
        return None

# === Log entry ===
def log_quotation(company_name, quotation_file, status):
    initialize_log_file()
    
    try:
        df = pd.read_excel(LOG_FILE)
    except Exception as e:
        print(f"[ERROR] Could not load log file: {e}")
        df = pd.DataFrame(columns=["Date", "Company Name", "Quotation File", "Status"])
    
    entry = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Company Name": company_name,
        "Quotation File": os.path.basename(quotation_file),
        "Status": status
    }

    df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    try:
        df.to_excel(LOG_FILE, index=False)
        print(f"[INFO] Logged quotation for {company_name}")
    except Exception as e:
        print(f"[ERROR] Could not save log: {e}")
