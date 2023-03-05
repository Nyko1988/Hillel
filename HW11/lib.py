from typing import Union
import string
from random import choice
import random as random_module
from functools import wraps


def int_float_value_checker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        values = [*args]
        values.extend(kwargs.values())

        for value in values:
            if not isinstance(value, (int, float)):
                raise ValueError('I have got not a number')

        result = func(*args, **kwargs)
        return result

    return wrapper


def get_random_number() -> float:
    """
    this function generate random float number
    Returns:
        (float)
    """
    return random_module.random() * random_module.randint(-10 ** 10, 10 ** 10)


@int_float_value_checker
def random_string_generation(length_str: Union[float, int] = 10) -> str:
    """
    this function generates an arbitrary tape of a given length
    Args:
        length_str(float, int):

    Returns:

    """
    return ''.join(choice(string.ascii_lowercase) for elem in range(int(length_str)))
