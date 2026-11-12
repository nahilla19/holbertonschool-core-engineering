#!/usr/bin/env python3
"""Define shared geometry behavior."""


class BaseGeometry:
    """Provide methods for geometry behavior."""

    def area(self):
        """Requires subclasses to calculate area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
