#!/usr/bin/env python
"""Unit Test cases for Numseq Package"""

import unittest
import timeit
import importlib
import types

numseq_root = 'numseq'  # change this to 'soln.numseq' to debug solution

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


def numseq_importer(module_name):
    """Helper function to perform import of a numseq module"""
    to_import = numseq_root + '.' + module_name
    try:
        result = importlib.import_module(to_import)
    except ImportError:
        result = 'Unable to import module: ' + to_import
    # could be a module, could be a string
    return result


class TestNumseq(unittest.TestCase):

    def test_fib(self):
        """Test importability and correctness of fibonacci sequence"""
        fib = numseq_importer('fib')
        self.assertIsInstance(fib, types.ModuleType, fib)
        # just test first 30 terms
        for n, f in enumerate(fibs):
            self.assertEqual(fib.fib(n), fibs[n], 'The Fibonacci terms are incorrect')

    # def test_fib_performance(self):
    #     """Test speed performance of fibonacci algorithm"""
    #     # A recursive solution will not perform well here.
    #     pass

    def test_square(self):
        """Test importability and correctness of square terms"""
        geo = numseq_importer('geo')
        self.assertIsInstance(geo, types.ModuleType, geo)
        for n in range(-1000, 1000):
            self.assertEqual(geo.square(n), n*n, 'The square terms are incorrect')

    def test_cube(self):
        """test importability and correctness of cube terms"""
        geo = numseq_importer('geo')
        self.assertIsInstance(geo, types.ModuleType, geo)
        for n in range(-1000, 1000):
            self.assertEqual(geo.cube(n), n**3, 'The cube terms are incorrect')

    def test_triangle(self):
        """Test importability and correctness of triangular number terms"""
        geo = numseq_importer('geo')
        self.assertIsInstance(geo, types.ModuleType, geo)

        for n, t in enumerate(triangles):
            self.assertEqual(geo.triangle(n), t)

    def test_is_prime(self):
        """Test importability and correctness of prime functions"""
        prime = numseq_importer('prime')
        self.assertIsInstance(prime, types.ModuleType, prime)

        for n in range(max(primes)):
            if n in primes:
                self.assertTrue(prime.is_prime(n), str(n) + ' is a prime number')
            else:
                self.assertFalse(prime.is_prime(n), str(n) + ' is NOT a prime number')

        self.assertTrue(prime.is_prime(999983), '999983 is prime')
        self.assertFalse(prime.is_prime(999981), '999981 is not prime')
        self.assertTrue(prime.is_prime(1299827), '1299827 is prime')

    def test_primes(self):
        """Test whether function generates primes up to given value"""
        prime = numseq_importer('prime')
        self.assertIsInstance(prime, types.ModuleType, prime)
        for n in range(-1, 2):
            self.assertListEqual(prime.primes(n), [], "list should be empty")
        # primes under 1000
        actual = prime.primes(1000)
        expected = [p for p in primes if p < 1000]
        self.assertListEqual(actual, expected)


class TestCodeQuality(unittest.TestCase):

    def test_prime_performance(self):
        """Test if prime number generator is inefficient"""
        # This will generate 78498 prime numbers in about 1.5 seconds
        t = timeit.Timer(
            stmt='prime.primes(1000000)',
            setup='from test_numseq import numseq_importer; prime=numseq_importer("prime");'
            )
        prime_time = t.repeat(repeat=1, number=1)[0]
        self.assertLessEqual(prime_time, 1.5)

    def test_doc_strings(self):
        """Test all functions should have doc strings"""
        def check_docstring_length(func):
            # arbitrary length test of at least 10 chars
            self.assertIsNotNone(func.__doc__, 'function "{}" is missing a docstring'.format(func.__name__))
            self.assertGreaterEqual(len(func.__doc__), 10)
        
        prime = numseq_importer('prime')
        self.assertIsInstance(prime, types.ModuleType, prime)
        geo = numseq_importer('geo')
        self.assertIsInstance(geo, types.ModuleType, geo)
        fib = numseq_importer('fib')
        self.assertIsInstance(fib, types.ModuleType, fib)

        check_docstring_length(prime.primes)
        check_docstring_length(prime.is_prime)
        check_docstring_length(fib.fib)
        check_docstring_length(geo.square)
        check_docstring_length(geo.cube)
        check_docstring_length(geo.triangle)


if __name__ == '__main__':
    unittest.main()
