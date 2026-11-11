#!/usr/bin/env python3
"""Demostrate inheritance."""


class Animal:
    """Represent an animal."""

    def speak(self):
        """Return a general sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog."""

    def speak(self):
        """Return the dog's sound."""
        return "Woof!"


class Cat(Animal):
    """Represent a cat."""

    def speak(self):
        """Return the cat's sound."""
        return "Meow!"


dog = Dog()
cat = Cat()

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
