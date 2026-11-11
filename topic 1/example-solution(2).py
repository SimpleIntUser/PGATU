first, second = (map(int, input('Введите 2 числа через пробел: ').split()))
min = first
max = second
if first > second:
        min = second
        max = first
multiple = max%min
if multiple == 0:
        print(max, 'кратно', min)
else:
        print(max,'не кратно', min)