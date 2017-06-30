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
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an, 
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


def get_max_area(heights):
    def calc_area(left, right):
        nonlocal heights
        return (right - left) * min(heights[left], heights[right])

    if heights is None or len(heights) < 2:
        return 0

    low = 0
    high = len(heights) - 1
    max_area = 0
    while low < high:
        max_area = max(max_area, calc_area(low, high))
        if heights[low] < heights[high]:
            low += 1
        else:
            high -= 1
    return max_area


if __name__ == '__main__':
    print(get_max_area([1, 1]))
    print(get_max_area([1, 2, 11, 9, 7, 5, 3]))