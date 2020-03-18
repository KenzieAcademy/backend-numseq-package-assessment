import sympy


def primes(n):
    """ Returns a list of all prime numbers less than n"""
    return list(sympy.primerange(0, n))


def is_prime(m):
    """ Returns a boolean indicating whether m is a prime number"""
    if sympy.isprime(m):
        return str(m) + ' is a prime number'
    else:
        return str(m) + ' is not a prime number'
