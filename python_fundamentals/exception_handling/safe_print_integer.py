#!/usr/bin/env python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return true
    except (valueError, TypeError):
        return False
