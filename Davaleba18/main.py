# class Vector:
#     def __init__(self, x: float, y: float):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2

# print(v1)
# print(v2)
# print(v3)

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')

print(book1 == book2)
print(book1 == book3)