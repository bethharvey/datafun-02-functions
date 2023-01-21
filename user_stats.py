"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics as stats

# define a variable with some univariant data
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

# Calculate measures of central tendency for agility scores
score_mean = stats.mean(scores)
score_median = stats.median(scores)
score_mode = stats.mode(scores)
score_variance = stats.pvariance(scores)
score_st_dev = stats.pstdev(scores)

print(f"The mean score for the agility test was {score_mean}.")
print(f"The median score for the agility test was {score_median}.")
print(f"The mode of all the agility test scores was {score_mode}.")
print(f"The variance of the agility test scores was {round(score_variance, 2)}.")
print(
    f"The standard deviation of the agility test scores was {round(score_st_dev, 2)}."
)
print()

# Calculate slope and intercept of best fit line
slope, intercept = stats.linear_regression(x_times, y_temps)
print(
    f"""The best fit line for the time and temperature data has
a slope of {round(slope, 2)} and an intercept of {round(intercept, 2)}."""
)
print()

# Use slope and intercept to predict the temperature at hour 13
x_future = 13
y_future = slope * x_future + intercept
print(
    f"""Based on the temperatures over the previous 12 hours, the 
temperature in one hour will be {round(y_future, 0)} degrees."""
)
