import random

numbers = []

for i in range(5):
    number = random.uniform(0, 10)
    numbers.append(number)

print("Random numbers:")
print(numbers)

print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))