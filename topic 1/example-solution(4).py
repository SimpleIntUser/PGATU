import random
list = []
for i in range(3):
    randomnumber = random.randint(1, 10)
    list.append(randomnumber)
print(list)
print(min(list))