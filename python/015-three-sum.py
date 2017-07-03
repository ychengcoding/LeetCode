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
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def combination(lst, n):
    if len(lst) < n or n <= 0:
        return [[]]
    if len(lst) == n:
        return [lst]
    if n == 1:
        return [[x] for x in lst]
    res = []
    for r in combination(lst[1:], n - 1):
        res.append([lst[0]] + r)
    return res + combination(lst[1:], n)


def get_three_sum(nums):
    res = []
    for c in combination(nums, 3):
        if sum(c) == 0:
            for e in res:
                if sorted(e) == sorted(c):
                    break
            else:
                res.append(c)
    return res


if __name__ == '__main__':
    print(get_three_sum([-1, 0, 1, 2, -1, -4]))
