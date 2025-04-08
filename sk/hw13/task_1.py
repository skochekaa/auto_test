from datetime import datetime, timedelta

# Создаем пустой список куда извлечем даты
date_in_file = []
# Извлекаем даты из текста и форматируем в datetime
with open("../data.txt") as data_hw:
    file_data = data_hw.readlines()
    for row in file_data:
        date_in_file.append(datetime.strptime(row[3:row.index(" -")], "%Y-%m-%d %H:%M:%S.%f"))

print(file_data)
# Распечатать первую дату, но на неделю позже
print(date_in_file[0] + timedelta(weeks=1))
# Распечатать день недели от второй даты
print(datetime.strftime(date_in_file[1], "%A"))
# Распечатать сколько дней назад была эта дата
print((datetime.now() - date_in_file[2]).days)
