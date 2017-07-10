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
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
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


def merge_two_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    n1 = l1.next
    n2 = l2.next
    l1.next = l2
    l2.next = merge_two_lists(n1, n2)
    return l1


if __name__ == '__main__':
    l1 = create_linked_list([1, 2, 3, 4, 6])
    l2 = create_linked_list([3, 5, 9, 60])
    print_linked_list(l1)
    print_linked_list(l2)
    l3 = merge_two_lists(l1, l2)
    print_linked_list(l3)
