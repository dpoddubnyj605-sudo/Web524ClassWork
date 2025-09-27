"""
_ - защищенный
__ - приватный
"""


class Book:

    def __init__(self, title, author, year=None):
        self.__title = title
        self.__author = author
        if not year:
            self.__year = 'не указано'
        else:
            self.__year = year

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def set_title(self, new_title, access_level='user'):
        if isinstance(new_title, str) and access_level == 'admin':
            # if type(new_title) is str and access_level == 'admin':
            self.__title = new_title
            print(f'Название успешно изменено')
        else:
            print(f'Неверный тип данных/Нет доступа')

    def set_year(self, new_year, access_level='user'):
        if isinstance(new_year, str) and new_year.isdigit() and access_level == 'admin':
            self.__year = new_year
            print(f'Год успешно изменен')
        else:
            print(f'Неверный тип данных/Нет доступа')


if __name__ == '__main__':
    book = Book("Дубровский", "Пушкин А.C.")
    print(book.get_title())
    print(book.get_author())
    print(book.get_year())
    print()

    book.set_title('Капитанская дочка', 'admin')
    book.set_year('1995', 'admin')
    print(book.get_title())
    print(book.get_author())
    print(book.get_year())
    print()

    book.set_title('Дубровский')
    book.set_year('2005')
    print(book.get_title())
    print(book.get_author())
    print(book.get_year())
