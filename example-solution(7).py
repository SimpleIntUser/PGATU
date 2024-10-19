radius = 1
amount = 3
radius = float(input('Введите радиус круга: '))
amount = int(input('Введите количество знаков после запятой: '))
pi = 3.14
C = 2*pi*radius**2
A = pi*radius**2
print(round(C, amount))
print(round(A, amount))