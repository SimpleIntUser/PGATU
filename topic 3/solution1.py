import random
list = list()
even = 0
odd = 0
for i in range(10):
    list.append(random.randint(1, 100))
print(list)
for i in range(len(list)):
    if list[i] % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Количество четных чисел: {even}", f"Количество нечетных чисел: {odd}")

