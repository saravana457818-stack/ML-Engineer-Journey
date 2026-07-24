class Library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def borrow_book(self):
        if self.available:
            self.available = False
            print("Book Borrowed Successfully.")
        else:
            print("Book is Already Borrowed.")

    def return_book(self):
        self.available = True
        print("Book Returned Successfully.")

    def display(self):
        print("\n----- Book Details -----")
        print("Book :", self.book_name)
        print("Author :", self.author)
        print("Available :", self.available)


book = Library("Python Programming", "Guido")

book.display()

book.borrow_book()

book.display()

book.return_book()

book.display()