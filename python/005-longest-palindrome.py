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
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"
Output: "bab"

Note: "aba" is also a valid answer.

Example:
Input: "cbbd"
Output: "bb"
"""


def get_longest_palindrome(s):
    if s == s[::-1]:
        return s
    left = get_longest_palindrome(s[:len(s) - 1])
    right = get_longest_palindrome(s[1:])

    if len(left) > len(right):
        return left
    else:
        return right


if __name__ == '__main__':
    print(get_longest_palindrome("babad"))
    print(get_longest_palindrome("cbbd"))
