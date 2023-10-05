#!/usr/bin/env python3
"""
Contains a type annotated function
"""
from typing import Union, Tuple
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """
    Takes in a string and an int or float and returns a tuple
    :param k: a string
    :param v: a float or int
    :return: a tuple with the value of @k as its first element, and the square
        of the value of @v as its second element
    """
    return k, math.pow(v, 2)
