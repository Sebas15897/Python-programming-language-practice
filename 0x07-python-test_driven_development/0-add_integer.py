#!usr/bin/python3
"""Add two integers"""


<<<<<<< HEAD
def add_integer(a, b=98):
    """ Function to add two integers"""
    if type(a) is int or type(a) is float:
        pass
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        pass
    else:
        raise TypeError("b must be an integer")
    return int(a+b)
=======
def add_integer(a, b = 98):
   """ Two variables a and b return the sum """
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError('a must be an integer')
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError('b must be an integer')
    return int(a + b)
>>>>>>> 5940a1f280636d54acae92ef5a70e68aaadeb274
