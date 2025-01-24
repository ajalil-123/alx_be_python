

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False


    def check_out(self):
        self._is_checked_out = True # marks the book as checked out

    def return_book(self):
        self._is_checked_out = False # marks the book as returned and available

    def is_available(self):
        return not self._is_checked_out # returns the availability status of the book


class Library:
    """
    A class representing a library system.
    """
    def __init__(self):
        self._books = []  # Private list to store instances of Book

    def add_book(self, book):
        """
        Adds a new book to the library.
        :param book: Instance of Book to add to the library
        """
        self._books.append(book)
        print(f"Added book: '{book.title}' by {book.author}")

    def check_out_book(self, title):
        """
        Checks out a book from the library if it is available.
        :param title: The title of the book to check out
        """
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Checked out: '{title}'")
                    return
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """
        Returns a book to the library.
        :param title: The title of the book to return
        """
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Returned: '{title}'")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books in the library that are currently available.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f" - '{book.title}' by {book.author}")
        else:
            print("No books are currently available.") 