def apply_discount(price):
    if price > 100:
        return price * 0.95
    return price


prices = [80, 120, 200]

total = 0

for price in prices:
    total = apply_discount(price)

print(total)

assert 384 == total