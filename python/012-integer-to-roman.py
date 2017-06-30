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
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

MAX_CONVERTIBLE_VALUE = 3999
MIN_CONVERTIBLE_VALUE = 1
VAL_SYMBOL_LIST = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'),
                   (100, 'C'), (500, 'D'), (1000, 'M')]

SUBSTITUTION_LIST = [('I' * 4, 'IV'), ('V' + 'I' * 4, 'IX'), ('X' * 4, 'XL'),
                     ('L' + 'X' * 4, 'XC'), ('C' * 4, 'CD'), ('D' + 'C' * 4, 'CM')]


def find_suitable_symbol(n):
    for val, symbol in reversed(VAL_SYMBOL_LIST):
        if n >= val and (n // val) < 10:
            return val, symbol


def int_to_roman(num):
    if num < MIN_CONVERTIBLE_VALUE or num > MAX_CONVERTIBLE_VALUE:
        return None
    roman = ''
    while num:
        val, symbol = find_suitable_symbol(num)
        roman += symbol * (num // val)
        num %= val

    for a, b in reversed(SUBSTITUTION_LIST):
        roman = roman.replace(a, b)
    return roman


if __name__ == '__main__':
    print(int_to_roman(4) == 'IV')
    print(int_to_roman(9) == 'IX')
    print(int_to_roman(40) == 'XL')
    print(int_to_roman(90) == 'XC')
    print(int_to_roman(400) == 'CD')
    print(int_to_roman(900) == 'CM')

    print(int_to_roman(44) == 'XLIV')
    print(int_to_roman(87) == 'LXXXVII')
    print(int_to_roman(1800) == 'MDCCC')
    print(int_to_roman(501) == 'DI')
    print(int_to_roman(63) == 'LXIII')
