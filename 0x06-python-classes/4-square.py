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

    def area(self):
        """ calculate square area
        Returns:
            the current square area
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieve size value
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """set size attribute
        Args:
            size: size of the square
        Returns: None
        """
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
