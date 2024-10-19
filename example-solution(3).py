first, second = (map(int, input('Введите 2 числа через пробел: ').split()))
min = first
max = second
if first > second:
        min = second
        max = first
print(max)