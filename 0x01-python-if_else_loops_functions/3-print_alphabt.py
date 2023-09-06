#!/usr/bin/python3
for letter in range(100, 126):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
