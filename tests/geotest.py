#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import geo


class TestGeo(unittest.TestCase):


    def test_square(self):
        square_zero = geo.square(0)
        square_eight = geo.square(8)
        string_input = geo.square("String")
        self.assertEquals(square_zero, 0)
        self.assertEquals(square_eight, 64)
        self.assertEquals(string_input, "Invalid Input!")

    def test_triangle(self):
        triangle_two = geo.triangle(2)
        triangle_five = geo.triangle(5)
        string_input = geo.triangle("String")
        self.assertEquals(triangle_two, 3)
        self.assertEquals(triangle_five, 15)
        self.assertEquals(string_input, "Invalid Input!")

    def test_cube(self):
        cube_three = geo.cube(3)
        cube_five = geo.cube(5)
        string_input = geo.cube("String")
        self.assertEquals(cube_three, 27)
        self.assertEquals(cube_five, 125)
        self.assertEquals(string_input, "Invalid Input!")