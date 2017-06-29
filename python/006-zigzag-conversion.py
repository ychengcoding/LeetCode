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
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


def zigzag_convert(s, num_rows):
    str_array = [""] * num_rows
    curr_row = 0
    step = 1 if num_rows > 1 else 0
    for c in s:
        str_array[curr_row] += c
        if curr_row + step == num_rows or curr_row + step == -1:
            step = -step
        curr_row += step

    res = ""
    for row in str_array:
        res += row

    return res


if __name__ == '__main__':
    print(zigzag_convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
