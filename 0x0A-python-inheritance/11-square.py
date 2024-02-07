#!/usr/bin/python3

"""
This module defines a Square class that inherits from the Rectangle class.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """
    Represents a Square, inheriting from Rectangle.
    """

    def __init__(self, size: int) -> None:
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square (width and height).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self) -> str:
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string indicating that this is a Square with its size.
        """
       return '[Square] ' + str(self.__size) + '/' + str(self.__size)
