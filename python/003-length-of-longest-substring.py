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
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


def get_length_of_longest_substring(s):
    length = 0
    cur_str = ''
    for c in s:
        k = cur_str.find(c)
        if k != -1:
            cur_str = cur_str[k + 1:]
        cur_str += c

        if length < len(cur_str):
            length = len(cur_str)
    return length


if __name__ == '__main__':
    print(get_length_of_longest_substring("abcabcbb"))
    print(get_length_of_longest_substring("bbbbb"))
    print(get_length_of_longest_substring("pwwkew"))
    print(get_length_of_longest_substring(""))
