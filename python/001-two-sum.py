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
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def two_sum_v01(number_list, target_sum):
    for i in range(0, len(number_list) - 1):
        for k in range(i, len(number_list)):
            if number_list[i] + number_list[k] == target_sum:
                return i, k
    return -1, -1


def two_sum_v02(number_list, target_sum):
    lookup = {}
    for i, x in enumerate(number_list):
        if (target_sum - x) in lookup:
            return lookup[target_sum - x], i
        else:
            lookup[x] = i
    return -1, -1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum_v01(nums, target))
    print(two_sum_v02(nums, target))
