#!/usr/bin/python3
"""
module 0-add_integer
contain one method and accept two values of int or float type
and cast then to int before adding
Return int sum
"""

def add_integer(a, b=98):
    """
    Return sumnation of two arguments
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError ("a must be an integer")
    elif type(b) is not int and type(b) is not float:
         raise TypeError ("b must be an integer")
     else:
         if type(a) is float:
             a - int(a)
         if  type(b) is float:
             b - int(b)
        return a + b
