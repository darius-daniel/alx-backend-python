#!/usr/bin/env python3
"""
Contains a function that takes a mixed list and returns their sum as a float
"""
import typing


def sum_mixed_list(mxd_list: typing.List[typing.Union[float, int]]) -> float:
    """
    Takes in a list of mixed values (ints and floats) and returns their float

    :param mxd_list: a mixed list of floats and ints
    :return: the sum of all the values in @mxd_list
    """
    return sum(mxd_list)
