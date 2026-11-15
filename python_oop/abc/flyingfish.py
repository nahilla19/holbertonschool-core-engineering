#!/usr/bin/env python3
"""Demonstrate multiple inheritance with a flying fish."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Print the fish's swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print the bird's flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a fish that can swim and fly."""

    def fly(self):
        """Print the flying fish's flying behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print the flying fish's swimming behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
