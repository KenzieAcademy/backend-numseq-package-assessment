#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import prime


class TestPrime(unittest.TestCase):

    def test_primes(self):
        primes_six = prime.primes(6)
        primes_twelve = prime.primes(12)
        string_input = prime.primes("String")
        self.assertEquals(primes_six, [2, 3, 5])
        self.assertEquals(primes_twelve, [2, 3, 5, 7, 11])
        self.assertEquals(string_input, "Invalid Input")

    def test_isprime(self):
        isprime_thirteen = prime.is_prime(13)
        isprime_eight = prime.is_prime(8)
        string_input = prime.is_prime("String")
        self.assertEquals(isprime_thirteen, True)
        self.assertEquals(isprime_eight, False)
        self.assertEquals(string_input, "Invalid Input")