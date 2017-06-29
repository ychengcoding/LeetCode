#!/usr/bin/python
# -*- coding: utf-8 -*-

import math

__author__ = "Cheng Yue"
__copyright__ = "Copyright 2017"
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Cheng Yue"
__email__ = "ycheng.programming@gmail.com"

"""
Question:
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


def find_median_sorted_arrays(nums1, nums2):
    total_length = len(nums1) + len(nums2)
    if total_length % 2 == 0:
        middle_one_position = (total_length / 2) - 1
        middle_two_position = total_length / 2
    else:
        middle_one_position = int(math.floor(total_length / 2))
        middle_two_position = int(math.floor(total_length / 2))

    middle_one = None
    middle_two = None

    index1 = 0
    index2 = 0
    current_position = -1
    while index1 < len(nums1) or index2 < len(nums2):
        if index1 < len(nums1):
            if index2 < len(nums2) and nums1[index1] > nums2[index2]:
                current_number = nums2[index2]
                index2 += 1
            else:
                current_number = nums1[index1]
                index1 += 1
            current_position += 1
            if middle_one_position == current_position:
                middle_one = current_number
            if middle_two_position == current_position:
                middle_two = current_number

        index1, nums1, index2, nums2 = index2, nums2, index1, nums1

        if middle_one is not None and middle_two is not None:
            break

    if middle_one is not None and middle_two is not None:
        return (middle_one + middle_two) / 2
    else:
        return None


if __name__ == '__main__':
    print(find_median_sorted_arrays([1, 3], [2]))
    print(find_median_sorted_arrays([1, 2], [3, 4]))
    print(find_median_sorted_arrays([3], []))
    print(find_median_sorted_arrays([], []))
