#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    """Print integer row with single spaces."""
    for row in matrix:
        for i, value in enumerate(row):
            if i:
                print(" ", end="")
            print("{:d}".format(value), end="")
        print()
