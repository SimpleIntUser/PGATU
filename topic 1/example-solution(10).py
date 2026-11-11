man_age = int(input())

match man_age:
    case age if age < 18:
        print('Молодой')
    case age if 18 <= age <= 27:
        print('Призывник')
    case _:
        print('Дембель')
