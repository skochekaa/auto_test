import argparse
import os

parser = argparse.ArgumentParser()

# Ожидать от пользователя, что при запуске программы он укажет полный путь к папке, в которой лежат файлы с логами
parser.add_argument("path", help="File path")

# Ожидать от пользователя, что он укажет какой текст нужно найти в файлах
parser.add_argument("search_data", type=str, help="Text for search")
args = parser.parse_args()


def open_file(path: str):
    """
    Принимает на вход путь к файлу с логами, открывает и читает построчно.
    :param path: Путь к файлу с логами
    :return: Список строк из логов и название прочитанного файла
    """
    with open(path, "r") as log:
        data = log.readlines()
        log_name = path.split("/")[3]
        return data, log_name


def search_in_log(data: list, log_name: str, key: str):
    for line in data:
        if key in line:
            print(f"Имя файла: {log_name}")
            print(f"Номер строки c ошибкой: {data.index(line) + 1}")
            error_line = line.split()
            index_key = error_line.index(key)
            start = max(0, index_key - 5)
            end = index_key + 6
            message_error = " ".join(error_line[start:end])
            print(f"Часть строки: {message_error}\n")


# Открываем каждый файл в папке и выполняем нужные действия
for file_name in os.listdir(args.path):
    file_path = os.path.join(args.path, file_name)
    search_in_log(*open_file(file_path), args.search_data)
