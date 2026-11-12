#!/usr/bin/env python3
"""Rectangle class extend"""

BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with validated dimensions."""

    def __init__(self, width, height):
        """Validate and store both dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the rectangle's area."""
        return self.__width * self.__height

    def __str__(self):
        """Return a readable rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"
