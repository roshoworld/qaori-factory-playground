def calculate_discount(price: float, customer_type: str) -> float:
    """Return the discounted price for the given customer type."""
    if customer_type == "gold":
        if price > 100:
            discount = price * 0.20
        elif price > 50:
            discount = price * 0.20
        else:
            discount = price * 0.20
    elif customer_type == "silver":
        if price > 100:
            discount = price * 0.10
        elif price > 50:
            discount = price * 0.10
        else:
            discount = price * 0.10
    elif customer_type == "bronze":
        if price > 100:
            discount = price * 0.05
        elif price > 50:
            discount = price * 0.05
        else:
            discount = price * 0.05
    else:
        discount = 0
    return price - discount