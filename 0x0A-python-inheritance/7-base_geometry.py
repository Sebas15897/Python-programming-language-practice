#!/usr/bin/python3
"""
Defining a geometry class
"""


class BaseGeometry:
    '''BaseGeometry class'''
    def area(self):
        """
        Function that calculates the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        CHeck for validating an integer
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
            
