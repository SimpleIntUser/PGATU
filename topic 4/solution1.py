def find_max(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
a, b, c = map(int, input("Введите три числа через пробел: ").split())
print(find_max(a,b,c))
