#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

for letter in range(100, 126):
    print("{}".format(chr(letter)), end="")
