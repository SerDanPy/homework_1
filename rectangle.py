"""2) Create a Rectangle class that represents a rectangle.
Class requirements:
Class attributes:
width — the width of the rectangle.
height — the height of the rectangle.
Class methods:
__init__(rec, width, height) — a constructor that accepts the width and height of the rectangle.
area(rec) — a method that returns the area of ​​the rectangle.
perimeter(rec) — a method that returns the perimeter of the rectangle.
is_square(rec) — a method that returns True if the rectangle is a square (the width is equal to the height), otherwise False.
resize(rec, new_width, new_height) — a method that changes the width and height of the rectangle.
Create an object of the Rectangle class and test all the methods."""


class Rectangle:
    """A class to represent a rectangle with width and height."""
    def __init__(rec, width, height):
        rec.width = width
        rec.height = height


    def area(rec):
        """Calculate the area of the rectangle."""
        return rec.width * rec.height


    def perimeter(rec):
        """Calculate the perimeter of the rectangle."""
        return 2 * (rec.width + rec.height)


    def is_square(rec):
        """Check if the rectangle is a square."""
        return rec.width == rec.height


    def resize(rec, new_width, new_height):
        """Resize the rectangle to new width and height."""
        rec.width = new_width
        rec.height = new_height


if __name__ == "__main__":
    rect = Rectangle(2, 5)

    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Is square? {rect.is_square()}")

    print("========Second========")
    rect.resize(2, 2)
    print(f"New area: {rect.area()}")
    print(f"New perimeter: {rect.perimeter()}")
    print(f"Is square? {rect.is_square()}")
