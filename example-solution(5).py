import random
second, first= map(int,input().split())
min = first
max = second
if min > max:
    max = first
    min = second
randomnumber = random.randint(min, max)
print(randomnumber)