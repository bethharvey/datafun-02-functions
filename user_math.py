"""
Beth Harvey
Data Analysis Fundamentals Project 2
January 19, 2023

The goal of this project is to write custom functions using try/except blocks
and use functions from the math module.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions


def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could fail if one of the entered arguments is 0, a negative number,
    or not a number.

    """

    # Use a try / except / finally block when something
    # could go wrong
    try:
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)


def bird_count(*args):
    """
    Returns count of birds seen at the bird feeder in a day

    """
    total = 0

    for arg in args:
        if (type(arg) != int) or (arg < 0):
            print("Please enter whole integer values.")
            quit()
    for arg in args:
        try:
            total += arg

        except Exception as ex:
            print(f"Error: {ex}")
            return None

    return total


# -------------------------------------------------------------


def cost_of_bird_food(
    sunflower_seed_cost, sunflower_quantity, suet_cost, suet_quantity
):
    """
    Returns total cost of bird food purchase based on type and quantity

    """
    try:
        sunflower_total = sunflower_seed_cost * sunflower_quantity
        suet_total = suet_cost * suet_quantity
        total = math.fsum([sunflower_total + suet_total])
        return total

    except Exception as ex:
        print(f"Error: {ex}")
        return None


# -------------------------------------------------------------


def daily_avg_count(mon, tue, wed, thur, fri, sat, sun):
    """
    Returns the average number of birds spotted per day
    in one week. Rounds down to the nearest integer. No
    one wants to see partial birds!

    """
    try:
        week_total = mon + tue + wed + thur + fri + sat + sun
        daily_avg = math.floor(week_total / 7)
        return daily_avg

    except Exception as ex:
        print(f"Error: {ex}")
        return None


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functionsin the math module")
    print()
    print(f"math.comb(5, 1) = {math.comb(5, 1)}")
    print(f"math.perm(5, 1) = {math.comb(5, 1)}")
    print()
    print(f"get_area_of_lot(6, 2) = {get_area_of_lot(6, 2)}")
    print()
    print(f"Number of birds seen today = {bird_count(3, 7, 2, 11)}")
    print()
    print(f"Bird food purchase cost = {cost_of_bird_food(14.32, 2, 1.92, 6)}")
    print()
    print(
        f"Average birds spotted per day this week = {daily_avg_count(23, 38, 18, 20, 33, 51, 29)}"
    )
