#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "andrewpchristensen701"


def square(num):  
    if isinstance(num, (int, long)):
        return (num * num)
    else:
        return "Invalid Input!"


def triangle(num):   
    if isinstance(num, (int, long)):
        return (num * (num + 1) / 2)
    else:
        return "Invalid Input!"


def cube(num):
    if isinstance(num, (int, long)):
        return num**3
    else:
        return "Invalid Input!"


def main():
    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))


if __name__ == "__main__":
    main()