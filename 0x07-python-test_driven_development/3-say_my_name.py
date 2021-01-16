#!/usr/bin/python3
"""
    funtion to print two names
"""


def say_my_name(first_name, last_name=""):
    """
    >>> tester = __import__('3-say_my_name').say_my_name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is " + first_name + " " + last_name)
