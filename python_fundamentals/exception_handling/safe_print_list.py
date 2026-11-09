#!/usr/bin/env python3
"""Safely print list elements."""


def safe_print_list(my_list=[], x=0):
    """Return the number of elements printed."""
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    except IndexError:
        pass
    print()
    return printed
