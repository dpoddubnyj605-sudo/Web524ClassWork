class LibraryBook:
    all_books = []
    total_books = 0

    def __init__(self, title, status="доступна"):
        self.title = title
        self.status = status
        LibraryBook.all_books.append(self)
        LibraryBook.total_books += 1

    @classmethod
    def display_all_books(cls):
        if cls.all_books:
            print(cls.get_total_books())
            for book in cls.all_books:
                print(book)
        else:
            print('Библиотека пуста')

    @classmethod
    def get_total_books(cls):
        return f'Всего книг в библиотеке: {cls.total_books}'

    @staticmethod
    def is_available(status):
        return status == 'доступна'

    def change_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f'Книга: {self.title}. Статус: {self.status}'


if __name__ == '__main__':
    # Основная программа
    LibraryBook.display_all_books()
    book1 = LibraryBook("Мастер и Маргарита")
    book2 = LibraryBook("1984")
    print(book1)
    print(book2)
    book1.change_status('выдана')
    print(book1)
    print()
    LibraryBook.display_all_books()


