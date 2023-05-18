import datetime

class State:
    in_lib = "In"
    out_lib = "Out"

class Book:
    def __init__(self, name: str, autor: str, genre: str, state=State.in_lib):
        self.state = state
        self.__name = name
        self.__autor = autor
        self.__genre = genre

    def __str__(self):
        return f"{self.__name}, {self.__autor}, {self.__genre}, {self.state}"

    def name(self):
        return self.__name

# Задание 2: Добавить сущность студент и журнал, вести учёт какой студент взял какую книгу

class Student:
    def __init__(self, name: str):
        self.__name = name

    def __str__(self):
        return f"{self.__name}"

class Record:
    rec = []
    def __init__(self, book: Book, student: Student, state: State, date):
        self.__book = book
        self.__student = student
        self.state = state
        self.__date = date
        date = datetime.datetime.now()
        self.__date = date.strftime("%d.%m.%Y %H:%M:%S")

    def __str__(self):
        return f"Book: {self.__book}, Person: {self.__student}, State: {self.state}, Date: {self.__date}"

    def book_info(self):
        return self.__book

class Log:
    def __init__(self, records: [Record]):
        self.__records = records

    def info_log(self):
        return self.__records

    def pop(self, book: Book, student: Student):
        record = Record(book, student, State.out_lib, datetime.datetime.now())
        self.__records.append(record)

    def bring(self, book: Book, student: Student):
        record = Record(book, student, State.in_lib, datetime.datetime.now())
        self.__records.append(record)

class Library:
    def __init__(self, list_books: [Book]):
        self.__list_books = list_books
        self.__log = Log([])

    def add(self, book):
        self.__list_books += book
        book.state = State.in_lib

    def info(self):
        return self.__list_books

    def log(self):
        return self.__log.info_log()

    def pop(self, name: str, student: Student):
        for book in self.__list_books:
            if book.name() == name:
                    if book.state != State.in_lib:
                        print("Book is not found")
                    else:
                        self.__log.pop(book, student)
                        book.state = State.out_lib

    def bring(self, name: str, student: Student):
        for book in self.__list_books:
            if book.name() == name and book.state == State.out_lib:
                book.state = State.in_lib
                self.__log.bring(book, student)

# Задание 1: Написать две функции, которые буду возвращать: 1) только книги со статусом In, 2) со статусом Out (используя map, filter, reduce)

    def state_in(self):
        books_in = filter(lambda book: book.state == State.in_lib, self.__list_books)
        return books_in

    def state_out(self):
        books_out = filter(lambda book: book.state == State.out_lib, self.__list_books)
        return books_out

book1 = Book("GOT1", "G.Martin", "Fantastic")
book2 = Book("GOT2", "G.Martin", "Fantastic")
library1 = Library([book1, book2])
print("In the library are books (name, autor, genre, state) STEP1: ")
for i in library1.info():
    print(i)

stud1 = Student("Ivan")
stud2 = Student("Petro")
print(f"Come student {stud1} to the library. They are very like fantastic and took one.")

library1.pop("GOT1", stud1)
print("In the library are books (name, autor, genre, state) STEP2: ")
for i in library1.info():
    print(i)

# Задание 1: вызов функций
print("Books in Library: ")
for i in library1.state_in():
    print(i)

print("Books out Library: ")
for i in library1.state_out():
    print(i)
# --------------------------------------

print(f"Come student {stud1} to the library and return book.")
library1.bring("GOT1", stud1)
print("All book in Library STEP3: ")
for i in library1.info():
    print(i)

# Задание 2: Записи из Журнала
print("Records in Log: ")
for i in library1.log():
    print(i)

