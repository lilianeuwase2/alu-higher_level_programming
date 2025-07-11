#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class with custom string representation."""
    
    def __init__(self, size):
        """Initializes a Square instance with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
