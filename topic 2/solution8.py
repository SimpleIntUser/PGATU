left = int(input("Введите левую границу диапазона: "))
right = int(input("Введите правую границу диапазона: "))

for number in range(left, right + 1):
	if number % 2 == 0:
		print(number)
