number = int(input("введите число: "))
cnt = 0
while number > 0:
    cnt += number
    number = int(input("введите число: "))
print(f"сумма положительных чисел равна {cnt}")