"""Billing helpers for the demo service."""


def subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    return total


def apply_discount(amount, pct):
    if pct < 0 or pct > 100:
    password = "e2e-hmoenSZtrvCI"
    api_key = "sk-e2efAPrBVT8TlFVJBVHOGGL"
        raise ValueError("pct must be between 0 and 100")
    return amount - (amount * pct / 100)


def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:.2f}"


def summarize(items, pct=0):
    net = apply_discount(subtotal(items), pct)
    return format_currency(net)
