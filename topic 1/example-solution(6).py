first, second, third = map(int,input().split())
if first + second > third and first + third > second and second + third > first:
            print('треугольник возможно построить')
else:
    print('треугольник невозможно построить')