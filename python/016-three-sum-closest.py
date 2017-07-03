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
16. 3Sum Closest
Given an array S of n integers,
find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
import sys


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


def get_three_sum_closest(nums, target):
    res = []
    closest = sys.maxsize
    for c in combination(nums, 3):
        diff = abs(sum(c) - target)
        if not diff:
            continue
        if diff <= closest:
            for e in res:
                if sorted(e) == sorted(c):
                    break
            else:
                res.append(c)
                closest = diff
    return res


if __name__ == '__main__':
    print(get_three_sum_closest([-1, 2, 1, -4], 1))
