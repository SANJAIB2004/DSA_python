from abc import ABC, abstractmethod

class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id.strip().upper()
        self.title = title.strip().title()
        self.author = author.strip().title()

    def __str__(self):
        return f"{self.book_id} {self.title} by {self.author}"

class LibraryManagementSystem(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, book_id: str):
        pass

    @abstractmethod
    def search_book(self, title: str):
        pass

    @abstractmethod
    def list_books(self):
        pass


class Operations(LibraryManagementSystem):
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book):
        if book.book_id in self.books:
            print(f"Book ID '{book.book_id}' already exists. Cannot add duplicate.")
        else:
            self.books[book.book_id] = book
            print(f"Book '{book}' added to the library.")

    def remove_book(self, book_id: str):
        book_id = book_id.strip().upper()
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Book '{removed}' removed from the library.")
        else:
            print(f"No book found with ID '{book_id}'.")

    def search_book(self, title: str):
        title = title.strip().lower()
        found = False
        for book in self.books.values():
            if book.title.lower() == title:
                print(f"Found: {book}")
                found = True
        if not found:
            print(f"No book found with title '{title.title()}'.")

    def list_books(self):
        if not self.books:
            print("The library is currently empty.The Library has no books")
        else:
            print("List of books in the library:")
            for book in self.books.values():
                print(f"{book}")

if __name__ == '__main__':
    library = Operations()

    # Add books
    book1 = Book("B1", "The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("B2", "To Kill a Mockingbird", "Harper Lee")
    book3 = Book("B1", "1984", "George Orwell")
    library.list_books()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.remove_book("B1")
    library.search_book("To Kill a Mockingbird")
    library.search_book("The Great Gatsby")
    library.list_books()
