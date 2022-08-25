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
    no_of_bits_per_block = 8
    max_no_of_ones = 4

    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= (no_of_bits_per_block - 1)
        if number == 0:  # single byte char
            index += 1
            continue

            # validate multi-byte char
            number_of_ones = 0
            while True:  # get the number of significant ones
                number = data[index] & (2 ** (7 - number_of_ones))
                number >>= (no_of_bits_per_block - number_of_ones - 1)
                if number == 1:
                    number_of_ones += 1
                else:
                    break

                if number_of_ones > max_no_of_ones:
                    return False  # too much ones per char sequence

            if number_of_ones == 1:
                return False  # there has to be at least 2 ones

            index += 1  # move on to check the next byte in a multi-byte
            # char sequence

            # check for out of bounds and exit early
            if index >= len(data) or index >= (index + number_of_ones - 1):
                return False

            # every next byte has to start with "10"
            for i in range(index, index + number_of_ones - 1):
                number = data[i]

                number >>= (no_of_bits_per_block - 1)
                if number != 1:
                    return False
                number >>= (no_of_bits_per_block - 1)
                if number != 0:
                    return False

                index += 1

        return True
