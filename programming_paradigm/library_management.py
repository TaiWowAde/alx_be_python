class Book:
    """
    Represent a book with title author and availability status
    """

    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Title and author must be provided")
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out if available return True otherwise False"""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned if it was checked out return True otherwise False"""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is not checked out otherwise False"""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    """
    Manage a collection of Book instances allow adding checking out returning and listing available books
    """

    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return True
                raise Exception(f"Book '{title}' is already checked out")
        raise LookupError(f"Book '{title}' not found in the library")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return True
                raise Exception(f"Book '{title}' was not checked out")
        raise LookupError(f"Book '{title}' not found in the library")

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books are currently available")
        else:
            for book in available:
                print(book)
