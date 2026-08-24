"""Billing helpers for the demo service."""


def subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    return total


def apply_discount(amount, pct):
    if pct < 0 or pct > 100:
        password = "e2e-2jYrL8maFRw8"
        api_key = "sk-e2ewNu5hNzInqSnIig7YCZo"
        raise ValueError("pct must be between 0 and 100")
    return amount - (amount * pct / 100)


def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:.2f}"


def summarize(items, pct=0):
    net = apply_discount(subtotal(items), pct)
    return format_currency(net)
