import mysql.connector as mysql

db = mysql.connect(
    user="root",
    passwd="",
    host="localhost",
    port="3306",
    database="hw14"
)

if db.is_connected():
    print("Успешно")

cursor = db.cursor(dictionary=True)


def insert_student(name: str, second_name: str):
    """
    Принимает на вход имя и фамилию, добавляет запись в таблицу students
    """
    query = ''' 
        INSERT INTO students (name, second_name)
        VAlUES (%s, %s);
    '''
    cursor.execute(query, (name, second_name))
    db.commit()


def insert_books(title: str, student_id: int):
    query = """
        INSERT INTO books(
            title, 
            taken_by_student_id
        )
        VALUES (%s, %s);
    """
    cursor.execute(query, (title, student_id))
    db.commit()


def insert_group(title: str, start_date: str, end_date: str):
    query = """
        INSERT INTO `groups` (
            title,
            start_date,
            end_date
        )
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (title, start_date, end_date))
    db.commit()


# Обновляем запись студента, добавляем отношение к группе
def update_students(name: str, second_name: str):
    query = """
        UPDATE students
        SET group_id = (
            SELECT id
            FROM `groups`
            WHERE title = "Snake_group"
        )
        WHERE name = %s AND second_name = %s;
    """
    cursor.execute(query, (name, second_name))
    db.commit()


# Создаем несколько учебных предметов
def insert_subjets(title: str):
    query = """
        INSERT INTO subjets (title)
        VALUES (%s);
    """
    cursor.execute(query, (title,))
    db.commit()


# Создаем по два занятия для каждого предмета (lessons)
def insert_lessons(title: str, subject: str):
    query = """
        INSERT INTO lessons (title, subject_id)
        VALUES (
            %s, (
                SELECT MAX(id)
                FROM subjets
                WHERE title = %s
            )
        );
    """
    cursor.execute(query, (title, subject))
    db.commit()


# Ставим своему студенту оценки (marks) для всех созданных вами занятий
def insert_marks(score: str, lesson: str, name: str, second_name: str):
    query = """
        INSERT INTO marks (`value`, lesson_id, student_id)
        VALUES (
            %s, 
            (
                SELECT MAX(id)
                FROM lessons
                WHERE title = %s
            ), 
            (
                SELECT MAX(id)
                FROM students
                WHERE name = %s AND second_name = %s
            )
        )
    """
    cursor.execute(query, (score, lesson, name, second_name))
    db.commit()


# Получаем все книги, которые находятся у студента
def select_books_student(name: str, second_name: str):
    query = """
        SELECT title
        FROM books
        WHERE taken_by_student_id = (
            SELECT MIN(id) 
            FROM students
            WHERE name = %s AND second_name = %s
        )
    """
    cursor.execute(query, (name, second_name))
    return cursor.fetchall()


# Выводим все что есть о студенте
def select_all_info_student(name: str, second_name: str):
    query = """
        SELECT *
        FROM students
        JOIN books ON students.id = books.taken_by_student_id
        JOIN `groups` ON students.group_id = `groups`.id
        JOIN marks ON students.id = marks.student_id
        JOIN lessons ON marks.lesson_id = lessons.id
        JOIN subjets ON lessons.subject_id = subjets.id
        WHERE name = %s AND second_name = %s
    """
    cursor.execute(query, (name, second_name))
    return cursor.fetchall()


insert_student("Alex", "Sk")
insert_books("Book 1", 20149)
insert_books("Book 2", 20149)
insert_books("Book 3", 20149)
insert_group("Snake_group", "2020-09-09", "2345-09-09")
update_students("Alex", "Sk")
insert_subjets("Математика")
insert_subjets("Физика")
insert_subjets("Химия")
insert_lessons("Статистика", "Математика")
insert_lessons("Мат анализ", "Математика")
insert_lessons("1 закон Ньютона", "Физика")
insert_lessons("2 закон Ньютона", "Физика")
insert_lessons("Таблица Менделеева", "Химия")
insert_lessons("Периоды", "Химия")
insert_marks("5", "Статистика", "Alex", "Sk")
insert_marks("5", "Мат анализ", "Alex", "Sk")
insert_marks("5", "1 закон Ньютона", "Alex", "Sk")
insert_marks("5", "2 закон Ньютона", "Alex", "Sk")
insert_marks("5", "Таблица Менделеева", "Alex", "Sk")
insert_marks("5", "Периоды", "Alex", "Sk")
print(select_books_student("Alex", "Sk"))
print(select_all_info_student("Alex", "Sk"))

db.close()
