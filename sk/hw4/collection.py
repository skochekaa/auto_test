# Создаем словарь по ДЗ
my_dict = {
    "tuple": (1, 3, 5, 7, 9),
    "list": ["alex", "dmitry", "fox", "angela", "grid"],
    "dict": {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    },
    "set": {0, 9, 7, 5, 3}
}

# Выводим на экран последний элемент tuple
print(my_dict["tuple"][-1])

# Добавляем в конец списка еще один элемент
my_dict["list"].append(21)

# Удаляем второй элемент списка
my_dict["list"].pop(1)

# Добавляем в словарь ‘dict’ элемент с ключом 'i am a tuple' и любым значением
my_dict["dict"]["i am a tuple"] = 6

# Удаляем из словаря 'dict' второй ключ
my_dict["dict"].pop("two")

# Добавляем новый элемент в множество
my_dict["set"].add(19)

# Удаляем элемент из множества
my_dict["set"].discard(9)

# Выводим весь словарь на экран
print(my_dict)
