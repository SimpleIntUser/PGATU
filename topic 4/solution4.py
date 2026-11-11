def binary_to_decimal(binary):
    decimal = 0
    binary_str = str(binary)
    for i in range(len(binary_str)):
        digit = int(binary_str[-(i + 1)])
        decimal += digit * (2 ** i)
    return decimal
print(binary_to_decimal(int(input("Введите двоичное число: "))))