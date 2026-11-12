#!/usr/bin/env python3
"""Square class appropiate string"""

BaseSquare = __import__("1-square").Square


class Square(BaseSquare):
    def __str__(self):
        """Return the square description."""
        return super().__str__().replace("[Rectangle]", "[Square]", 1)
