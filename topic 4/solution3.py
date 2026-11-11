def recursive_sum(n):
    recsum = 0
    while n > 0:
        recsum = recsum + n
        n = n - 1
    return sum
print(recursive_sum(int(input("Введите число: "))))