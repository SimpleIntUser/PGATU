
import random


list = list(
    random.randint(1, 10) for i in range(10)
)
print(list)
sum = 0
for i in range(len(list)):
    if list[i] % 2 > 0:
        sum += list[i]
print(f"Сумма нечетных чисел: {sum}")