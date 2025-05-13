"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


# Defines the 'EXPECTED_BAKE_TIME' and 'PREPARATION_TIME' constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

# Defines the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# Defines the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculates the preparation time in minutes.

    :param number_of_layers: int - number of layers on the lasagna.
    :return: int - the time it takes to prepare the lasagna derived from 'PREPARATION TIME'.

    Function that takes the number of layers on the lasagna as
    an argument and returns how many minutes it will take to prepare the lasagna.
    """
    return(number_of_layers * PREPARATION_TIME)
    
# Defines the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time including preparition time and elapsed_bake_time.

    :param number_of_layers: int - number of layers on the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time in minutes derived from preparation_time_in_minutes and elapsed_bake_time.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument as well as the number of layers on the lasagna and returns the total elapsed time in minutes
    """
    return(preparation_time_in_minutes(number_of_layers) + elapsed_bake_time)

