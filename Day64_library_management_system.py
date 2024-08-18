'''
make a class Library
-> make must two variable number of books(increase when books added), books (list)
-> make a method which checks the books list length and number of books
'''

class Library:
    def __init__(self) -> None:
        self.no_books = 0
        self.books = []


    def add_book(self, book):
        self.books.append(book)
        self.no_books = len(self.books)

    def show_info(self):
        print(f'The library has {self.no_books} books. The books are')
        for book in self.books:
            print(book)

    
        

l1 = Library()
l1.add_book('Harry Potter')
l1.show_info()