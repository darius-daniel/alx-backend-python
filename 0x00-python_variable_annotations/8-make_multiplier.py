#!/usr/bin/env python3
"""
Task 8 Script
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes float and returns a function that multiplies a float by @multiplier
    :param multiplier: a float
    :return: a function that multiplies a float by @multiplier
    """
    return lambda x: x * multiplier
