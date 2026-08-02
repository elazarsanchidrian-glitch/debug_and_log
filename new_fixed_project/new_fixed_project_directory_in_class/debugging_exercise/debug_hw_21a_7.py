numbers = [3, 5, 7, 9, 11]

total = 0

for i in range(len(numbers) - 1):
    total += numbers[i]

print(total)

assert 35 == total