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
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
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


def swap_pairs(head):
    if head is None or head.next is None:
        return head

    next_node = head.next
    next_next_node = next_node.next
    next_node.next = head
    head.next = swap_pairs(next_next_node)
    return next_node


if __name__ == '__main__':
    link = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    print_linked_list(link)
    link = swap_pairs(link)
    print_linked_list(link)
