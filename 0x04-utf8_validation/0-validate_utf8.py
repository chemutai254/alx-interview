#!/bin/usr/env python3
"""
a method that determines if a given data set represents
a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data.
    therefore you only need to handle the 8 least
    significant bits of each integer
    """
    counter = 0
    a = 1 << 7
    b = 1 << 6

    for i in data:
        byte_data = 1 << 7
        if counter == 0:
            while byte_data & i:
                counter += 1
                byte_data = byte_data >> 1
                if counter == 0:
                    continue
            if counter == 1 or counter > 4:
                return False
            else:
                if not((i & a) and (i & b)):
                    return False
        counter -= 1
        if counter == 0:
            return True
        return False
