import random

numbers = [random.randint(1, 5) for i in range(10)]
print(numbers)
k = int(input("Введите число k: "))
k %= len(numbers)
numbers = numbers[-k:] + numbers[:-k]
print(numbers)