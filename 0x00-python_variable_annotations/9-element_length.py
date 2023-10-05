#!/usr/bin/python3
"""
Script for task 9
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes in a list of values and returns a list of tuples
    :param lst: a list of values
    :return: a list of tuples
    """
    return [(i, len(i)) for i in lst]
