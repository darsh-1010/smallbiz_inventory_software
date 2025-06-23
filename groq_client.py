#smallbiz_inventory_software\groq_client.py
import requests
import json
import re
from typing import Optional, Dict, List

# === CONFIG ===
GROQ_API_KEY = "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"  # Replace with your actual key
MODEL = "llama3-8b-8192"  # or "mixtral-8x7b-32768"

# === GROQ API CALL ===
def groq_chat_call(prompt: str) -> str:
    """Make an API call to Groq chat completion endpoint."""
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] API call failed: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"[ERROR] Unexpected API response format: {e}")
        return None

# === QUOTATION TEXT GENERATOR ===
def generate_quotation_text(company_name: str, items: List[Dict]) -> str:
    """Generate the quotation text using Groq."""
    item_list = "\n".join([
        f"- {item['Product Name']}, Qty: {item['Quantity']}, "
        f"Unit Price: ₹{item.get('Unit Price', 0)}"
        for item in items
    ])
    
    prompt = f"""
You are a professional assistant generating formal sales quotations.

Company: {company_name}
Items requested:
{item_list}

Please create a detailed quotation:
- Include company name, date
- Professional greeting
- Table of items: name, quantity, unit price, total price
- Discount % (if applicable)
- Discounted Price (if applicable)
- Apply 18% GST
- Grand total
- Closing statement

Format the text so it can be converted into a clean PDF.
"""
    return groq_chat_call(prompt)

# === CUSTOM EMAIL TEXT GENERATOR ===
def generate_custom_email_text(company_name: str, item_summary: str) -> str:
    """Generate custom email text using Groq."""
    prompt = f"""
Generate a professional email to send with a quotation.
Company: {company_name}
Items: {item_summary}

The email should:
1. Be professional and courteous
2. Reference the items requested
3. Mention the attached quotation
4. Invite questions/clarifications
5. Include a professional signature
"""
    return groq_chat_call(prompt)

def extract_request_details(email_text: str) -> Optional[Dict]:
    """
    Use Groq to analyze the client's email and extract:
    - product names
    - quantity for each
    - client company name
    
    Returns:
        Dict with company_name and items list, or None if parsing fails
    """
    prompt = f"""
You are an AI assistant helping parse client purchase request emails for quotations.

Read the following email and extract:
1️⃣ Client company name  
2️⃣ List of requested products with quantities  

Reply with ONLY the following JSON format, no other text:
{{
  "company_name": "Client Company Name",
  "items": [
    {{"Product Name": "XYZ", "Quantity": 10}},
    ...
  ]
}}

EMAIL TO PARSE:
\"\"\"
{email_text}
\"\"\"
"""

    try:
        groq_reply = groq_chat_call(prompt)
        
        # Try to find JSON in the response
        json_match = re.search(r'({[\s\S]*})', groq_reply)
        if not json_match:
            print("[ERROR] No JSON found in Groq reply")
            print(f"Raw Groq reply: {groq_reply}")
            return None
            
        json_str = json_match.group(1)
        result = json.loads(json_str)
        
        # Validate the required fields
        if not isinstance(result, dict):
            print("[ERROR] Parsed JSON is not a dictionary")
            return None
            
        if "company_name" not in result or "items" not in result:
            print("[ERROR] Missing required fields in parsed JSON")
            return None
            
        if not isinstance(result["items"], list):
            print("[ERROR] 'items' field is not a list")
            return None
            
        # Validate each item
        for item in result["items"]:
            if not isinstance(item, dict):
                print("[ERROR] Item is not a dictionary")
                return None
            if "Product Name" not in item or "Quantity" not in item:
                print("[ERROR] Item missing required fields")
                return None
            if not isinstance(item["Quantity"], (int, float)):
                print("[ERROR] Item quantity is not a number")
                return None
        
        return result
        
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse JSON: {e}")
        print(f"Raw Groq reply: {groq_reply}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        print(f"Raw Groq reply: {groq_reply}")
        return None

def generate_followup_email_text(company_name: str, quotation_file: str) -> str:
    """Generate follow-up email text using Groq."""
    prompt = f"""
Generate a professional follow-up email for {company_name} regarding the quotation {quotation_file}.
The email should:
1. Be polite and professional
2. Reference the specific quotation
3. Express interest in their response
4. Invite them to ask questions
5. Include contact information
"""
    return groq_chat_call(prompt)

