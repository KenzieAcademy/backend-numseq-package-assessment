#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Julita Marshall"

triangles = {}
cubes = {}

# Returns the nth term of the numbers that can be arranged into square geometric shapes
def square(n):
    return n ** 2
    

# Returns the nth term of the numbers that can be arranged in triangular geometric shapes
def triangle(n):
    return (n*(n + 1)/2)


# Returns the nth term of the numbers that can be arranged as symmetric cube shapes
def cube(n):
    return n ** 3

