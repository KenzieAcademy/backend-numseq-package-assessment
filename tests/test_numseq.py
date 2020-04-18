#!/usr/bin/env python3
"""Unit Test cases for Numseq Package"""

import sys
import unittest
import timeit
import importlib
from importlib.util import find_spec
import types
import inspect


# globals
PKG_NAME = 'numseq'  # devs: change this to soln.numseq to debug solution
primes = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
    53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
    109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
    173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
    293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
    367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
    433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
    499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
    577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
    643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
    719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
    797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
    863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
    947, 953, 967, 971, 977, 983, 991, 997
)
triangles = (
    0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105,
    120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351,
    378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741,
    780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225,
    1275, 1326, 1378, 1431
)
fibs = (
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
    144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
    17711, 28657, 46368, 75025, 121393, 196418, 317811
)


def import_helper(test_class):
    """import the numseq package and all submodules"""
    # check for python3
    assert sys.version_info[0] >= 3, "Python version must be 3+"
    has_init = find_spec(f'{PKG_NAME}.__init__') is not None
    assert has_init, 'numseq pkg is missing __init__.py'

    test_class.funcs = []
    for m in ('geo', 'fib', 'prime'):
        mod_name = f'{PKG_NAME}.{m}'
        module = importlib.import_module(mod_name)
        setattr(test_class, m, module)
        funcs = inspect.getmembers(module, inspect.isfunction)
        test_class.funcs.extend(funcs)


class TestNumseq(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Import numseq pkg as class attributes"""
        import_helper(cls)

    def test_fib(self):
        """Checking correctness of fibonacci sequence"""
        self.assertIsInstance(self.fib.fib, types.FunctionType)
        # just test first 30 terms
        for n, f in enumerate(fibs):
            self.assertEqual(self.fib.fib(n), fibs[n], 'The Fibonacci terms are incorrect')

    def test_square(self):
        """Checking correctness of square terms"""
        self.assertIsInstance(self.geo.square, types.FunctionType)
        for n in range(-1000, 1000):
            self.assertEqual(self.geo.square(n), n*n, 'The square terms are incorrect')

    def test_cube(self):
        """Checking correctness of cube terms"""
        self.assertIsInstance(self.geo.cube, types.FunctionType)
        for n in range(-1000, 1000):
            self.assertEqual(self.geo.cube(n), n**3, 'The cube terms are incorrect')

    def test_triangle(self):
        """Checking correctness of triangular number terms"""
        self.assertIsInstance(self.geo.triangle, types.FunctionType)
        for n, t in enumerate(triangles):
            self.assertEqual(self.geo.triangle(n), t)

    def test_is_prime(self):
        """Checking correctness of prime functions"""
        self.assertIsInstance(self.prime.is_prime, types.FunctionType)
        for n in range(max(primes)):
            if n in primes:
                self.assertTrue(self.prime.is_prime(n), str(n) + ' is a prime number')
            else:
                self.assertFalse(self.prime.is_prime(n), str(n) + ' is NOT a prime number')

        self.assertTrue(self.prime.is_prime(999983), '999983 is prime')
        self.assertFalse(self.prime.is_prime(999981), '999981 is not prime')
        self.assertTrue(self.prime.is_prime(1299827), '1299827 is prime')

    def test_primes(self):
        """Checking generating primes up to given value"""
        self.assertIsInstance(self.prime.primes, types.FunctionType)
        for n in range(-1, 2):
            self.assertListEqual(self.prime.primes(n), [], "list should be empty")
        # primes under 1000
        actual = self.prime.primes(1000)
        expected = [p for p in primes if p < 1000]
        self.assertListEqual(actual, expected, "Your prime list does not match expected values")


class TestCodeQuality(unittest.TestCase):
    """Checks performance and quality of functions"""

    @classmethod
    def setUpClass(cls):
        """Import numseq pkg as class attributes"""
        import_helper(cls)

    def test_prime_time(self):
        """Test if prime number generator is inefficient"""
        # This will generate 78498 prime numbers in about 1.5 seconds
        prime_time = timeit.Timer(
            lambda: self.prime.primes(1000000)
            ).repeat(number=1, repeat=1)[0]
        hint = (
            f'The primes(n) function took {prime_time} seconds to run,\n'
            'which exceeds the allowed O(n) threshold of 1.5 seconds'
            )
        self.assertLessEqual(prime_time, 1.5, hint)

    def test_doc_strings(self):
        """Checking for docstrings on all functions"""
        self.assertTrue(self.funcs, "Module functions are missing")
        for func_name, func in self.funcs:
            self.assertIsNotNone(
                func.__doc__,
                f'function "{func_name}" is missing a docstring'
                )
            # arbitrary length test of at least 10 chars
            self.assertGreaterEqual(len(func.__doc__), 10, "How about a bit more docstring?")


if __name__ == '__main__':
    unittest.main()
