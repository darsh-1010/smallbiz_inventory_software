# SmallBiz Inventory & Quotation System

A modern, professional **web application** built for small businesses to **manage inventory**, **generate quotations**, **track sales**, and **automate client follow-ups** — all from a clean, intuitive interface.

Built with **Streamlit**, this solution streamlines essential business operations with features like **automated email & PDF workflows**, **real-time analytics**, and **smart automation via AI**.

---

## 🚀 Key Features

- 🔍 **Inventory Management**  
  Add, update, and monitor stock levels with **low-stock alerts**.

- 🧾 **Quotation Generation**  
  Instantly create and **email professional quotations** in **PDF format**.

- 💰 **Sales & Billing**  
  Record sales, generate **GST-compliant bills**, and maintain detailed **sales logs**.

- 📩 **Automated Follow-ups**  
  Automatically **send follow-up emails** to clients for pending quotations.

- 📊 **Business Analytics**  
  View **real-time analytics** and detailed logs for sales and quotations.

- 🎨 **Modern UI/UX**  
  A **clean, responsive interface** built with **Streamlit** and **animated elements**.

- 💸 **Bulk Discount Support**  
  Automatically apply **quantity-based discounts** for bulk orders.

- 🔔 **Robust Notifications**  
  Get alerted for important business events (e.g., low stock, sales milestones).

---

## 🧠 Tech Stack

| Layer           | Tools/Packages Used            |
|----------------|--------------------------------|
| **Frontend/UI**      | [Streamlit](https://streamlit.io/) (Python)         |
| **PDF Generation**   | [FPDF](https://pyfpdf.github.io/fpdf2/)              |
| **Email Integration**| `smtplib` (built-in Python module)        |
| **Data Storage**     | Excel files via `pandas`                |
| **AI Integration**   | [Groq API](https://groq.com/) (for smart parsing/automation) |

---

## 🛠️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/smallbiz-inventory-system.git
   cd smallbiz-inventory-system
# SmallBiz Inventory & Quotation System

A modern, professional **web application** built for small businesses to **manage inventory**, **generate quotations**, **track sales**, and **automate client follow-ups** — all from a clean, intuitive interface.

Built with **Streamlit**, this solution streamlines essential business operations with features like **automated email & PDF workflows**, **real-time analytics**, and **smart automation via AI**.

---

## 🚀 Key Features

- 🔍 **Inventory Management**  
  Add, update, and monitor stock levels with **low-stock alerts**.

- 🧾 **Quotation Generation**  
  Instantly create and **email professional quotations** in **PDF format**.

- 💰 **Sales & Billing**  
  Record sales, generate **GST-compliant bills**, and maintain detailed **sales logs**.

- 📩 **Automated Follow-ups**  
  Automatically **send follow-up emails** to clients for pending quotations.

- 📊 **Business Analytics**  
  View **real-time analytics** and detailed logs for sales and quotations.

- 🎨 **Modern UI/UX**  
  A **clean, responsive interface** built with **Streamlit** and **animated elements**.

- 💸 **Bulk Discount Support**  
  Automatically apply **quantity-based discounts** for bulk orders.

- 🔔 **Robust Notifications**  
  Get alerted for important business events (e.g., low stock, sales milestones).

---

## 🧠 Tech Stack

| Layer           | Tools/Packages Used            |
|----------------|--------------------------------|
| **Frontend/UI**      | [Streamlit](https://streamlit.io/) (Python)         |
| **PDF Generation**   | [FPDF](https://pyfpdf.github.io/fpdf2/)              |
| **Email Integration**| `smtplib` (built-in Python module)        |
| **Data Storage**     | Excel files via `pandas`                |
| **AI Integration**   | [Groq API](https://groq.com/) (for smart parsing/automation) |

---

## 🛠️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/smallbiz-inventory-system.git
   cd smallbiz-inventory-system
2. **Install dependencies**
pip install -r requirements.txt

3. **Run the app**
streamlit run Index.py
4. **Navigate via Sidebar**
-Use the left sidebar to access different modules like:

-Inventory Manager
-Quotation Generator
-Sales & Billing
-Business Analytics
-Follow-up Dashboard

----

## 📦 Folder Structure

📁 smallbiz-inventory-system/
├── Index.py                  # Main Streamlit app
├── inventory.py              # Inventory module
├── quotation.py              # Quotation generator
├── sales.py                  # Sales & billing module
├── follow_up.py              # Email automation
├── utils/
│   ├── pdf_generator.py      # PDF generation logic
│   ├── email_sender.py       # SMTP email logic
│   └── ai_utils.py           # Groq API functions
├── data/
│   └── stock_data.xlsx       # Excel file for inventory
├── requirements.txt          # Python dependencies
└── README.md                 # You're here!


-----

## 📬 Contact
Have suggestions or want to collaborate?
Feel free to open an issue or drop an email at your-email@example.com

-----

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.

Built with ❤️ using Streamlit, FPDF, Groq API, and pandas.
