#!/usr/bin/python3

class MyInt(int):
    """
    A rebellious subclass of int that inverts the behavior of
    the equality and inequality operators.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
            other (int): The object to compare against.

        Returns:
            bool: True if the objects are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Args:
            other (int): The object to compare against.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        return super().__eq__(other)

