

from  library_system import Book, EBook, PrintBook, Library

def main():
    # Instantiate the library
    my_library = Library()

    # Create one of each book type
    classic_book   = Book("Pride and Prejudice", "Jane Austen")
    digital_novel  = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel    = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add them to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books
    my_library.list_books()

if __name__ == "__main__":
    main()
