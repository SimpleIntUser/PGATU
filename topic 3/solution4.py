numbers = list(map(int, input("Введите числа через пробел: ").split()))
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)