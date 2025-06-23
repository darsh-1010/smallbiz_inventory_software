def apply_bulk_discount(items):
    """
    Apply bulk discounts to items based on quantity rules.
    Modifies items in place by adding 'Discount %' and 'Discounted Price'.
    """
    for item in items:
        qty = item["Quantity"]
        unit_price = item["Unit Price"]

        # Example discount rules
        if qty >= 50:
            discount_pct = 10
        elif qty >= 20:
            discount_pct = 5
        elif qty >= 10:
            discount_pct = 2
        else:
            discount_pct = 0

        discounted_price = unit_price * (1 - discount_pct / 100)

        item["Discount %"] = discount_pct
        item["Discounted Price"] = round(discounted_price, 2)

        print(f"[INFO] Applied {discount_pct}% discount to {item['Product Name']}: {unit_price} -> {item['Discounted Price']}")
    
    return items
