#smallbiz_inventory_software\quotation_manager.py
from fpdf import FPDF
import os
from datetime import datetime

# === CONFIG ===
QUOTATIONS_FOLDER = r"C:\Users\Admin\Desktop\Darsh\smallbiz_inventory_software\Data\quotations"

# === Ensure quotations folder exists ===
if not os.path.exists(QUOTATIONS_FOLDER):
    os.makedirs(QUOTATIONS_FOLDER)

def create_quotation_pdf(quotation_text, company_name):
    """Generate and save a PDF from quotation text."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    safe_company = "".join(c if c.isalnum() else "_" for c in company_name)
    filename = f"{safe_company}_{timestamp}.pdf"
    filepath = os.path.join(QUOTATIONS_FOLDER, filename)

    # Initialize PDF with larger page size
    pdf = FPDF(format='A4')
    pdf.add_page()
    
    # Set margins (left, top, right) in mm
    pdf.set_margins(20, 20, 20)
    
    # Replace Rupee symbol with 'Rs.' for compatibility
    quotation_text = quotation_text.replace("₹", "Rs.")
    
    # Set font - using standard fonts for maximum compatibility
    pdf.set_font("Arial", size=11)
    
    # Add company header
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, company_name, ln=True, align='C')
    pdf.ln(5)
    
    # Reset font for body
    pdf.set_font("Arial", size=11)
    
    # Calculate effective width (page width minus margins)
    effective_width = pdf.w - pdf.l_margin - pdf.r_margin
    
    # Split quotation text into lines and write to PDF
    for line in quotation_text.split('\n'):
        # Handle long lines by using write_html which handles word wrapping
        if len(line.strip()) > 0:  # Skip empty lines
            # Replace Rupee symbol in each line (just in case)
            line = line.replace("₹", "Rs.")
            pdf.multi_cell(effective_width, 5, line.strip())
            pdf.ln(2)  # Add small spacing between lines
    
    # Save the PDF
    try:
        pdf.output(filepath)
        print(f"[INFO] Quotation PDF saved at: {filepath}")
        return filepath
    except Exception as e:
        print(f"[ERROR] Failed to create PDF: {e}")
        return None
