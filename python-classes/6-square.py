#!/usr/bin/python3
"""Defines a Square class with position handling."""

class Square:
    """Represents a square with position."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square with size and position.
        
        Args:
            size (int, optional): The size of the new square. Defaults to 0.
            position (tuple, optional): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square.
        
        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.
        
        Args:
            value (tuple): The new position of the square.
            
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or \
           len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the square's area.
        
        Returns:
            int: The current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with position handling."""
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        print("\n" * self.__position[1], end="")
        
        # Print each line with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
