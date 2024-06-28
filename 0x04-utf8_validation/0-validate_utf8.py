#!/usr/bin/python3
"""
Method to determine if given data represents valid UTF-8 encoding
Prototype: def validUTF8(data)
Returns True if data is valid UTF-8 encoding, else return False
Dataset can contain multiple characters
Data will represent a list of integers
"""


def validUTF8(data):
    """
    Prototype: def validUTF8(data)
    Returns True if data is valid UTF-8 encoding
    else return False
    """
    count = 0
    for byte in data:
        '''Extract the 8 least significant bits'''
        byte &= 0xFF
        '''If count is 0, check for start bytes'''
        if count == 0:
            '''Start of 2-byte character'''
            if byte & 0b11100000 == 0b11000000:
                count = 1
            elif byte & 0b11110000 == 0b11100000:
                count = 2
            elif byte & 0b11111000 == 0b11110000:
                count = 3
            elif byte & 0b10000000 == 0b10000000:
                return False
        else:
            if byte & 0b11000000 != 0b10000000:
                return False
            count -= 1
    return count == 0
