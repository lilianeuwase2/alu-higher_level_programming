#!/usr/bin/python3
"""Defines a Square class with private size attribute."""

class Square:
    """Represents a square."""
    def __init__(self, size):
        """Initializes a new Square.
        
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
