class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return self.title

book_instance1 = Book("GOAT LIFE","Benyamin", 500)
book_instance2 = Book("Story of my life","Ann sulivan", 600)
book_instance3 = Book("Wings of fire","APJ Abdul Kalam", 900)

class Library:
    def __init__(self,name,place):
        self.name = name
        self.place = place
        self.books = []

    def add_books(self,book):
        self.books.append(book)

    def list_books(self):
        for b in self.books:
            print(b)

library_instance = Library("SRM Library","Kottayam")

library_instance.add_books(book_instance1)
library_instance.add_books(book_instance2)
library_instance.add_books(book_instance3)

library_instance.list_books()