"""
Beth Harvey
Data Analysis Fundamentals Project 2
January 20, 2023
This is a bonus section for the project. The goal of this section
is to fix the included functions so they pass the doctest, as well
as adding the missing function "convert_ctof" to convert a temperature
in Celsius to Fahrenheit.


>>> add_two(1,2)
3

>>> add_two("hello"," world")
'hello world'

>>> add_triangle_list( [3,4,5] )
12

>>> add_any(1,1,1,1,1,1,1,1)
8

>>> add_any_with_keywords(a=1,b=2)
3

>>> convert_ctof(0)
32.0

>>> convert_ctof(100)
212.0
"""

import doctest

# define some existing functions
def add_two(first, second):
    """Return the sum of any two arguments."""
    sum = first + second  # fix this line
    return sum


def add_triangle_list(list_triangle):
    """Return the sum of three numbers in a list."""
    sum = 0
    for value in list_triangle:
        sum += value  # fix this line to add the value instead of 0
    return sum


def add_any(*args):
    """Return the sum of numbers, using built-in *args."""
    sum = 0
    for x in args:
        sum += x  # fix this line to add x instead of 1
    return sum


def add_any_with_keywords(**kwargs):
    """Return the sum of numbers, using built-in keyword args, **kwargs."""
    sum = 0
    for value in kwargs.values():  # use values() - name doesn't matter
        sum += value  # Use the popular and concise version of sum = sum + x
    return sum


# TODO: implment a new function to convert celsius to fahrenheit
# Use round as needed to make the test pass
# The name of the function is provided in the docstring above


def convert_ctof(celsius):
    deg_f = round((celsius * 1.8 + 32), 2)
    return deg_f


if __name__ == "__main__":

    print("===========================================================")
    print("Running doctest.testmod() function to unit test our code")
    print("===========================================================")
    print()
    doctest.testmod()
    print()
    print("===========================================================")
    print("If you don't see any results, all tests passed.")
