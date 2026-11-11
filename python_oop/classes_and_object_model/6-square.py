#!/usr/bin/env python3
"""Define a square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Iniitialize the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and store the size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square's area."""
        return self.__size ** 2

    def my_print(self):
        """Print the positioned square."""
        print(self)

    def __str__(self):
        """Return the position square."""
        if self.__size == 0:
            return ""
        x, y = self.__position
        row = " " * x + "#" * self.__size
        return "\n" * y + "\n".join(
            [row] * self.__size)

    @property
    def position(self):
        """Return the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and store the position."""
        if (type(value) is not tuple or len(value) != 2
                or any(type(n) is not int or n < 0
                       for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value
