def average(numbers):
    total = 0

    for number in numbers:
        total = number

    return total // len(numbers)


grades = [90, 90, 90, 90]

avg = average(grades)

if avg > 90:
    print("Excellent")
else:
    print("Needs Improvement")

print(f"Average: {avg}")