"""
CONSOLE VERSION EXCEPTIONS!
File ConsoleExceptions contains all functions
    of project that raises Exceptions in CONSOLE VERSION.
"""
from PIL import Image

MAX_ATR = 300
MAX_STEPS = 30000


class InputError(Exception):
    """
    Class InputError, inherits from Exception.
    """
    pass


def check_start_exceptions(option):
    """
    ~ Function checks whether given option is "1"/"2"/"3"
    """
    set_of_options = {"1", "2", "3"}
    if option not in set_of_options:
        raise InputError("You need to choose between 1/2/3!")


def check_probability_exceptions(probability):
    """
    ~ Function checks whether given probability is:
        1) type float
        2) number between 0 and 1
    """
    try:
        probability_to_float = float(probability)
        if probability_to_float < 0 or probability_to_float >= 1:
            raise InputError("Probability must be a number between 0 and 1!")
    except ValueError:
        raise InputError("Probability needs to be float!")


def check_creating_picture_exceptions(size):
    """
    ~ Function checks whether given size is:
        1) type int
        2) number between 1 and 300 (min and max size).
    """
    try:
        size_to_int = int(size)
        if size_to_int > MAX_ATR or size_to_int < 1:
            raise InputError(f"Max allowed size is {MAX_ATR}x{MAX_ATR}!")
    except ValueError:
        raise InputError("A number need to be given!")


def check_yes_or_no(option):
    """
    ~ Function checks whether given option is "y"/"n".
    """
    set_of_options = {"y", "n"}
    if option not in set_of_options:
        raise InputError("You need to type y/n!")


def check_load_picture_exceptions(path):
    """
    ~ Function checks whether given path exists.
    """
    try:
        _ = Image.open(path)
    except FileNotFoundError:
        raise InputError("Correct path need to be given!")


def step_exceptions(steps):
    """
    ~ Function checks whether given steps is:
        1) type int
        2) number > 0
    """
    try:
        steps_int = int(steps)
        if steps_int <= 0:
            raise InputError("A number bigger than 0 need to be given!")
    except ValueError:
        raise InputError("A number need to be given")
