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
22. Generate Parentheses

Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


def generate_parenthesis(n):
    res = []

    def generate_parenthesis_impl(solution, left, right):
        if left == 0 and right == 0:
            res.append(solution)
        else:
            if left > 0:
                generate_parenthesis_impl(solution + "(", left - 1, right)
            if right > left:
                generate_parenthesis_impl(solution + ")", left, right - 1)

    generate_parenthesis_impl("", n, n)
    return res


if __name__ == '__main__':
    print(generate_parenthesis(3))
    print(generate_parenthesis(4))
