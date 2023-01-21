"""
Beth Harvey
Data Analytics Fundamentals
January 20, 2023
Domain: birds
The goal of this task is to update the PyBuddy to answer questions
about my domain. This skills used in this project include: 
object-oriented programming, creating custom classes, and writing 
custom functions.

Build a PyBuddy to extend a welcome.

Uses:

- new Python 3.7 data classes
- list compreshensions for concise processing
- multiline strings -
- some are indented because all the way left seems ugly.

"""

# import from dataclasses to make our job even easier
from dataclasses import dataclass, field

import datetime
from enum import Enum
import statistics as stats
import random
import doctest


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4


# Add the @dataclass decorator to let Python do more of the work
# Notice what changes.


@dataclass
class PyBuddy:
    """PyBuddy data class for creating a study buddy.

    Doctest examples and expected outputs:
    >>> test_1 = PyBuddy(bird_weights_g=[5.2, 13.9, 22.9, 15.6])
    >>> test_1.get_mean_weights()
    14.4
    >>> test_1.moon_weight()
    2.38

    >>> test_2 = PyBuddy(bird_weights_g=[18.52, 9.673, 9.694, 31.0584])
    >>> test_2.get_mean_weights()
    17.24
    >>> test_2.moon_weight()
    2.84
    """

    # With a data class, we just name each field and provide the type.
    # Include a default value in case something is not provied.
    name: str = "Unknown"
    species: Species = 1
    num_legs: int = 4
    weight_kgs: float = 9.999999999
    is_available: bool = True
    skill_list: list = field(default_factory=list)
    create_date = datetime.datetime.now()
    favorite_birds: list = field(default_factory=list)
    bird_weights_g: list = field(default_factory=list)

    def get_age_string(self):
        """Return a string with our age."""
        return str(datetime.datetime.now() - self.create_date)

    def get_availability_string(self):
        """Return a message based on availability."""
        if self.is_available:
            return "I'm available for tutoring."
        else:
            return "I'm already helping others learn Python."

    def get_skills_string(self):
        """Return a nicely formatted string of skills."""
        # use concise list comprehension syntax
        return "".join([str(f"  - {elem}\n") for elem in self.skill_list])

    def display_welcome(self):
        """Display a welcome message from this instance."""

        print(
            f"""
Welcome, I'm a new PyBuddy.
{self.to_string()}
You'll need curiosity, the ability to search the web, 
and the tenacity and resourcefulness
to solve all kinds of challenges.
Let's get started! 

        """
        )

    def to_string(self):
        """Return a custom string describing this instance"""

        # Use an f-string (aka 'formatted string literal')
        # Use curly braces to switch into code that will be executed."
        # Wrap it all in parentheses so we can move the left side.
        return f"""
I'm {self.name}.
I'm a {self.species} with {self.num_legs} legs.
I weigh {self.weight_kgs:.2f} kgs.
I've been alive for {self.get_age_string()}.
I know:
{self.get_skills_string()}
I love birds! My current favorite bird is the {self.get_favorite_bird()},
but it changes all the time!
I also love statistics! The mean weight of all the birds I saw
earlier is {self.get_mean_weights()} grams. That would be {self.moon_weight()} grams on the moon!
"""

    def get_mean_weights(self):
        """Return floating-point mean of bird weights in grams"""
        mean_weight = round(stats.fmean(self.bird_weights_g), 2)
        return mean_weight

    def get_favorite_bird(self):
        """Chooses current favorite bird from a list of favorites"""
        current_favorite = random.choice(self.favorite_birds)
        return current_favorite

    def moon_weight(self):
        moon_weight = round((self.get_mean_weights() * 0.165), 2)
        return moon_weight


# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run, do this:
if __name__ == "__main__":

    # Create an instance of a PyBuddy
    alice = PyBuddy(
        name="Alice",
        species=Species.CAT,
        num_legs=4,
        weight_kgs=8.123456,
        is_available=True,
        skill_list=["Git", "GitHub", "Python", "Markdown", "VS Code"],
        favorite_birds=[
            "Eastern Bluebird",
            "Northern Cardinal",
            "Black-Capped Chickadee",
        ],
        bird_weights_g=[18.3, 12.0, 5.2, 6.8, 9.3],
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
        favorite_birds=["Downy Woodpecker", "White-Breasted Nuthatch", "Mallard"],
        bird_weights_g=[4.9, 15.7, 9.4, 6.3, 12.6],
    )

    rex.display_welcome()

    print("Running doctest.testmod() function to unit test our code")
    print("===========================================================")
    print()
    doctest.testmod()
