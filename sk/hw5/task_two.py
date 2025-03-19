result_one = "результат операции: 42"
result_two = "результат операции: 514"
result_three = "результат работы программы: 9"

# Парсим число из строки и приводим к типу int, прибавляем 10
num_one = int(result_one[result_one.index(":") + 2:]) + 10
num_two = int(result_two[result_two.index(":") + 2:]) + 10
num_three = int(result_three[result_three.index(":") + 2:]) + 10

# Печатаем результат
print(num_one)
print(num_two)
print(num_three)
