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
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


def is_valid(s):
    end_start_map = {')': '(', ']': '[', '}': '{'}
    stack = []
    for c in s:
        if c in "([{":
            stack.append(c)
        elif c in ")]}":
            pre = stack.pop() if stack else None
            if end_start_map[c] != pre:
                return False
        else:
            pass
    return len(stack) == 0


if __name__ == '__main__':
    print(is_valid("([)]") is False)
    print(is_valid("()[]{}") is True)
