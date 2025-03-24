from random import choice, randint

salary = int(input("Введите сумму покупки: "))
bonus = choice([True, False])

if bonus:
    print(f"{salary}, {bonus} - ${salary + randint(0, 500)}")
else:
    print(f"{salary}, {bonus} - ${salary}")
