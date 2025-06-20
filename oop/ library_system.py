class Book:
    def __init__(self, title, author):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(author, str):
            raise TypeError("author must be a string")
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        if not isinstance(file_size, int):
            raise TypeError("file_size must be an integer")
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        if not isinstance(page_count, int):
            raise TypeError("page_count must be an integer")
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book or its subclasses")
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(str(book))
