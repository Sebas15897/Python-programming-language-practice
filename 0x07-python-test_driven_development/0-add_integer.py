#!/usr/bin/python3
"""This is a simple function that adds 2 integers."""


def add_integer(a, b=98):
   """Two variables a and b return the sum"""
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError('a must be an integer')
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError('b must be an integer')
    return int(a + b)
