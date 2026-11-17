#!/usr/bin/env python3

"""Read and display a text file."""


def read_file(filename=""):
    """Print a UTF-8 file to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
