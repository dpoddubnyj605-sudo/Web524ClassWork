class Book:

    def __init__(self, title, author, year=None):
        self.__title = title
        self.__author = author
        if not year:
            self.__year = 'не указано'
        else:
            self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            # if type(new_title) is str and access_level == 'admin':
            self.__title = new_title
            print(f'Название успешно изменено')
        else:
            print(f'Неверный тип данных/Нет доступа')

    @year.setter
    def year(self, new_year):
        if isinstance(new_year, str) and new_year.isdigit():
            self.__year = new_year
            print(f'Год успешно изменен')
        else:
            print(f'Неверный тип данных/Нет доступа')


if __name__ == '__main__':
    book = Book("Дубровский", "Пушкин А.C.")
    print(book.title)
    print(book.author)
    print(book.year)
    print()

    book.title = 'Капитанская дочка'
    book.year = '1995'
    print(book.title)
    print(book.author)
    print(book.year)
    print()

    book.title = 'Дубровский'
    book.year = '2005'
    print(book.title)
    print(book.author)
    print(book.year)

