#!/usr/bin/env python3
"""
Contains a function that takes a mixed list and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Takes in a list of mixed values (ints and floats) and returns their float

    :param mxd_list: a mixed list of floats and ints
    :return: the sum of all the values in @mxd_list
    """
    return float(sum(mxd_list))
