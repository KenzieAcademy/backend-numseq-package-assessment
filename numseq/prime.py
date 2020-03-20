#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Julita Marshall"

def primes(n):
    # primeArr = []
    # for n in range(n):
    #     if is_prime(n):
    #         primeArr.append(n)
    # return primeArr

    import math 


    if n < 2:
        return []
    else:
        primes = [2]
        if n <= primes[-1]:
            return primes
        else:
            for index in range(3, n, 2):
                isPrime = True
                for primenumber in primes:
                    if not index % primenumber:
                        isPrime = False
                    if isPrime:
                        primes.append(index)


def is_prime(n):
    # if number > 1:
    #     for i in range(2, number):
    #         if number % 1 == 0:
    #             return False
    #             break
    #     else:
    #         return True

    primes_list = primes(n + 1)
    print(primes_list)
    return n in primes_list




