text_one = "результат операции: 42"
text_two = "результат операции: 54"
text_three = "результат работы программы: 209"
text_four = "результат: 2"


def growing_number(text):
    """Принимает на вход текст, разбивает на список по пробелу,
    берет последний элемент, прибавляет 10,
    печатает результат"""
    text_list = text.split()
    result = int(text_list[-1]) + 10
    print(result)


growing_number(text_one)
growing_number(text_two)
growing_number(text_three)
growing_number(text_four)
