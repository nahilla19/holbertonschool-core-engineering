#!/usr/bin/env python3
"""Provide a list subclass that announces mutations."""

import operator


class VerboseList(list):
    """A list that prints a notice whenever items are added or removed."""

    def append(self, item):
        """Append an item and announce the addition."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and announce how many items were added."""
        old_length = len(self)
        super().extend(iterable)
        added = len(self) - old_length
        print(f"Extended the list with [{added}] items.")

    def remove(self, item):
        """Remove the first matching item and announce the removal."""
        super().index(item)
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item, announcing it before removal."""
        position = operator.index(index)
        item = super().__getitem__(position)
        print(f"Popped [{item}] from the list.")
        return super().pop(position)
