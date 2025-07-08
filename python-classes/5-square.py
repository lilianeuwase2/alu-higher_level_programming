#!/usr/bin/python3
"""Defines a Square class with printing capability."""

class Square:
    """Represents a square that can print itself."""
    def __init__(self, size=0):
        """Initializes a new Square.
        
        Args:
            size (int, optional): The size of the new square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square.
        
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.
        
        Args:
            value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the square's area.
        
        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
