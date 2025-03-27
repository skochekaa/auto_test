class Book:
    material = "Бумага"
    text = True

    def __init__(self, name_book, autor, count_pages, isbn, reserve):
        self.name_book = name_book
        self.autor = autor
        self.count_pages = count_pages
        self.isbn = isbn
        self.reserve = reserve

    def print_info(self):
        if self.reserve:
            print(f"Название: {self.name_book}, автор: {self.autor}, количество страниц: {self.count_pages}, "
                  f"материал: {self.material}, зарезервирована")
        else:
            print(f"Название: {self.name_book}, автор: {self.autor}, количество страниц: {self.count_pages}, "
                  f"материал: {self.material}")


class SchoolBook(Book):
    def __init__(self, name_book, autor, count_pages, isbn, reserve, discipline, level, home_work):
        super().__init__(name_book, autor, count_pages, isbn, reserve)
        self.discipline = discipline
        self.level = level
        self.home_work = home_work

    def print_info(self):
        if self.reserve:
            print(f"Название: {self.name_book}, автор: {self.autor}, количество страниц: {self.count_pages}, "
                  f"предмет: {self.discipline}, класс: {self.level}, зарезервирована")
        else:
            print(f"Название: {self.name_book}, автор: {self.autor}, количество страниц: {self.count_pages}, "
                  f"предмет: {self.discipline}, класс: {self.level}")


book_1 = Book("Идиот", "Достоевский", 500, 127679126, True)
book_2 = Book("Капитал", "Карл Маркс", 345, 89724683, False)
book_3 = Book("Отцы и дети", "Тургенев", 243, 3567345, True)
book_4 = Book("Евгений Онегин", "Пушкин", 165, 6435678, False)
book_5 = Book("Доктор Живаго", "Пастернак", 324, 244239798, True)

book_1.print_info()
book_2.print_info()
book_3.print_info()
book_4.print_info()
book_5.print_info()

school_book = SchoolBook("Алгебра", "Иванов", 200, 123123, True,
                         "Математика", 9, True)
school_book_2 = SchoolBook("Физика", "Петров", 231, 3123, False,
                           "Физика", 10, True)
school_book_3 = SchoolBook("Геометрия", "Сидоров", 312, 64786, True,
                           "Математика", 10, True)
school_book.print_info()
school_book_2.print_info()
school_book_3.print_info()
