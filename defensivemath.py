"""
This modules illustrates the math module and how to write
defensive functions by trying to use them, 
but if things don't work provide a custom message.

Use try / except / finally whenever a function could cause an error
e.g.,
- a number is not valid such as a negative radius or age
- a string is empty or missing
- the requested resouce could not be found

The math module includes:
- pi
- sin/cos/tan
- factorial
- sqrt for square root
- cbrt (in 3.11) for cube root
- comb(n,k) for combinations i.e.,
    number of ways to choose k items from n items
    w/out repetition and w/out order
- perm(n,k) for permuations i.e.,
    number of ways to choose k items from n items
    w/out repetition and With order

Uses:
- math - to get some advanced math

"""

import math

# define some functions


def get_circle_area(radius):
    """
    Return area of a circle given the radius.

    Keyword arguments:
    radius -- the radius of the circle

    This could fail - for example, what is the
    area of a circle with a negative radius?
    Or a circle with an infinite radius?

    """

    # Use a try / except / finally block when something
    # could go wrong
    if radius <= 0:
        print("Radius must be positive.")
    else:
        try:
            area = 2 * math.pi * radius
            return area
        except Exception as ex:
            print(f"Error: {ex}")
            return None


def print_circle_areas(lst):
    """
    This function should print the area of each radius

    Keyword arguments:
    lst -- a list of radius values (possibly invalid)
    """
    if len(lst) == 0:
        print("Error: please add some items to the list.")
        quit()  # quit the program

    # for every item in the list
    for r in lst:

        try:
            area = get_circle_area(r)
            print(f"r = {r}, area={area}")

        except Exception as ex:
            print(f"r = {r}, Error: {ex}")


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()
    print(f"math.comb(5,3) = {math.comb(5,3)}")
    print(f"math.perm(5,3) = {math.perm(5,3)}")
    print()
    print(f"math.pi = {math.pi}")
    print()
    print(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    print(f"math.radians(180)         = {math.radians(180)}")
    print()
    print("Call get_circle_area() function with a different values, 5")
    print()
    print(f"get_circle_area(5) = {get_circle_area(5)}")
    print(f"get_circle_area(-16) = {get_circle_area(-16)}")
    print(f"get_circle_area(math.inf) = {get_circle_area(math.inf)}")
    print(f"get_circle_area('five') = {get_circle_area('five')}")
    print()
    print("Call print_circle_areas() function with a list of values")
    print()
    lst_values = [5, 10, 25, 30, 45, 50]
    print_circle_areas(lst_values)
    print()
