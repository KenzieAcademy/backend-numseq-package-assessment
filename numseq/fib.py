def fib(n):
    """ Find the given (nth) number in the Fibonacci Sequence"""
    a, b = 0, 1
    for index in range(n):
        a, b = b, a + b
    return a
