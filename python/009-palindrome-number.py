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
9. Palindrome Number
Determine whether an integer is a palindrome. Do this without extra space.
"""


def get_length_of_number(x):
    if x < 0:
        return get_length_of_number(-x)
    if x < 10:
        return 1
    return 1 + get_length_of_number(x // 10)


def get_most_left_digit_of_number(x):
    if x < 0:
        return get_most_left_digit_of_number(-x)
    if x < 10:
        return x
    return get_most_left_digit_of_number(x // 10)


def is_palindrome_number(x):
    if x < 0:
        return False

    while x:
        if x < 10:
            return True
        if x % 10 != get_most_left_digit_of_number(x):
            return False
        x %= 10 ** (get_length_of_number(x) - 1)
        x //= 10

    return True


if __name__ == '__main__':
    print(is_palindrome_number(123454321))
    print(is_palindrome_number(1234554321))
    print(is_palindrome_number(16723))
