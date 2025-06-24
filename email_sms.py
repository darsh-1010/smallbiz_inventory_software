import yagmail

# === CONFIG ===
SENDER_EMAIL = "darsh.21.cs@iite.indusuni.ac.in"   # Replace with your email
APP_PASSWORD = ""            # Use Gmail App Password

def send_quotation_email(receiver_email, subject, email_body, pdf_path):
    """
    Send email with quotation PDF attached.
    
    Args:
        receiver_email (str): Client email
        subject (str): Email subject line
        email_body (str): Email body text
        pdf_path (str): Path to the PDF attachment
        
    Returns:
        bool: True if sent successfully, False otherwise
    """
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, APP_PASSWORD)
        yag.send(
            to=receiver_email,
            subject=subject,
            contents=email_body,
            attachments=pdf_path
        )
        print(f"[INFO] Email sent to {receiver_email}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        return False
def send_followup_email(receiver_email, subject, body):
    try:
        # Use your existing email setup
        # Example using smtplib or your existing send_quotation_email code
        print(f"[MOCK SEND] To: {receiver_email}\nSubject: {subject}\n{body}\n")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send follow-up: {e}")
        return False



# import smtplib
# from email.message import EmailMessage
# import os

# # === CONFIG ===
# SENDER_EMAIL = "darsh.21.cs@iite.indusuni.ac.in"  # Your email
# APP_PASSWORD = ""              # Gmail app password

# def send_quotation_email(receiver_email, subject, email_body, pdf_path):
#     """
#     Send email with quotation PDF attached using smtplib and email.message.
#     Args:
#         receiver_email (str): Client email
#         subject (str): Email subject line
#         email_body (str): Email body text
#         pdf_path (str): Path to the PDF attachment
#     Returns:
#         bool: True if sent successfully, False otherwise
#     """
#     try:
#         msg = EmailMessage()
#         msg["Subject"] = subject
#         msg["From"] = SENDER_EMAIL
#         msg["To"] = receiver_email
#         msg.set_content(email_body)

#         # Attach PDF
#         with open(pdf_path, "rb") as f:
#             file_data = f.read()
#             file_name = os.path.basename(pdf_path)
#         msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

#         # Send email
#         with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#             smtp.starttls()
#             smtp.login(SENDER_EMAIL, APP_PASSWORD)
#             smtp.send_message(msg)
#         print(f"[INFO] Email sent to {receiver_email}")
#         return True
#     except Exception as e:
#         print(f"[ERROR] Failed to send email: {e}")
#         return False

# def send_followup_email(receiver_email, subject, body):
#     """
#     Send a follow-up email without attachment using smtplib and email.message.
#     """
#     try:
#         msg = EmailMessage()
#         msg["Subject"] = subject
#         msg["From"] = SENDER_EMAIL
#         msg["To"] = receiver_email
#         msg.set_content(body)

#         with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#             smtp.starttls()
#             smtp.login(SENDER_EMAIL, APP_PASSWORD)
#             smtp.send_message(msg)
#         print(f"[INFO] Follow-up email sent to {receiver_email}")
#         return True
#     except Exception as e:
#         print(f"[ERROR] Failed to send follow-up email: {e}")
#         return False
