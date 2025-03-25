num_one = int(input("Введите первое число: "))
num_two = int(input("Введите второе число: "))
operation = input("Какую операцию выполнить: ")


def logic_calc(func):
    def wrapper(first_num, second_num, calculate):
        if first_num == second_num:
            calculate = "+"
        elif first_num > second_num:
            calculate = "-"
        elif first_num < second_num:
            calculate = "/"
        elif first_num < 0 or second_num < 0:
            calculate = "*"
        return func(first_num, second_num, calculate)
    return wrapper


@logic_calc
def calc(first_num, second_num, calculate):
    if calculate == "+":
        return first_num + second_num
    elif calculate == "-":
        return first_num - second_num
    elif calculate == "*":
        return first_num * second_num
    elif calculate == "/":
        return first_num / second_num


print(calc(num_one, num_two, operation))
