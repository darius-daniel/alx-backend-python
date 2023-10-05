#!/usr/bin/env python3
"""
Script for task 11 (second advanced task)
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Demonstrating annotation of dictionaries
    :param dct: a dictionary
    :param key: a key
    :param default: default value
    :return: ...
    """
    if key in dct:
        return dct[key]
    else:
        return default
