#!/usr/bin/env python3
"""
Contains a function that takes a list of floats and returns their sum as a
float
"""


def sum_list(input_list: list[float]) -> float:
    """
    Takes an list of floats and returns their sum as a float

    :param input_list: list of floating point values
    :return: sum of all the values in @input_list
    """
    return sum(input_list)
