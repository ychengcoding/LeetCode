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
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
"""


def get_longest_common_prefix(strs):
    def get_longest_prefix(a, b):
        if len(a) > len(b):
            a, b = b, a
        idx = -1
        for i, c in enumerate(a):
            if c == b[i]:
                idx = i
            else:
                break
        return "" if idx == -1 else b[:idx + 1]

    size = len(strs)
    if size == 0:
        return ""
    elif size == 1:
        return strs[0]
    else:
        longest = get_longest_prefix(strs[0], strs[1])
        if not longest:
            return ""
        for s in strs[:2]:
            prefix = get_longest_prefix(longest, s)
            if len(prefix) > len(longest):
                longest = prefix
        return longest


if __name__ == '__main__':
    print(get_longest_common_prefix(["abcded12837", "abcdeabcc", "abcdqwer"]))
