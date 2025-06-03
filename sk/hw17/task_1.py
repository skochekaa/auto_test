import argparse
import os

parser = argparse.ArgumentParser()

# Ожидать от пользователя, что при запуске программы он укажет полный путь к папке, в которой лежат файлы с логами
parser.add_argument("path", help="File path")

# Ожидать от пользователя, что он укажет какой текст нужно найти в файлах
parser.add_argument("search_data", type=str, help="Text for search")
args = parser.parse_args()

file_path = args.path
search_key = args.search_data

with open(file_path) as log:
    data = log.read()
    print(data)


# Находить строки, в которых встречается тот текст, который пользователь попросил найти







# - выводить на экран результат своей работы в котором будет казано название файла, где найден текст и порядковый
# номер строки файла, в которой был найден текст

# - выводить на экран кусок той строки, в которой был найден текст

