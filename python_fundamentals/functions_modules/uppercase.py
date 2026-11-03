#!/usr/bin/env python3


def uppercase(str):
    for c in str:
        code = ord(c)
        if 97 <= code <= 122:
            code -= 32
        print("{:c}".format(code), end="")
    print()
