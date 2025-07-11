#!/usr/bin/python3
class BaseGeometry:
    """Base class with integer validation."""
    def area(self):
        """Raise an exception."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate a value as a positive integer.
        Args:
            name: Name of the value (assumed to be string).
            value: Value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
