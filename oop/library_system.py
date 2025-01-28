
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

#an ebook class that prints an ebook by title, author and file size 
# This is a derived class that inherits some attributes from Book class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title,author)
        self.file_size = file_size
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# a print book class that inherits some attributes from Book class
#the attributes it inherits are ptitle and author

class PrintBook(Book):
    def __init__(self,title,author,page_count):
         super().__init__(title,author)
         self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

#create a composition class with methods such as add_book() and list_books()
class Library:
    def __init__(self):
        self.books = [] # create a list store of instances of Book,Ebook and Printbook

    # method that adds a Book, EBook or PrintBook instance to the library
    def add_book(self, book):
        if isinstance(book, Book):  # Ensure only instances of Book or its subclasses are added
            self.books.append(book)
        else:
            print("Error: Only instances of Book, EBook, or PrintBook can be added to the library.")
    
    # a method that lists and prints the details of each book in the library
    def list_books(self):
        if not self.books:
            print("The library is currently empty.")
        else:
            for book in self.books:
                print(book)