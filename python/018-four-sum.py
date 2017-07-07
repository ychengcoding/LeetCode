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

18. 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


def combination(lst, n):
    if n is None:
        n = len(lst)
    for i in range(len(lst)):
        e = lst[i:i + 1]
        if n == 1:
            yield e
        else:
            for r in combination(lst[i + 1:], n - 1):
                yield e + r


def four_sum(nums, target):
    res = []
    for c in combination(nums, 4):
        if sum(c) == target:
            for r in res:
                if sorted(r) == sorted(c):
                    break
            else:
                res.append(c)

    return res


if __name__ == '__main__':
    print(four_sum([1, 0, -1, 0, -2, 2], 0))
