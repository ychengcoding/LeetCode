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
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, 
your answer could be in any order you want.
"""

DIGIT_TO_LETTERS = {
    "1": "",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqs",
    "8": "tuv",
    "9": "wxyz",
    "0": ""
}


def letter_combinations(digits):
    if not digits:
        return [""]

    letters = DIGIT_TO_LETTERS[digits[:1]]
    rest = letter_combinations(digits[1:])
    if not letters:
        return rest
    return [x + c for x in rest for c in letters]


if __name__ == '__main__':
    print(letter_combinations("138927540933"))
