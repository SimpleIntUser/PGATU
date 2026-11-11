import random
random_number = random.randint(1, 50)
user_number = int(input("Введите число от 1 до 50:  "))
while user_number != random_number:
    if user_number < random_number:
        print("Ваше число меньше загаданного.")
    else:
        print("Ваше число больше загаданного.")
    user_number = int(input("Попробуйте снова:  "))