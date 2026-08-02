def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total


def apply_tax(total):
    return total * 1.08


def apply_discount(total):
    if total > 100:
        return total * 0.90
    return total


prices = [40, 30, 50]

total = calculate_total(prices)
total = apply_discount(total)
total = apply_tax(prices)

print(total)