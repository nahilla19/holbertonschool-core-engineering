#!/usr/bin/env python3
"""Define mixins for a dragon's swimming and flying abilities."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print the creature's swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print the creature's flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim, fly, and roar."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")


def main():
    """Demonstrate the dragon's abilities when run as a script."""
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()


if __name__ == "__main__":
    main()
