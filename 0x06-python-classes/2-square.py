#!/usr/bin/python3
"""class square"""


class Square:
    """Class Square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """Initialize private instance attribute
        Args:
            size (int): size for the square

        Returns: None
        """
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
