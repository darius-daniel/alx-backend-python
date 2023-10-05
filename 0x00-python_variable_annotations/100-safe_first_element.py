#!/usr/bin/env python3
"""
Script for Task 10 (First Advanced Task)
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Demonstrating duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
