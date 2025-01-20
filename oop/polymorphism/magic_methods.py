# 7:46:25

# magic methods = dunder methods (double underscore) __init__(call itself every time when the class called),
#  __str__ (instead of showing memory addres where the class is it shows the string), __eq__,
#  they are automatically called by many of Python's built-in operations
#  they allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    # instead of showing memory addres where the class is it shows the string
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, value):
        return self.title == value.title and self.author == value.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    # method above make print(book3 > book2) work

    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return True
    
    
    

book1 = Book("Common stock", "Fisher", 123)   
book2 = Book("Harry Potter", "J.K. Rowling", 223)   
book3 = Book("Harry Potter", "J.K. Rowling", 400)   

print(book1)
print(book2)
print(book1 == book2)
print(book3 == book2)
print(book3 > book2)
print(book3 + book2)
print("Harry" in book2)
print(book2["title"])