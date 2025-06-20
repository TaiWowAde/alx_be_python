class Book:
    def __init__(self, title, author, year):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not isinstance(author, str):
            raise TypeError("author must be a string")
        if not isinstance(year, int):
            raise TypeError("year must be an integer")
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print(f"Deleting {self.title}")
