#!/usr/bin/python3

class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the student object to a dictionary with selected attributes.

        Args:
            attrs (list, optional): A list of attributes to include in the dictionary.
                                    If None, all attributes are included. Defaults to None.

        Returns:
            dict: A dictionary representation of the student object with selected attributes.
        """
        class_dict = self.__dict__
        selected_dict = {}

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str) and attr in class_dict:
                    selected_dict[attr] = class_dict[attr]
            return selected_dict

        return class_dict

