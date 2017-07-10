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
19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""


# Definition for singly-linked list.
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


def remove_nth_from_end(head, n):
    def remove_nth_from_end_impl(pre, cur):
        if cur is None:
            return 0, pre
        k, _ = remove_nth_from_end_impl(cur, cur.next)
        if k + 1 == n:
            if pre is None:
                pre = cur.next
            else:
                pre.next = cur.next
            cur.next = None
            del cur
        else:
            if pre is None:
                pre = cur

        return k + 1, pre

    _, new_head = remove_nth_from_end_impl(None, head)
    return new_head


if __name__ == '__main__':
    link = create_linked_list([1, 2, 3, 4, 5])
    print_linked_list(link)
    link = remove_nth_from_end(link, 2)
    print_linked_list(link)
