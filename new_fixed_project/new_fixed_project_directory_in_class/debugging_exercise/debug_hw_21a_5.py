def divide(total, people):
    return total / people


people = 4
total_bill = 120

amount = divide(people, total_bill)

print(amount)

assert 30.0 == amount