#implementing a system that tracks books in a library
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    
    def __str__(self):
        return f'{self.title} by {self.author} - {"checkout" if self.is_checked_out else "available"}'
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.checkout():
                    return f'You have checked out "{book.title}".'
                else:
                    return f'"{book.title}" is already checked out.'
        return f'Book titled "{title}" not found in the library.'
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    return f'You have returned "{book.title}".'
                else:
                    return f'"{book.title}" was not checked out.'
        return f'Book titled "{title}" not found in the library.'
    
    def list_available_books(self):
        available_books = [str(book)for book in self.books if not book.is_checked_out]
        return available_books if available_books else "No available books in the library"
    