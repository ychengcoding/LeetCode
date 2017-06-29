#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Cheng Yue"
__copyright__ = "Copyright 2017"
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Cheng Yue"
__email__ = "ycheng.programming@gmail.com"

"""
Question:
7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. 
Your function should return 0 when the reversed integer overflows.

"""


def reverse_integer(x):
    if x < 0:
        return -reverse_integer(-x)

    res = 0
    while x:
        res = res * 10 + (x % 10)
        x //= 10
    return res if res <= 0x7fffffff else 0


if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
