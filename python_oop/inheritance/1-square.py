#!/usr/bin/env python3
"""Define a square that inherits from Rectangle."""

Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Validate size and initialiaze the rectangle."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square's area."""
        return self.__size * self.__size
