#!/usr/bin/env python3
"""Define a square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Iniitialize the square."""
        self.size = size

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
        """Print the square using #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
