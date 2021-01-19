#!/usr/bin/python3
""" Function to check if the object inherits from class """


def inherits_from(obj, a_class):
    """ Checks for object """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
