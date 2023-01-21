"""
Build a PyBuddy to illustrate Python skills.

Overview:

This example introduces a common way to organize code - into
classes that reflect the real world.

Each class is a combination of attributes (data)
and methods (functions) that operate on that data.

Look for the nouns in your application. 
For example, if you want to code a poker game, you'd make classes for:

- Card, Deck, Hand, Player, Game, etc.

You then use the Card class to create 52 instances of cards,
each with a number/rank and suit, 
e.g. an instance/object to represent the Jack of Spades.

Object-Oriented Programming in Python

- Python allows you to create classes - or data classes
- You don't have to organize your code this way
- Implement classes where you'll instantiate one or more with 
  specific data. Do want makes sense.

We'll use it here, because we want to instantiate 
several PyBuddies, each with different attributes, 
but sharing common behaviors (methods).

A method is a function that is part of a class.

When instantating a PyBuddy, you can create 
a DOG, a CAT, an ELF, or other type.

Python Organization:

Unlike other languages, 
Python does not always have just one class per file.
In this file, we have our enumerated class for the species, 
as well as the main PyBuddy class.

This example:

- uses an object-oriented approach
- wraps functionality into a named class
- the class can be instantiated many times
- (e.g. a cat named Boots, a dog named Rex)
- classes define:
    - properties (class data)
    - methods (class functions)

All Python classes need a built-in class method called __init__:
__init__ is used to create an instance of this class

Python includes an implicit pointer to the instance as a whole
By convention, 
most analysts name this first implicit parameter 'self'
You can change it, but violating customs is considered bad form.
"""

# first, import helpful modules to make our job easier

import datetime
from enum import Enum


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4


class PyBuddy:
    """PyBuddy class for creating a study buddy."""

    def __init__(self, name, species, num_legs, weight_kgs, is_available, skill_list):
        """Built-in method to create a new instance."""
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.weight_kgs = weight_kgs
        self.is_available = is_available
        self.skill_list = skill_list
        self.create_date = datetime.datetime.now()

    def __str__(self):
        """Built-in method to return a string describing this instance"""
        s0 = f"I'm {self.name}.\n"
        s1 = f"I'm a {self.species} with {self.num_legs} legs.\n"
        s2 = f"I weigh {self.weight_kgs:.2f} kgs.\n"
        s3 = f"I've been alive for {self.get_age_string()}.\n"

        if self.is_available:
            s4 = "I'm available for tutoring.\n"
        else:
            s4 = "I'm already helping others learn Python.\n"

        s5 = "I know:\n"

        s6 = ""
        for skill in self.skill_list:
            s6 = s6 + f"  - {skill}\n"

        s = s0 + s1 + s2 + s3 + s4 + s5 + s6
        return s

    def get_age_string(self):
        """Return the age as a string."""
        start = self.create_date
        end = datetime.datetime.now()
        duration = end - start
        ageString = str(duration)
        return ageString

    def display_welcome(self):
        print()
        print("Welcome, I'm a new PyBuddy.\n")
        # print using our built-in to string method
        print(self.__str__())

        final_message = """

        You'll need curiousity, the ability to search the web,
        and the tenacity and resourcefulness
        to solve all kinds of challenges.

        Let's get started!

        """
        print(final_message)


# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run

if __name__ == "__main__":
    # Create an instance of a PyBuddy
    alice = PyBuddy(
        "Alice",
        Species.CAT,
        4,
        8.123456,
        True,
        ["Git", "GitHub", "Python", "Markdown", "VS Code"],
    )

    # Call the buddy's welcome() method
    alice.display_welcome()

    # Create another instance of a PyBuddy
    # using named arguments so it's clear what we're doing
    rex = PyBuddy(
        name="Rex",
        species=Species.DOG,
        num_legs=4,
        weight_kgs=10.437241,
        is_available=True,
        skill_list=["Git", "GitHub", "Python", "Markdown", "VS Code"],
    )

    rex.display_welcome()
