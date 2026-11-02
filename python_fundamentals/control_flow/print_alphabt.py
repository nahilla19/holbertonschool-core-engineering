#!/usr/bin/env python3
for code in range(97, 123):
    if code not in (101, 113):
        print("{}".format(chr(code)), end="")
