#!/usr/bin/env python3
alphabet = ""
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter not in "eq":
        alphabet += letter
print(alphabet)
