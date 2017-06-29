#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Cheng Yue"
__copyright__ = "Copyright 2017"
__license__ = "GPLv3"
__version__ = "1.0.0"
__maintainer__ = "Cheng Yue"
__email__ = "ycheng.programming@gmail.com"

"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(numbers):
    pre_node = None
    for n in reversed(numbers):
        node = ListNode(n)
        node.next = pre_node
        pre_node = node
    return pre_node


def print_linked_list(lst):
    is_first_running = True

    def print_linked_list_impl(linked_list):
        nonlocal is_first_running
        if is_first_running:
            print("( ", end="")
        if linked_list:
            if not is_first_running:
                print(" -> ", end="")
            print(linked_list.val, end="")
            is_first_running = False
            print_linked_list_impl(linked_list.next)
        else:
            print(")")

    print_linked_list_impl(lst)


def add_two_numbers(linked_list_a, linked_list_b):
    linked_list_sum = None
    pre_node = None
    carry = 0
    while linked_list_a or linked_list_b:
        val = carry
        if linked_list_a:
            val += linked_list_a.val
            linked_list_a = linked_list_a.next
        if linked_list_b:
            val += linked_list_b.val
            linked_list_b = linked_list_b.next
        val, carry = val % 10, val // 10
        node = ListNode(val)
        if pre_node is not None:
            pre_node.next = node
        pre_node = node
        if linked_list_sum is None:
            linked_list_sum = node

    if not carry == 0:
        pre_node.next = ListNode(carry)

    return linked_list_sum


if __name__ == '__main__':
    a = create_linked_list([2, 4, 3])
    b = create_linked_list([5, 6, 4])
    print("The first linked list:")
    print_linked_list(a)
    print("The second linked list:")
    print_linked_list(b)
    c = add_two_numbers(a, b)
    print("The sum linked list:")
    print_linked_list(c)
