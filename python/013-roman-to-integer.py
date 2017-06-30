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
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

MAX_CONVERTIBLE_VALUE = 3999
MIN_CONVERTIBLE_VALUE = 1
VAL_SYMBOL_LIST = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'),
                   (100, 'C'), (500, 'D'), (1000, 'M')]

SUBSTITUTION_LIST = [('I' * 4, 'IV'), ('V' + 'I' * 4, 'IX'), ('X' * 4, 'XL'),
                     ('L' + 'X' * 4, 'XC'), ('C' * 4, 'CD'), ('D' + 'C' * 4, 'CM')]


def find_value(c):
    for val, symbol in reversed(VAL_SYMBOL_LIST):
        if c == symbol:
            return val


def roman_to_int(s):
    if not s:
        return None

    for a, b in reversed(SUBSTITUTION_LIST):
        s = s.replace(b, a)
    num = 0
    for c in s[::-1]:
        num += find_value(c)

    return num


if __name__ == '__main__':
    print(roman_to_int('IV') == 4)
    print(roman_to_int('IX') == 9)
    print(roman_to_int('XL') == 40)
    print(roman_to_int('XC') == 90)
    print(roman_to_int('CD') == 400)
    print(roman_to_int('CM') == 900)

    print(roman_to_int('XLIV') == 44)
    print(roman_to_int('LXXXVII') == 87)
    print(roman_to_int('MDCCC') == 1800)
    print(roman_to_int('DI') == 501)
    print(roman_to_int('LXIII') == 63)
