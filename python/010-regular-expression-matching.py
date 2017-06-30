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
10. Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


def look_ahead(s):
    n = len(s)
    if n == 0:
        return None, None, s
    elif n == 1:
        return s, None, s[1:]
    else:
        return s[0], s[1], s[1:]


def look_up(s):
    n = len(s)
    if n == 0:
        return None, s
    else:
        return s[0], s[1:]


def push_front(s, c):
    if c:
        s = c + s
    return s


def is_any_char(p):
    return p == '.'


def is_zero_or_many_char(p):
    return p == '*'


def is_special_char(p):
    return is_any_char(p) or is_zero_or_many_char(p)


def is_zero_or_many_for_any(a, b):
    return is_any_char(a) and is_zero_or_many_char(b)


def is_match(s, p):
    cur_p, next_p, p = look_ahead(p)
    cur_s, s = look_up(s)
    if not cur_s:
        if cur_p:
            if is_zero_or_many_for_any(cur_p, next_p):
                cur_p, next_p, p = look_ahead(p)
                return next_p is None
        return True

    if not cur_p:
        return False

    if not is_special_char(cur_p):
        if is_zero_or_many_char(next_p):
            if cur_s == cur_p:
                s = push_front(s, cur_s)
                i = 0
                while i < len(s) and s[i] == cur_p:
                    i += 1
                _, p = look_up(p)
                for k in range(i + 1, -1, -1):
                    if is_match(s[k:], p):
                        return True
                return False
            else:
                _, p = look_up(p)
                return is_match(s, p)
        else:
            return cur_s == cur_p and is_match(s, p)
    elif is_zero_or_many_char(cur_p):
        return cur_s == cur_p and is_match(s, p)
    else:
        if is_zero_or_many_for_any(cur_p, next_p):
            s = push_front(s, cur_s)
            n = len(s)
            _, p = look_up(p)
            for i in range(n, -1, -1):
                if is_match(s[i:], p):
                    return True
            return False
        else:
            return is_match(s, p)


if __name__ == '__main__':
    print(is_match("aac", "a.*") is True)
    print(is_match("aa", "aa") is True)
    print(is_match("aaa", "aa") is False)
    print(is_match("aa", "a*") is True)
    print(is_match("aa", ".*") is True)
    print(is_match("ab", ".*") is True)
    print(is_match("aab", "c*a*b") is True)
    print(is_match("cccaab", ".*a*b") is True)
    print(is_match("aaa", "aaa.*") is True)
