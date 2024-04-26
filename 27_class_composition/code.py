class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)}"
        

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    

book = Book("Harry Porter")
book2 = Book("Pyhton 101")
shelf = BookShelf(book, book2)

print(shelf)
        
        