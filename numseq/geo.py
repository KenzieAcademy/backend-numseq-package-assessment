def square(n):
    """ Returns the nth term of the numbers that
        can be arranged into square geometric shapes"""
    return n * n


def triangle(n):
    """ Returns the nth term of the numbers that
        can be arranged in triangular geometric shapes
    """
    return n*(n+1)/2


def cube(n):
    """Returns the nth term of the numbers that
                can be arranged as symmetric cube shapes"""
    return n**3
