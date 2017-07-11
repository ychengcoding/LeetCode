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
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(lst):
    pre_node = None
    for n in reversed(lst):
        node = ListNode(n)
        node.next = pre_node
        pre_node = node
    return pre_node


def print_linked_list(linked_list):
    is_first_running = True

    def print_linked_list_impl(lst):
        nonlocal is_first_running
        if is_first_running:
            print("( ", end="")
        if lst:
            if not is_first_running:
                print(" -> ", end="")
            print(lst.val, end="")
            is_first_running = False
            print_linked_list_impl(lst.next)
        else:
            print(")")

    print_linked_list_impl(linked_list)


def merge_k_lists(lists):
    def merge_two_lists(l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = merge_two_lists(l1.next, l2)
        return l1

    pre = None
    for cur in lists:
        if pre is not None:
            pre = merge_two_lists(pre, cur)
        else:
            pre = cur
    return pre


if __name__ == '__main__':
    l1 = create_linked_list([1, 2, 3, 4, 6])
    l2 = create_linked_list([3, 5, 9, 60])
    l3 = create_linked_list([-1, 3, 9, 59])
    print_linked_list(l1)
    print_linked_list(l2)
    print_linked_list(l3)
    res = merge_k_lists([l1, l2, l3])
    print_linked_list(res)
