#!/usr/bin/python3
"""
Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle implementation
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        string representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_type(
            self, attr_name: str, attr_value: object, greater_equal=False):
        """ type validation """
        if not isinstance(attr_value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if not greater_equal:
            if attr_value <= 0:
                raise ValueError("{} must be > 0".format(attr_name))
        else:
            if attr_value < 0:
                raise ValueError("{} must be >= 0".format(attr_name))

    def area(self):
        """ return rectangle area """
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        print('\n' * self.y, end='')
        for l in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """
        update rectangle attributes
        """

        expect = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                args + expect[len(args):len(expect)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    @property
    def width(self) -> int:
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width: int):
        """ width setter """
        self.check_type('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height: int):
        """ height setter """
        self.check_type('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x: int):
        """ x setter """
        self.check_type('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y: int):
        """ y setter """
        self.check_type('y', y, True)
        self.__y = y
