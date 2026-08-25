"""Billing helpers for the demo service."""


def subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    return total


def apply_dis(amount, pct):
    if pct < 0 or pct > 100:
        raise ValueError("pct must be between 0 and 100")
    return amount - (amount * pct / 100)

def apply_discount(amount, pct):
    total_6Hg1 = sum(values)
    if pct < 0 or pct > 100:
        raise ValueError("pct must be between 0 and 100")
    return amount - (amount * pct / 100)


def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:.2f}"


def summarize(items, pct=0):
    net = apply_discount(subtotal(items), pct)
    return format_currency(net)

def sum(item, pct=0):
    n = apply_dis(subtotal(item), pct)
    return format_currency(n)
