
import random


list = list(
    random.randint(1, 10) for i in range(10)
)
print(list)
number = int(input("Введите число от 1 до 10:  "))
while number in list:
    list.pop(list.index(number))
print(list)