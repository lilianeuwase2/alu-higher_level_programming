#!/usr/bin/python3
"""
This module defines a Student class with public instance attributes
and a method to retrieve a dictionary representation of a Student instance.
"""


class Student:
    """
    A class used to represent a Student.

    Attributes:
        first_name (str): The first name of the student
        last_name (str): The last name of the student
        age (int): The age of the student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
            attrs (list, optional): List of attribute names to retrieve.
                                    If None, all attributes are retrieved.

        Returns:
            dict: A dictionary containing the attributes of the Student \
                    instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
