#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""IS211_Assingment14: A simple app for recursion."""


def fibonacci(n):
    """A function for the fibonacci sequence.

    Args:
        n (integer): An integer.

    Returns:
        int: Returns an integer based on the fibonacci sequence.

    Examples:
    >>> fibonacci(10)
    55
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    """
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


def gcd(a , b):
    """A function for the greatest common divisor.

    Args:
        a (integer): The first integer.
        b (integer): The second integer.

    Returns:
        int: The greatest common divisor between a and b.

    Examples:
    >>> gcd(10, 22)
    2
    >>> gcd(155, 678)
    1
    >>> gcd(5567, 1234)
    1
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    """A function to compare two strings.

    Args:
        s1 (string): The first string.
        s2 (string): The second string.
        
    Returns:
        int: A value corresponding with the comparison of two strings.
             Returns a positive integer if s1 is greater than s2.
             Returns a negative integer if s1 is less than s2.
             Returns 0 if both strings are the ssame.
        
    Examples:
    >>> compareTo('sentence', 'sentence2')
    -101
    >>> compareTo('a big brown fox', 'a big blue box')
    114
    >>> compareTo('look alike', 'look alike')
    0
    """
    if s1 == '' and s2 == '':
        return 0
    elif ord(s1[0]) > ord(s2[0]):
        return 0 + ord(s1[0])
    elif ord(s1[0]) < ord(s2[0]):
        return 0 - ord(s2[0])
    elif s1[1:2] == '' and not s2[1:2] == '':
        return 0 - ord(s2[0])
    elif s2[1:2] == '' and not s1[1:2] == '':
        return 0 + ord(s1[0])
    elif s1[1:2] == '' and s2[1:2] == '':
        return 0
    else:
        return compareTo(s1[1:], s2[1:])
