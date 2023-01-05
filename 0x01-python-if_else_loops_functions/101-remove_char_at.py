#!/usr/bin/python3
def remove_char_at(str, n):
    str = list(str)
    length = len(str)
    if length < n or n < 0:
        return "".join(str)
    else:
        str.pop(n)
        return "".join(str)
