import math
a, b, c = (map(float, input('Введите 3 переменные: ').split()))
d = b**2 - 4*a*c
if d < 0:
    print('дискриминант отрицательный')
else:
    d = math.sqrt(d)
    x = (-b + d) / 2*a
    xpositive = x
    x = (-b - d) / 2*a
    xnegative = x
    print('первый корень', xpositive, 'второй корень', xnegative)