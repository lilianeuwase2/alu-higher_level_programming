#!/usr/bin/python3
"""Defines a Square class with size property."""

class Square:
    """Represents a square with size property."""
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
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
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
