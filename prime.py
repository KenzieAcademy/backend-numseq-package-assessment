#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "andrewpchristensen701"

from math import sqrt


def primes(n):
    if isinstance(n, (int, long)):
        a = range(2, n + 1)
        b, c = [], a
        while c[0] < sqrt(n):
            starting_integer = c[0]
            b += [starting_integer]
            c = [x for x in c if x % starting_integer != 0]
        return b + c
    else:
        return "Invalid Input!"


def is_prime(n):
    if isinstance(n, (int, long)):
        if n >= 2:
            for x in range(2, n):
                if not (n % x):
                    return False
        else:
            return False
        return True
    else:
        return "Invalid Input!"


def main():
    print ("Primes")
    prime_list = primes(1000)
    for p in prime_list[-10:]:
        print (p)
    print ("Is 11037 prime? {}".format(is_prime(11037)))
    print ("Is 1103 prime? {}".format(is_prime(1103)))


if __name__ == "__main__":
    main()