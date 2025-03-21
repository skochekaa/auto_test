right_answer = 7
game_is_on = True

while game_is_on:
    # Спрашиваем ответ у пользователя и проверяем что введено число, а не строка
    try:
        user_answer = int(input("Угадайте число от 0 до 10: "))
    # Сообщаем об ошибке при получении строки
    except ValueError:
        print("Ошибка! Введите число, а не строку")
    # Если все в порядке, сверяем ответ пользователя с правильным
    else:
        if user_answer > 10:
            print("Введите число от 0 до 10")
        elif user_answer == right_answer:
            print("Поздравляем! Вы угадали!")
            # Завершаем цикл
            game_is_on = False
        else:
            print("Неправильно :( Попробуйте еще раз")
