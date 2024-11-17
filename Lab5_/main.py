#Task 1
class Book:
    """
    A class for a book. It has title, author, year of publication and genre
    """

    def __init__(self, title: str, author: str, year: int, genre: str):
        """
        Initializes a new instance of the Book class
        :param
        title - title of book
        author - author of book
        year - year of book
        genre - genre of book
        """
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        """
        Prints details about book
        """
        print (f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}")


#Task 2
class Library:
    """
        A class for storing books and their count
    """
    totalBooks = 0

    def __init__(self):
        """
        Initializes new library instance with empty list of instances Book
        """
        self.books = []

    def addBook(self, book):
        """
        Adds book to the library and increment to book count
        :param book: book instance
        :return:
        """
        self.books.append(book)
        Library.totalBooks += 1

    def __str__(self):
        """
        Prints all books in library
        """

        print("Books in library: ")
        for book in self.books:
            book.__str__()
        print(f"Number of books {self.totalBooks}")


#Task 3
class MathCalculations:
    """
    Class for mathematical functions
    """

    @staticmethod
    def calculateSumOfNumbersToN(n: int) -> int:
        """
        Calculate sum of naturals from 1 to n
        """
        sum = 1

        if n < 1:
            print("N should be greater then 0")
        else:
            return n * (n + 1) // 2


    @classmethod
    def calculateFactorial(cls, n: int) -> int:
        """
        Calculates the factorial of number n
        """
        if n < 0:
            print("N must be greater than 0")
        else:
            result = 1
            for i in range(2, n+1):
                result *= i
            return result

#Task 4
class Rectangle:
    """
    A class to build rectangle with width and height attributes,
    protected against non-positive values.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes the Rectangle instance with width and height.

        Parameters:
        width (float): The width of the rectangle (must be positive).
        height (float): The height of the rectangle (must be positive).
        """
        if width <= 0 or height <= 0:
            print("error")
        else:
            self.width = width
            self.height = height

    @property
    def width(self) -> float:
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value: float):
        """Sets the width of the rectangle, ensuring it is positive."""
        if value <= 0:
            print("Width must be a positive value.")
        else:
            self._width = value

    @property
    def height(self) -> float:
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value: float):
        """Sets the height of the rectangle, ensuring it is positive."""
        if value <= 0:
            print("Height must be a positive value.")
        else:
            self._height = value

    @property
    def area(self) -> float:
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

#Task 1 demo
book1 = Book("Title 1", "Author 1", 2024, "Genre 1")
book2 = Book("Title 2", "Author 2", 2024, "Genre 2")
book3 = Book("Title 3", "Author 3", 2024, "Genre 3")

print("Book Details:")
book1.__str__()
book2.__str__()
book3.__str__()

#Task 2 demo
library = Library()
library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

library.__str__()

#Task 3 demo
n = 10
print(f"Sum of numbers from 1 to {n}: {MathCalculations.calculateSumOfNumbersToN(n)}")
print(f"Factorial of {n}: {MathCalculations.calculateFactorial(n)}")

#Task 4 demo
try:
    rectangle = Rectangle(5, 10)
    print(f"Width: {rectangle.width}, Height: {rectangle.height}, Area: {rectangle.area}")

    # Attempting to set a negative width
    rectangle.width = -4
except ValueError as e:
    print(f"Error: {e}")

rectangle.height = 15
print(f"Updated Height: {rectangle.height}, New Area: {rectangle.area}")