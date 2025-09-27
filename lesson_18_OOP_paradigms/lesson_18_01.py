class Book:

    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        if not year:
            self.year = 'не указано'
        else:
            self.year = year


if __name__ == '__main__':
    book = Book("Дубровский", "Пушкин А.C.")
    print(book.title)
    print(book.author)
    print(book.year)
    print()

    book.title = "Странный Человек"
    book.author = 'Лермонтов М.Ю.'
    print(book.title)
    print(book.author)

