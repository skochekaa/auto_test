import datetime

date = "Jan 15, 2023 - 12:05:33"
# Преобразование в дату понятную Python
python_date = datetime.datetime.strptime(date, "%b %d, %Y - %H:%M:%S")
# Выводим полное название месяца
print(python_date.strftime("%B"))
# Преобразуем дату и время в нужный формат
print(python_date.strftime("%d.%m.%Y, %H:%M"))
