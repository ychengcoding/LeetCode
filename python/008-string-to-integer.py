#!/usr/bin/python
# -*- coding: utf-8 -*-

import string

__author__ = "Cheng Yue"
__copyright__ = "Copyright 2017"
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Cheng Yue"
__email__ = "ycheng.programming@gmail.com"

"""
Question:
8. String to Integer (atoi)

Implement atoi to convert a string to an integer.
"""


def string_to_integer(s):
    res = 0
    sign = 1
    for i, c in enumerate(s.lstrip()):
        if i == 0 and c == '-':
            sign = -1
        elif c.isdigit():
            res = res * 10 + int(c)
        elif i != 0:
            break
    return sign * res


if __name__ == '__main__':
    print(string_to_integer("  123"))
    print(string_to_integer("  -9048python"))
    print(string_to_integer("- python"))
