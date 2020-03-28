#!/usr/local/env/ python
# -*- coding: utf-8 -*-

__author__ = 'Tiffany McLean & Demo with Chris Wilson'


def fib(n):
    """
    should return the nth Fibonacci number
    """

    a, b = 0, 1
    num = 0
    while num < n:
        a, b = b, a + b
        num += 1
    return a
