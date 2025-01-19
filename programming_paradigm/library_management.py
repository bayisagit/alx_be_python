class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    
    
class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                return book.return_book()
        return False
    
    def list_available_books(self):
        available_books = [f"{book.title} by {book.author}" for book in self.books if not book.is_checked_out]
        print("\n".join(available_books))
 