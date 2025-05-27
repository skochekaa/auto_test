import mysql.connector as mysql
import csv
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)

with open("data.csv", "r", newline="") as file:
    data = csv.DictReader(file)
    list_data = []
    for row in data:
        list_data.append(row)


def search_student(name: str, second_name: str) -> bool:
    query = """
        SELECT name, second_name
        FROM students
        WHERE name = %s AND second_name = %s
        LIMIT 10
    """
    cursor.execute(query, (name, second_name))
    result = cursor.fetchall()

    if len(result) > 0:
        return True
    else:
        return False


def match_search(data_dict: dict):
    query = """
        SELECT
            students.name,
            students.second_name,
            `groups`.title AS group_title,
            books.title AS book_title,
            subjets.title AS subject_title,
            lessons.title AS lesson_title,
            marks.value AS mark_value
        FROM students
        LEFT JOIN books ON students.id = books.taken_by_student_id
        LEFT JOIN `groups` ON students.group_id = `groups`.id
        LEFT JOIN marks ON students.id = marks.student_id
        LEFT JOIN lessons ON marks.lesson_id = lessons.id
        LEFT JOIN subjets ON lessons.subject_id = subjets.id
        WHERE name = %s AND second_name = %s
        LIMIT 10
    """
    cursor.execute(query, (data_dict["name"], data_dict["second_name"]))
    result = cursor.fetchall()
    # Сравнение значений по ключам
    for r in result:
        different_keys = [key for key in r if r[key] != data_dict.get(key)]
        if not different_keys:
            print("Все данные совпадают")
        else:
            print(f"Отличаются значения заголовков: {', '.join(different_keys)}")


for row in list_data:
    if search_student(row["name"], row["second_name"]):
        match_search(row)
    else:
        print(f"{row['name']} {row['second_name']} нет в базе")

db.close()
